import yaml
import copy
import json

def load_openapi_spec(file_path):
    """OpenAPI 명세를 YAML 파일에서 로드합니다."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def resolve_schema_ref(ref, spec):
    """$ref 문자열을 통해 실제 스키마 객체를 찾습니다."""
    if not ref.startswith('#/'):
        return None
        
    ref_path = ref.replace('#/', '').split('/')
    ref_obj = spec
    for path in ref_path:
        if path in ref_obj:
            ref_obj = ref_obj[path]
        else:
            return None
    return ref_obj

def convert_refs(spec):
    """전체 스펙에서 모든 $ref 참조를 실제 객체로 변환합니다."""
    # 참조된 컴포넌트를 복사해서 사용
    components = spec.get('components', {})
    
    def resolve_ref(obj):
        """객체 내의 $ref를 재귀적으로 해결합니다."""
        if isinstance(obj, dict):
            if '$ref' in obj:
                ref_path = obj['$ref'].replace('#/', '').split('/')
                ref_obj = spec
                for path in ref_path:
                    ref_obj = ref_obj.get(path, {})
                
                # 원본 객체와 참조된 객체를 병합
                resolved = copy.deepcopy(ref_obj)  # 깊은 복사를 수행하여 원본 참조 데이터가 변경되지 않도록 함
                obj.pop('$ref')  # $ref 키 제거
                
                # 나머지 키들이 있으면 병합
                for key, value in obj.items():
                    resolved[key] = value
                    
                return resolve_ref(resolved)  # 결과 객체에 중첩된 참조가 있을 수 있으므로 재귀 호출
            else:
                # $ref가 없는 일반 객체는 각 속성에 대해 재귀적으로 처리
                return {k: resolve_ref(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            # 리스트의 각 항목을 재귀적으로 처리
            return [resolve_ref(item) for item in obj]
        else:
            # 기본 타입은 그대로 반환
            return obj
    
    # 경로 정의에 있는 모든 참조 해결
    paths = spec.get('paths', {})
    resolved_paths = resolve_ref(paths)
    
    # 복사본 생성 및 업데이트된 paths 할당
    resolved_spec = copy.deepcopy(spec)
    resolved_spec['paths'] = resolved_paths
    
    return resolved_spec

def escape_markdown(text):
    """마크다운에서 특수 문자를 이스케이프 처리합니다."""
    if not isinstance(text, str):
        return text
        
    # 마크다운에서 이스케이프 처리가 필요한 특수 문자
    special_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!']
    for char in special_chars:
        text = text.replace(char, '\\' + char)
    return text

def format_schema_as_table(schema, title=None):
    """스키마를 마크다운 테이블로 변환합니다."""
    if not schema or not isinstance(schema, dict) or 'properties' not in schema:
        return "속성이 정의되지 않았습니다."

    table = []
    if title:
        table.append(f"{title}\n")
    
    table.append("| 이름 | 타입 | 필수 여부 | 설명 |")
    table.append("|------|------|:--------:|------|")
    
    # 먼저 모든 기본 필드 처리
    flat_fields = []
    required_props = schema.get('required', [])
    
    # 기본 필드를 평탄화된 형식으로 수집
    def collect_fields(properties, prefix="", is_required=False, parent_required=False):
        for prop_name, prop in properties.items():
            if not isinstance(prop, dict):
                continue
                
            field_name = f"{prefix}{prop_name}"
            prop_type = prop.get('type', '-')
            prop_desc = escape_markdown(prop.get('description', '-'))
            
            # 해당 속성이 필수인지 확인
            field_required = prop_name in required_props or is_required
            # 상위 객체가 필수이면 모든 하위 필드도 필수로 표시
            field_required = field_required or parent_required
            required_mark = "✓" if field_required else ""
            
            # 배열 표기법 조정
            if prop_type == 'array' and 'items' in prop:
                items = prop['items']
                if isinstance(items, dict):
                    item_type = items.get('type', '-')
                    # 객체 배열
                    if item_type == 'object' or 'properties' in items:
                        flat_fields.append({
                            "name": f"`{field_name}[]`",
                            "type": f"array&lt;object&gt;",  # < > 이스케이프 처리
                            "required": required_mark,
                            "desc": prop_desc
                        })
                        # 배열 항목의 속성들 재귀적으로 추가
                        if 'properties' in items:
                            for sub_name, sub_prop in items['properties'].items():
                                sub_type = sub_prop.get('type', '-')
                                sub_desc = escape_markdown(sub_prop.get('description', '-'))
                                sub_required = sub_name in items.get('required', [])
                                flat_fields.append({
                                    "name": f"`{field_name}[].{sub_name}`",
                                    "type": sub_type,
                                    "required": "✓" if sub_required or field_required else "",
                                    "desc": sub_desc
                                })
                    # 기본 타입 배열
                    else:
                        flat_fields.append({
                            "name": f"`{field_name}[]`",
                            "type": f"array&lt;{item_type}&gt;",  # < > 이스케이프 처리
                            "required": required_mark,
                            "desc": prop_desc
                        })
            # 객체 타입
            elif prop_type == 'object' and 'properties' in prop:
                flat_fields.append({
                    "name": f"`{field_name}`",
                    "type": "object",
                    "required": required_mark,
                    "desc": prop_desc
                })
                # 객체 속성 전개
                sub_required_props = prop.get('required', [])
                for sub_name, sub_prop in prop['properties'].items():
                    sub_type = sub_prop.get('type', '-')
                    sub_desc = escape_markdown(sub_prop.get('description', '-'))
                    sub_required = sub_name in sub_required_props
                    flat_fields.append({
                        "name": f"`{field_name}.{sub_name}`",
                        "type": sub_type,
                        "required": "✓" if sub_required or field_required else "",
                        "desc": sub_desc
                    })
            # 일반 필드
            else:
                flat_fields.append({
                    "name": f"`{field_name}`",
                    "type": prop_type,
                    "required": required_mark,
                    "desc": prop_desc
                })
    
    collect_fields(schema.get('properties', {}))
    
    # 테이블에 모든 필드 추가
    for field in flat_fields:
        table.append(f"| {field['name']} | {field['type']} | {field['required']} | {field['desc']} |")
    
    return "\n".join(table)

def generate_markdown(spec):
    """OpenAPI 스펙에서 마크다운 문서를 생성합니다."""
    markdown = []
    resolved_spec = convert_refs(spec)  # 전체 스펙의 $ref를 해결

    # 제목 및 설명
    title = spec['info'].get('title', 'API Documentation')
    description = spec['info'].get('description', '')
    version = spec['info'].get('version', '')
    markdown.append(f"# {title} v{version}\n")
    markdown.append(f"{description}\n")

    # 서버 정보
    if 'servers' in spec and spec['servers']:
        markdown.append("## 서버 정보\n")
        for server in spec['servers']:
            server_url = server.get('url', '')
            server_desc = server.get('description', '')
            markdown.append(f"- {server_url} - {server_desc}")
        markdown.append("\n")

    # 목차
    markdown.append("## 목차\n")
    
    # 태그별 목차 구성
    tags = {tag['name']: tag.get('description', '') for tag in spec.get('tags', [])}
    endpoints_by_tag = {}
    
    # 태그별로 엔드포인트 분류
    for path, methods in spec['paths'].items():
        for method in methods:
            method_details = methods[method]
            method_tags = method_details.get('tags', ['기타'])
            
            for tag in method_tags:
                if tag not in endpoints_by_tag:
                    endpoints_by_tag[tag] = []
                
                summary = method_details.get('summary', '')
                anchor = f"{method.lower()}-{path.replace('/', '-').replace('{', '').replace('}', '')}"
                endpoints_by_tag[tag].append({
                    'method': method.upper(),
                    'path': path,
                    'summary': summary,
                    'anchor': anchor
                })
    
    # 태그별로 목차 출력
    for tag in sorted(endpoints_by_tag.keys()):
        tag_description = tags.get(tag, '')
        markdown.append(f"### {tag} {tag_description}\n")
        
        for endpoint in sorted(endpoints_by_tag[tag], key=lambda x: x['path']):
            markdown.append(f"- [{endpoint['method']} {endpoint['path']}](#{endpoint['anchor']}) - {endpoint['summary']}")
        
        markdown.append("\n")

    # Content-Type에 따른 코드 블록 형식 매핑
    content_type_format = {
        'application/json': 'json',
        'application/xml': 'xml',
        'text/plain': 'text',
        'text/html': 'html',
        'application/x-www-form-urlencoded': 'http'
    }
    
    # 기본 형식은 yaml
    def get_format_for_content_type(content_type):
        for ct_prefix, fmt in content_type_format.items():
            if content_type.startswith(ct_prefix):
                return fmt
        return 'yaml'  # 기본값
    
    # Dict를 XML로 변환
    def dict_to_xml_example(data, schema, root_name="root", indent=""):
        """
        Python 사전을 XML 문자열로 변환
        schema에서 xml 정보를 이용하여 태그 이름 결정
        """
        # 최상위 XML 태그 이름 결정
        xml_lines = []
        
        # 루트 요소의 XML 이름 정보 가져오기
        root_xml_name = root_name
        if schema and 'xml' in schema and 'name' in schema['xml']:
            root_xml_name = schema['xml']['name']
        
        if isinstance(data, dict):
            xml_lines.append(f"{indent}<{root_xml_name}>")
            next_indent = indent + "  "
            
            # dict의 각 항목을 XML 요소로 변환
            for key, value in data.items():
                if value is None:
                    continue
                
                # 현재 키에 해당하는 스키마 찾기
                prop_schema = None
                if schema and 'properties' in schema:
                    prop_schema = schema['properties'].get(key, {})
                
                # XML 이름 결정 - 'name'과 같은 특별한 필드가 'n'으로 잘못 변환되는 문제 해결
                xml_name = key  # 기본값은 키 이름 그대로 사용
                
                # 특정 키 처리 - 'name'이 'n'으로 출력되는 문제 해결
                if key == 'name':
                    xml_name = 'name'  # 항상 'name'으로 출력
                elif prop_schema:
                    # 속성에 xml 정보가 있으면 그것을 사용
                    if 'xml' in prop_schema and 'name' in prop_schema['xml']:
                        xml_name = prop_schema['xml']['name']
                    # $ref 참조가 있는 경우
                    elif '$ref' in prop_schema:
                        ref_schema = resolve_schema_ref(prop_schema['$ref'], spec)
                        if ref_schema and 'xml' in ref_schema and 'name' in ref_schema['xml']:
                            xml_name = ref_schema['xml']['name']
                
                # 값이 딕셔너리인 경우 재귀 호출
                if isinstance(value, dict):
                    if prop_schema and '$ref' in prop_schema:
                        ref_schema = resolve_schema_ref(prop_schema['$ref'], spec)
                        if ref_schema:
                            xml_lines.append(dict_to_xml_example(value, ref_schema, xml_name, next_indent))
                        else:
                            xml_lines.append(dict_to_xml_example(value, {}, xml_name, next_indent))
                    else:
                        xml_lines.append(dict_to_xml_example(value, prop_schema, xml_name, next_indent))
                # 값이 리스트인 경우
                elif isinstance(value, list):
                    if prop_schema and 'type' in prop_schema and prop_schema['type'] == 'array':
                        # 배열이 wrapped인지 확인
                        wrapped = False
                        if 'xml' in prop_schema and 'wrapped' in prop_schema['xml'] and prop_schema['xml']['wrapped']:
                            wrapped = True
                            xml_lines.append(f"{next_indent}<{xml_name}>")
                            wrap_indent = next_indent + "  "
                        else:
                            wrap_indent = next_indent
                        
                        # 배열 항목의 스키마 가져오기
                        items_schema = prop_schema.get('items', {})
                        item_xml_name = 'item'  # 기본 이름
                        
                        # 배열 항목의 XML 이름 결정
                        if 'xml' in items_schema and 'name' in items_schema['xml']:
                            item_xml_name = items_schema['xml']['name']
                        elif '$ref' in items_schema:
                            ref_items_schema = resolve_schema_ref(items_schema['$ref'], spec)
                            if ref_items_schema and 'xml' in ref_items_schema and 'name' in ref_items_schema['xml']:
                                item_xml_name = ref_items_schema['xml']['name']
                        
                        # 배열이 비어 있을 때도 적절한 형식으로 표시
                        if not value:
                            # 빈 배열이지만 wrapped인 경우 열고 닫는 태그만 표시
                            if wrapped:
                                xml_lines.append(f"{next_indent}</{xml_name}>")
                            # 비어있고, wrapped가 아닌 경우 - 아무것도 추가하지 않음
                        else:
                            # 배열 각 항목에 대해 처리
                            for item in value:
                                if isinstance(item, dict):
                                    if '$ref' in items_schema:
                                        ref_items_schema = resolve_schema_ref(items_schema['$ref'], spec)
                                        if ref_items_schema:
                                            xml_lines.append(dict_to_xml_example(item, ref_items_schema, item_xml_name, wrap_indent))
                                        else:
                                            xml_lines.append(dict_to_xml_example(item, {}, item_xml_name, wrap_indent))
                                    else:
                                        xml_lines.append(dict_to_xml_example(item, items_schema, item_xml_name, wrap_indent))
                                else:
                                    # 원시 타입 항목
                                    xml_lines.append(f"{wrap_indent}<{item_xml_name}>{item}</{item_xml_name}>")
                            
                            # 배열이 wrapped인 경우 닫는 태그 추가
                            if wrapped:
                                xml_lines.append(f"{next_indent}</{xml_name}>")
                    else:
                        # 스키마 정보가 없는 경우 기본 처리
                        if value:  # 배열이 비어있지 않을 때만 처리
                            for item in value:
                                if isinstance(item, dict):
                                    xml_lines.append(dict_to_xml_example(item, {}, xml_name, next_indent))
                                else:
                                    xml_lines.append(f"{next_indent}<{xml_name}>{item}</{xml_name}>")
                # 일반 값인 경우
                else:
                    xml_lines.append(f"{next_indent}<{xml_name}>{value}</{xml_name}>")
            
            xml_lines.append(f"{indent}</{root_xml_name}>")
        else:
            # 원시 타입 값
            xml_lines.append(f"{indent}<{root_xml_name}>{data}</{root_xml_name}>")
        
        return "\n".join(xml_lines)
    
    # Dict를 form 데이터로 변환
    def dict_to_form(d, parent_key=""):
        form_str = []
        
        if isinstance(d, dict):
            for key, value in d.items():
                new_key = f"{parent_key}.{key}" if parent_key else key
                if isinstance(value, dict):
                    form_str.extend(dict_to_form(value, new_key))
                elif isinstance(value, list):
                    for i, item in enumerate(value):
                        list_key = f"{new_key}[{i}]"
                        if isinstance(item, dict):
                            form_str.extend(dict_to_form(item, list_key))
                        else:
                            form_str.append(f"{list_key}={item}")
                else:
                    form_str.append(f"{new_key}={value}")
        elif isinstance(d, list):
            for i, item in enumerate(d):
                list_key = f"{parent_key}[{i}]"
                if isinstance(item, dict):
                    form_str.extend(dict_to_form(item, list_key))
                else:
                    form_str.append(f"{list_key}={item}")
        else:
            form_str.append(f"{parent_key}={d}")
            
        return form_str

    # 스키마에서 예시 데이터 생성
    def generate_example_from_schema(schema):
        if not schema or not isinstance(schema, dict):
            return {}
            
        result = {}
        if 'type' in schema:
            if schema['type'] == 'object' and 'properties' in schema:
                for prop_name, prop in schema['properties'].items():
                    if 'example' in prop:
                        # 스키마에 example이 정의되어 있으면 그것을 사용
                        result[prop_name] = prop['example']
                    elif 'type' in prop:
                        if prop['type'] == 'string':
                            # 영문 예시 문자열 사용
                            result[prop_name] = f"example_{prop_name}"
                        elif prop['type'] == 'integer':
                            result[prop_name] = 0
                        elif prop['type'] == 'number':
                            result[prop_name] = 0.0
                        elif prop['type'] == 'boolean':
                            result[prop_name] = False
                        elif prop['type'] == 'array':
                            # 배열에 대해 항목의 예시 추가
                            items_schema = prop.get('items', {})
                            if items_schema:
                                if '$ref' in items_schema:
                                    ref_schema = resolve_schema_ref(items_schema['$ref'], spec)
                                    if ref_schema:
                                        # 참조된 스키마를 사용하여 예시 항목 생성
                                        result[prop_name] = [generate_example_from_schema(ref_schema)]
                                    else:
                                        # 문자열 배열인 경우 일관된 예시 추가
                                        if items_schema.get('type') == 'string':
                                            result[prop_name] = [f"example_{prop_name}_{i}" for i in range(1, 3)]
                                        else:
                                            result[prop_name] = []
                                else:
                                    # items 유형에 따라 적절한 예시 생성
                                    if items_schema.get('type') == 'string':
                                        # 모든 문자열 배열에 동일한 포맷 적용
                                        result[prop_name] = [f"example_{prop_name}_{i}" for i in range(1, 3)]
                                    elif items_schema.get('type') == 'integer':
                                        result[prop_name] = [i for i in range(1, 3)]
                                    elif items_schema.get('type') == 'object':
                                        result[prop_name] = [generate_example_from_schema(items_schema)]
                                    else:
                                        result[prop_name] = [generate_example_from_schema(items_schema)]
                            else:
                                result[prop_name] = []
                        elif prop['type'] == 'object':
                            result[prop_name] = generate_example_from_schema(prop)
            elif schema['type'] == 'array' and 'items' in schema:
                items_schema = schema.get('items', {})
                if '$ref' in items_schema:
                    ref_schema = resolve_schema_ref(items_schema['$ref'], spec)
                    if ref_schema:
                        return [generate_example_from_schema(ref_schema)]
                
                # items 유형에 따라 적절한 예시 생성
                if items_schema.get('type') == 'string':
                    return [f"example_item_{i}" for i in range(1, 3)]
                elif items_schema.get('type') == 'integer':
                    return [i for i in range(1, 3)]
                
                return [generate_example_from_schema(items_schema)]
                
        return result

    # 태그별 엔드포인트 출력
    for tag, endpoints in sorted(endpoints_by_tag.items()):
        markdown.append(f"## {tag}\n")
        
        # 태그에 대한 설명 추가
        if tag in tags:
            markdown.append(f"{tags[tag]}\n")
        
        # 해당 태그의 모든 엔드포인트 출력
        for endpoint in sorted(endpoints, key=lambda x: x['path']):
            path = endpoint['path']
            method = endpoint['method'].lower()
            details = resolved_spec['paths'][path][method]
            
            method_upper = method.upper()
            summary = details.get('summary', 'No summary provided')
            description = details.get('description', 'No description provided')
            
            # 메서드와 경로를 포함한 제목 형식 - 메서드를 먼저 표시
            anchor = endpoint['anchor']
            markdown.append(f"<h3 id='{anchor}'>{method_upper} {path}</h3>\n")
            markdown.append(f"**{summary}**\n")
            markdown.append(f"{description}\n")

            # 인증 정보
            if 'security' in details and details['security']:
                markdown.append("\n**인증 요구사항:**\n")
                for security_req in details['security']:
                    for scheme_name, scopes in security_req.items():
                        markdown.append(f"- {scheme_name}")
                        if scopes:
                            markdown.append(f"  - 스코프: {', '.join(scopes)}")
                markdown.append("\n")

            # 요청 정보 - 수준을 #### 로 조정
            markdown.append("#### 요청\n")
            if 'parameters' in details:
                markdown.append("\n**파라미터:**\n")
                
                # 파라미터를 위치별로 분류
                params_by_location = {}
                for param in details['parameters']:
                    location = param.get('in', 'unknown')
                    if location not in params_by_location:
                        params_by_location[location] = []
                    params_by_location[location].append(param)
                
                # 위치별로 파라미터 테이블 생성
                for location, params in params_by_location.items():
                    markdown.append(f"\n**{location} 파라미터:**\n")
                    markdown.append("| 이름 | 타입 | 필수 여부 | 설명 |")
                    markdown.append("|------|------|:--------:|------|")
                    
                    for param in params:
                        name = param.get('name', 'unknown')
                        required = "✓" if param.get('required', False) else ""
                        description = escape_markdown(param.get('description', '-'))
                        
                        if 'schema' in param:
                            schema = param['schema']
                            param_type = schema.get('type', '-')
                            if param_type == 'array' and 'items' in schema:
                                items = schema['items']
                                item_type = items.get('type', '-')
                                param_type = f"array&lt;{item_type}&gt;"  # < > 이스케이프 처리
                        else:
                            param_type = param.get('type', '-')
                        
                        markdown.append(f"| `{name}` | {param_type} | {required} | {description} |")
                markdown.append("\n")

            # 요청 본문
            if 'requestBody' in details:
                markdown.append("\n**요청 본문:**\n")
                request_body = details['requestBody']
                request_description = request_body.get('description', '')
                if request_description:
                    markdown.append(f"{request_description}\n")

                if 'content' in request_body:
                    schema_displayed = False
                    schema_info = {}  # 스키마 정보 저장
                    
                    # 모든 content 타입에서 스키마 정보 수집
                    for content_type, content_details in request_body['content'].items():
                        schema = content_details.get('schema')
                        if schema and not schema_displayed:
                            schema_info = {
                                'schema': schema,
                                'content_type': content_type
                            }
                            schema_displayed = True
                    
                    # 스키마 정보가 있으면 표시
                    if schema_info:
                        # 스키마 수준을 ##### 로 조정
                        markdown.append("\n##### 요청 본문 스키마\n")
                        markdown.append(format_schema_as_table(schema_info['schema']))
                    
                    # 각 컨텐츠 타입별 예시 표시
                    for content_type, content_details in request_body['content'].items():
                        schema = content_details.get('schema')
                        
                        # 예시 데이터 처리
                        example = content_details.get('example')
                        examples = content_details.get('examples')
                        
                        # 예시가 없으면 스키마에서 기본 예시 생성
                        if not example and not examples and schema:
                            example = generate_example_from_schema(schema)
                        
                        markdown.append(f"\n**Content Type**: {content_type}\n")
                        
                        if example or examples:
                            markdown.append("\n**예시:**\n")
                            
                            code_format = get_format_for_content_type(content_type)
                            
                            # 예시가 examples 딕셔너리로 제공된 경우
                            if examples:
                                for example_name, example_obj in examples.items():
                                    example_value = example_obj.get('value')
                                    if example_value:
                                        markdown.append(f"\n**{example_name}:**\n")
                                        if code_format == 'json':
                                            markdown.append(f"```{code_format}\n{json.dumps(example_value, indent=2, ensure_ascii=False)}\n```\n")
                                        elif code_format == 'xml':
                                            xml_root = "root"
                                            if schema and 'xml' in schema:
                                                xml_root = schema['xml'].get('name', xml_root)
                                            xml_example = dict_to_xml_example(example_value, schema, xml_root)
                                            markdown.append(f"```{code_format}\n{xml_example}\n```\n")
                                        elif code_format == 'http':
                                            form_example = dict_to_form(example_value)
                                            form_str = "\n".join(form_example)
                                            markdown.append(f"```{code_format}\n{form_str}\n```\n")
                                        else:
                                            markdown.append(f"```{code_format}\n{yaml.dump(example_value, sort_keys=False, allow_unicode=True)}\n```\n")
                            
                            # 단일 예시가 제공된 경우
                            elif example:
                                if code_format == 'json':
                                    markdown.append(f"```{code_format}\n{json.dumps(example, indent=2, ensure_ascii=False)}\n```\n")
                                elif code_format == 'xml':
                                    xml_root = "root"
                                    if schema and 'xml' in schema:
                                        xml_root = schema['xml'].get('name', xml_root)
                                    xml_example = dict_to_xml_example(example, schema, xml_root)
                                    markdown.append(f"```{code_format}\n{xml_example}\n```\n")
                                elif code_format == 'http':
                                    form_example = dict_to_form(example)
                                    form_str = "\n".join(form_example)
                                    markdown.append(f"```{code_format}\n{form_str}\n```\n")
                                else:
                                    markdown.append(f"```{code_format}\n{yaml.dump(example, sort_keys=False, allow_unicode=True)}\n```\n")

            markdown.append("\n")

            # 응답 정보 - 수준을 #### 로 조정
            markdown.append("#### 응답\n")
            for status, response in details.get('responses', {}).items():
                markdown.append(f"\n**상태 코드**: `{status}`\n")
                markdown.append(f"**설명**: {response.get('description', '-')}\n")
                
                if 'content' in response:
                    schema_displayed = False
                    schema_info = {}  # 스키마 정보 저장
                    
                    # 모든 content 타입에서 스키마 정보 수집
                    for content_type, content_details in response['content'].items():
                        schema = content_details.get('schema')
                        if schema and not schema_displayed:
                            schema_info = {
                                'schema': schema,
                                'content_type': content_type
                            }
                            schema_displayed = True
                    
                    # 스키마 정보가 있으면 표시
                    if schema_info:
                        # 스키마 수준을 ##### 로 조정
                        markdown.append("\n##### 응답 스키마\n")
                        markdown.append(format_schema_as_table(schema_info['schema']))
                    
                    # 각 컨텐츠 타입별 예시 표시
                    for content_type, content_details in response['content'].items():
                        schema = content_details.get('schema')
                        
                        # 예시 데이터 처리
                        example = content_details.get('example')
                        examples = content_details.get('examples')
                        
                        # 예시가 없으면 스키마에서 기본 예시 생성
                        if not example and not examples and schema:
                            example = generate_example_from_schema(schema)
                        
                        markdown.append(f"\n**Content Type**: {content_type}\n")
                        
                        if example or examples:
                            markdown.append("\n**예시:**\n")
                            
                            code_format = get_format_for_content_type(content_type)
                            
                            # 예시가 examples 딕셔너리로 제공된 경우
                            if examples:
                                for example_name, example_obj in examples.items():
                                    example_value = example_obj.get('value')
                                    if example_value:
                                        markdown.append(f"\n**{example_name}:**\n")
                                        if code_format == 'json':
                                            markdown.append(f"```{code_format}\n{json.dumps(example_value, indent=2, ensure_ascii=False)}\n```\n")
                                        elif code_format == 'xml':
                                            xml_root = "root"
                                            if schema and 'xml' in schema:
                                                xml_root = schema['xml'].get('name', xml_root)
                                            xml_example = dict_to_xml_example(example_value, schema, xml_root)
                                            markdown.append(f"```{code_format}\n{xml_example}\n```\n")
                                        elif code_format == 'http':
                                            form_example = dict_to_form(example_value)
                                            form_str = "\n".join(form_example)
                                            markdown.append(f"```{code_format}\n{form_str}\n```\n")
                                        else:
                                            markdown.append(f"```{code_format}\n{yaml.dump(example_value, sort_keys=False, allow_unicode=True)}\n```\n")
                            
                            # 단일 예시가 제공된 경우
                            elif example:
                                if code_format == 'json':
                                    markdown.append(f"```{code_format}\n{json.dumps(example, indent=2, ensure_ascii=False)}\n```\n")
                                elif code_format == 'xml':
                                    xml_root = "root"
                                    if schema and 'xml' in schema:
                                        xml_root = schema['xml'].get('name', xml_root)
                                    xml_example = dict_to_xml_example(example, schema, xml_root)
                                    markdown.append(f"```{code_format}\n{xml_example}\n```\n")
                                elif code_format == 'http':
                                    form_example = dict_to_form(example)
                                    form_str = "\n".join(form_example)
                                    markdown.append(f"```{code_format}\n{form_str}\n```\n")
                                else:
                                    markdown.append(f"```{code_format}\n{yaml.dump(example, sort_keys=False, allow_unicode=True)}\n```\n")
            markdown.append("\n")
            markdown.append("---\n")  # 경로 구분선 추가

    # 스키마 정의 섹션 추가
    if 'components' in spec and 'schemas' in spec['components']:
        markdown.append("## 스키마\n")
        markdown.append("API에서 사용되는 데이터 모델 스키마입니다.\n\n")
        
        for schema_name, schema in spec['components']['schemas'].items():
            markdown.append(f"### {schema_name}\n")
            
            # 스키마 설명 추가
            if 'description' in schema:
                markdown.append(f"{schema['description']}\n\n")
            
            # 스키마 테이블 생성
            markdown.append(format_schema_as_table(schema))
            markdown.append("\n")
            
            # 예시 생성
            example = None
            if 'example' in schema:
                example = schema['example']
            else:
                example = generate_example_from_schema(schema)
            
            if example:
                markdown.append("\n**예시:**\n")
                
                # JSON 예시
                markdown.append("```json\n")
                markdown.append(json.dumps(example, indent=2, ensure_ascii=False))
                markdown.append("\n```\n")
                
                # 스키마에 XML 정보가 있으면 XML 예시도 추가
                if 'xml' in schema:
                    xml_root = schema['xml'].get('name', schema_name)
                    xml_example = dict_to_xml_example(example, schema, xml_root)
                    markdown.append("\n**XML 예시:**\n")
                    markdown.append("```xml\n")
                    markdown.append(xml_example)
                    markdown.append("\n```\n")
            
            markdown.append("\n")

    return "\n".join(markdown)

def save_markdown(file_path, content):
    """생성된 마크다운 내용을 파일로 저장합니다."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    """메인 함수: OpenAPI 스펙을 로드하고 마크다운 문서를 생성합니다."""
    # 설정
    input_file = 'swagger.yaml'  # OpenAPI 스펙 파일
    output_file = 'markdown.md'  # 출력할 마크다운 파일
    
    # OpenAPI 스펙 로드
    spec = load_openapi_spec(input_file)
    
    # 마크다운 생성
    markdown_text = generate_markdown(spec)
    
    # 파일로 저장
    save_markdown(output_file, markdown_text)
    
    print(f"Markdown documentation generated: {output_file}")

if __name__ == "__main__":
    main()
