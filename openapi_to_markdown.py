#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenAPI 스펙 문서를 마크다운 형식으로 변환하는 스크립트입니다.

이 스크립트는 OpenAPI 3.0 스펙 문서(YAML 형식)를 읽고,
보기 좋은 마크다운 형식의 API 문서로 변환합니다.
계층구조와 참조($ref)를 적절히 처리하며, 각 콘텐츠 타입(JSON, XML, form-data)에 맞는
예시 출력을 제공합니다.
"""
import yaml
import copy
import json
import re
import os

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
    components = spec.get('components', {})
    
    def resolve_ref(obj):
        """객체 내의 $ref를 재귀적으로 해결합니다."""
        if isinstance(obj, dict):
            if '$ref' in obj:
                ref_path = obj['$ref'].replace('#/', '').split('/')
                ref_obj = spec
                for path in ref_path:
                    ref_obj = ref_obj.get(path, {})
                
                resolved = copy.deepcopy(ref_obj)
                obj.pop('$ref')
                
                for key, value in obj.items():
                    resolved[key] = value
                    
                return resolve_ref(resolved)
            else:
                return {k: resolve_ref(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [resolve_ref(item) for item in obj]
        else:
            return obj
    
    paths = spec.get('paths', {})
    resolved_paths = resolve_ref(paths)
    
    resolved_spec = copy.deepcopy(spec)
    resolved_spec['paths'] = resolved_paths
    
    return resolved_spec

def escape_markdown(text):
    """마크다운에서 특수 문자를 이스케이프 처리합니다."""
    if not isinstance(text, str):
        return text
        
    special_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!']
    for char in special_chars:
        text = text.replace(char, '\\' + char)
    return text

def format_schema_as_table(schema, title=None):
    """스키마를 마크다운 테이블로 변환합니다."""
    if not schema or not isinstance(schema, dict):
        return "스키마 정보가 없습니다."
    
    if schema.get('type') == 'array' and 'items' in schema:
        array_schema = schema['items']
        array_title = title or "배열 아이템 스키마"
        array_info = f"**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**\n\n"
        return array_info + format_schema_as_table(array_schema, array_title)
    
    if 'properties' not in schema:
        type_info = f"**타입**: {schema.get('type', '알 수 없음')}\n"
        if 'format' in schema:
            type_info += f"\n**포맷**: {schema['format']}\n"
        if 'description' in schema:
            type_info += f"\n**설명**: {schema['description']}\n"
        return type_info

    table = []
    if title:
        table.append(f"{title}\n")
    
    table.append("| 이름 | 타입 | 필수 여부 | 설명 |")
    table.append("|------|------|:--------:|------|")
    
    flat_fields = []
    required_props = schema.get('required', [])
    
    def collect_fields(properties, prefix="", is_required=False, parent_required=False):
        for prop_name, prop in properties.items():
            if not isinstance(prop, dict):
                continue
                
            field_name = f"{prefix}{prop_name}"
            prop_type = prop.get('type', '-')
            prop_desc = escape_markdown(prop.get('description', '-'))
            field_required = prop_name in required_props or is_required
            field_required = field_required or parent_required
            required_mark = "true" if field_required else "false"
            
            if prop_type == 'array' and 'items' in prop:
                items = prop['items']
                if isinstance(items, dict):
                    item_type = items.get('type', '-')
                    if item_type == 'object' or 'properties' in items:
                        flat_fields.append({
                            "name": f"`{field_name}[]`",
                            "type": f"array&lt;object&gt;",
                            "required": required_mark,
                            "desc": prop_desc
                        })
                        if 'properties' in items:
                            for sub_name, sub_prop in items['properties'].items():
                                sub_type = sub_prop.get('type', '-')
                                sub_desc = escape_markdown(sub_prop.get('description', '-'))
                                sub_required = sub_name in items.get('required', [])
                                flat_fields.append({
                                    "name": f"`{field_name}[].{sub_name}`",
                                    "type": sub_type,
                                    "required": "true" if sub_required or field_required else "false",
                                    "desc": sub_desc
                                })
                    else:
                        flat_fields.append({
                            "name": f"`{field_name}[]`",
                            "type": f"array&lt;{item_type}&gt;",
                            "required": required_mark,
                            "desc": prop_desc
                        })
            elif prop_type == 'object' and 'properties' in prop:
                flat_fields.append({
                    "name": f"`{field_name}`",
                    "type": "object",
                    "required": required_mark,
                    "desc": prop_desc
                })
                sub_required_props = prop.get('required', [])
                for sub_name, sub_prop in prop['properties'].items():
                    sub_type = sub_prop.get('type', '-')
                    sub_desc = escape_markdown(sub_prop.get('description', '-'))
                    sub_required = sub_name in sub_required_props
                    flat_fields.append({
                        "name": f"`{field_name}.{sub_name}`",
                        "type": sub_type,
                        "required": "true" if sub_required or field_required else "false",
                        "desc": sub_desc
                    })
            else:
                flat_fields.append({
                    "name": f"`{field_name}`",
                    "type": prop_type,
                    "required": required_mark,
                    "desc": prop_desc
                })
    
    collect_fields(schema.get('properties', {}))
    
    for field in flat_fields:
        table.append(f"| {field['name']} | {field['type']} | {field['required']} | {field['desc']} |")
    
    return "\n".join(table)

def dict_to_form(d, parent_key=""):
    """Dict를 form 데이터로 변환합니다."""
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

def dict_to_xml_example(data, schema, spec, root_name="root", indent=""):
    """Python 사전을 XML 문자열로 변환합니다."""
    xml_lines = []
    
    if isinstance(data, list):
        array_items_schema = None
        array_wrapped = False
        wrapper_name = root_name
        
        if schema and schema.get('type') == 'array':
            array_items_schema = schema.get('items', {})
            
            if 'xml' in schema:
                if 'wrapped' in schema['xml'] and schema['xml']['wrapped']:
                    array_wrapped = True
                if 'name' in schema['xml']:
                    wrapper_name = schema['xml']['name']
        
        if array_wrapped:
            xml_lines.append(f"{indent}<{wrapper_name}>")
            item_indent = indent + "  "
        else:
            item_indent = indent
        
        item_name = "item"
        if array_items_schema:
            if 'xml' in array_items_schema and 'name' in array_items_schema['xml']:
                item_name = array_items_schema['xml']['name']
            
        for item in data:
            if isinstance(item, dict):
                xml_lines.append(dict_to_xml_example(item, array_items_schema, spec, item_name, item_indent))
            else:
                xml_lines.append(f"{item_indent}<{item_name}>{item}</{item_name}>")
        
        if array_wrapped:
            xml_lines.append(f"{indent}</{wrapper_name}>")
            
        return "\n".join(xml_lines)
    
    root_xml_name = root_name
    if schema and 'xml' in schema and 'name' in schema['xml']:
        root_xml_name = schema['xml']['name']
    
    if isinstance(data, dict):
        xml_lines.append(f"{indent}<{root_xml_name}>")
        next_indent = indent + "  "
        
        for key, value in data.items():
            if value is None:
                continue
            
            prop_schema = None
            if schema and 'properties' in schema:
                prop_schema = schema['properties'].get(key, {})
            
            xml_name = key
            if prop_schema:
                if 'xml' in prop_schema and 'name' in prop_schema['xml']:
                    xml_name = prop_schema['xml']['name']
                elif '$ref' in prop_schema:
                    ref_schema = resolve_schema_ref(prop_schema['$ref'], spec)
                    if ref_schema and 'xml' in ref_schema and 'name' in ref_schema['xml']:
                        xml_name = ref_schema['xml']['name']
            
            if isinstance(value, dict):
                if prop_schema and '$ref' in prop_schema:
                    ref_schema = resolve_schema_ref(prop_schema['$ref'], spec)
                    if ref_schema:
                        xml_lines.append(dict_to_xml_example(value, ref_schema, spec, xml_name, next_indent))
                    else:
                        xml_lines.append(dict_to_xml_example(value, {}, spec, xml_name, next_indent))
                else:
                    xml_lines.append(dict_to_xml_example(value, prop_schema, spec, xml_name, next_indent))
            elif isinstance(value, list):
                if prop_schema and 'type' in prop_schema and prop_schema['type'] == 'array':
                    wrapped = False
                    if 'xml' in prop_schema and 'wrapped' in prop_schema['xml'] and prop_schema['xml']['wrapped']:
                        wrapped = True
                        xml_lines.append(f"{next_indent}<{xml_name}>")
                        wrap_indent = next_indent + "  "
                    else:
                        wrap_indent = next_indent
                    
                    items_schema = prop_schema.get('items', {})
                    item_xml_name = 'item'
                    
                    if 'xml' in items_schema and 'name' in items_schema['xml']:
                        item_xml_name = items_schema['xml']['name']
                    elif '$ref' in items_schema:
                        ref_items_schema = resolve_schema_ref(items_schema['$ref'], spec)
                        if ref_items_schema and 'xml' in ref_items_schema and 'name' in ref_items_schema['xml']:
                            item_xml_name = ref_items_schema['xml']['name']
                    
                    if not value:
                        if wrapped:
                            xml_lines.append(f"{next_indent}</{xml_name}>")
                    else:
                        for item in value:
                            if isinstance(item, dict):
                                if '$ref' in items_schema:
                                    ref_items_schema = resolve_schema_ref(items_schema['$ref'], spec)
                                    if ref_items_schema:
                                        xml_lines.append(dict_to_xml_example(item, ref_items_schema, spec, item_xml_name, wrap_indent))
                                    else:
                                        xml_lines.append(dict_to_xml_example(item, {}, spec, item_xml_name, wrap_indent))
                                else:
                                    xml_lines.append(dict_to_xml_example(item, items_schema, spec, item_xml_name, wrap_indent))
                            else:
                                xml_lines.append(f"{wrap_indent}<{item_xml_name}>{item}</{item_xml_name}>")
                        
                        if wrapped:
                            xml_lines.append(f"{next_indent}</{xml_name}>")
                else:
                    if value:
                        for item in value:
                            if isinstance(item, dict):
                                xml_lines.append(dict_to_xml_example(item, {}, spec, xml_name, next_indent))
                            else:
                                xml_lines.append(f"{next_indent}<{xml_name}>{item}</{xml_name}>")
            else:
                xml_lines.append(f"{next_indent}<{xml_name}>{value}</{xml_name}>")
        
        xml_lines.append(f"{indent}</{root_xml_name}>")
    else:
        xml_lines.append(f"{indent}<{root_xml_name}>{data}</{root_xml_name}>")
    
    return "\n".join(xml_lines)

def generate_example_from_schema(schema, spec):
    """스키마에서 예시 데이터를 생성합니다."""
    if not schema or not isinstance(schema, dict):
        return {}
        
    result = {}
    if 'type' in schema:
        if schema['type'] == 'object' and 'properties' in schema:
            for prop_name, prop in schema['properties'].items():
                if 'example' in prop:
                    result[prop_name] = prop['example']
                elif 'type' in prop:
                    if prop['type'] == 'string':
                        result[prop_name] = f"example_{prop_name}"
                    elif prop['type'] == 'integer':
                        result[prop_name] = 0
                    elif prop['type'] == 'number':
                        result[prop_name] = 0.0
                    elif prop['type'] == 'boolean':
                        result[prop_name] = False
                    elif prop['type'] == 'array':
                        items_schema = prop.get('items', {})
                        if items_schema:
                            if '$ref' in items_schema:
                                ref_schema = resolve_schema_ref(items_schema['$ref'], spec)
                                if ref_schema:
                                    result[prop_name] = [generate_example_from_schema(ref_schema, spec)]
                                else:
                                    if items_schema.get('type') == 'string':
                                        result[prop_name] = [f"example_{prop_name}_{i}" for i in range(1, 3)]
                                    else:
                                        result[prop_name] = []
                            else:
                                if items_schema.get('type') == 'string':
                                    result[prop_name] = [f"example_{prop_name}_{i}" for i in range(1, 3)]
                                elif items_schema.get('type') == 'integer':
                                    result[prop_name] = [i for i in range(1, 3)]
                                elif items_schema.get('type') == 'object':
                                    result[prop_name] = [generate_example_from_schema(items_schema, spec)]
                                else:
                                    result[prop_name] = [generate_example_from_schema(items_schema, spec)]
                        else:
                            result[prop_name] = []
                    elif prop['type'] == 'object':
                        result[prop_name] = generate_example_from_schema(prop, spec)
        elif schema['type'] == 'array' and 'items' in schema:
            items_schema = schema.get('items', {})
            if '$ref' in items_schema:
                ref_schema = resolve_schema_ref(items_schema['$ref'], spec)
                if ref_schema:
                    return [generate_example_from_schema(ref_schema, spec)]
            
            if items_schema.get('type') == 'string':
                return [f"example_item_{i}" for i in range(1, 3)]
            elif items_schema.get('type') == 'integer':
                return [i for i in range(1, 3)]
            
            return [generate_example_from_schema(items_schema, spec)]
            
    return result

def get_format_for_content_type(content_type):
    """Content-Type에 따른 코드 블록 형식을 반환합니다."""
    content_type_format = {
        'application/json': 'json',
        'application/xml': 'xml',
        'text/plain': 'text',
        'text/html': 'html',
        'application/x-www-form-urlencoded': 'http'
    }
    for ct_prefix, fmt in content_type_format.items():
        if content_type.startswith(ct_prefix):
            return fmt
    return 'yaml'

def format_example(example, schema, content_type, spec=None):
    """컨텐츠 타입에 따라 예시 데이터를 적절히 포맷팅합니다."""
    code_format = get_format_for_content_type(content_type)
    
    if code_format == 'json':
        return f"```{code_format}\n{json.dumps(example, indent=2, ensure_ascii=False)}\n```"
    elif code_format == 'xml':
        xml_root = "root"
        if schema and 'xml' in schema:
            xml_root = schema['xml'].get('name', xml_root)
        xml_example = dict_to_xml_example(example, schema, spec, xml_root)
        return f"```{code_format}\n{xml_example}\n```"
    elif code_format == 'http':
        form_example = dict_to_form(example)
        form_str = "\n".join(form_example)
        return f"```{code_format}\n{form_str}\n```"
    else:
        return f"```{code_format}\n{yaml.dump(example, sort_keys=False, allow_unicode=True)}\n```"

def process_content_examples(content_details, schema, content_type, spec=None):
    """컨텐츠 세부 정보에서 예시 데이터를 처리합니다."""
    result = []
    
    example = content_details.get('example')
    examples = content_details.get('examples')
    
    if not example and not examples and schema:
        example = generate_example_from_schema(schema, spec)
    
    if examples:
        for example_name, example_obj in examples.items():
            example_value = example_obj.get('value')
            if example_value:
                result.append(f"\n**{example_name}:**\n")
                result.append(format_example(example_value, schema, content_type, spec))
    elif example:
        result.append(format_example(example, schema, content_type, spec))
    
    return "\n".join(result)

def process_enum_values(schema, description='-'):
    """스키마의 enum 값을 처리하여 설명에 개행과 함께 추가합니다."""
    if 'enum' in schema:
        enum_values = schema['enum']
        enum_str = ', '.join([f"`{val}`" for val in enum_values])
        if description != '-':
            description += f"<br>(Enum: {enum_str})"
        else:
            description = f"Enum: {enum_str}"
    return description

def process_explode_param(param, description='-'):
    """explode 파라미터를 처리하여 설명에 개행과 함께 추가합니다."""
    if 'explode' in param:
        explode_value = param['explode']
        explode_str = f"explode: {str(explode_value).lower()}"
        if description != '-':
            description += f"<br>({explode_str})"
        else:
            description = explode_str
    return description

def process_array_param(schema, description='-'):
    """배열 파라미터의 항목에 있는 enum 값을 처리하여 개행과 함께 추가합니다."""
    if schema.get('type') == 'array' and 'items' in schema:
        items = schema['items']
        if 'enum' in items:
            enum_values = items['enum']
            enum_str = ', '.join([f"`{val}`" for val in enum_values])
            if description != '-':
                description += f"<br>(Array items: {enum_str})"
            else:
                description = f"Array items: {enum_str}"
    return description

def process_parameters(parameters, markdown, spec):
    """API 엔드포인트의 파라미터를 처리합니다."""
    if not parameters or not isinstance(parameters, list):
        return
        
    markdown.append("\n**파라미터:**\n")
    
    params_by_location = {}
    for param in parameters:
        location = param.get('in', 'unknown')
        if location not in params_by_location:
            params_by_location[location] = []
        params_by_location[location].append(param)
    
    for location, params in params_by_location.items():
        markdown.append(f"\n**{location} 파라미터:**\n")
        markdown.append("| 이름 | 타입 | 필수 여부 | 설명 |")
        markdown.append("|------|------|:--------:|------|")
        
        for param in params:
            name = param.get('name', 'unknown')
            required = "true" if param.get('required', False) else "false"
            description = escape_markdown(param.get('description', '-'))
            
            description = process_explode_param(param, description)
            
            if 'schema' in param:
                schema = param['schema']
                param_type = schema.get('type', '-')
                
                description = process_enum_values(schema, description)
                
                if param_type == 'array' and 'items' in schema:
                    items = schema['items']
                    item_type = items.get('type', '-')
                    param_type = f"array&lt;{item_type}&gt;"
                    
                    description = process_array_param(schema, description)
            else:
                param_type = param.get('type', '-')
            
            markdown.append(f"| `{name}` | {param_type} | {required} | {description} |")
    
    markdown.append("\n")

def process_request_body(request_body, markdown, spec):
    """요청 본문을 처리합니다."""
    if not request_body:
        return

    markdown.append("\n**요청 본문:**\n")
    request_description = request_body.get('description', '')
    if request_description:
        markdown.append(f"{request_description}\n")

    if 'content' in request_body:
        schema_displayed = False
        schema_info = {}
        
        for content_type, content_details in request_body['content'].items():
            schema = content_details.get('schema')
            if schema and not schema_displayed:
                schema_info = {
                    'schema': schema,
                    'content_type': content_type
                }
                schema_displayed = True
          
        if schema_info:
            markdown.append("\n##### 요청 본문 스키마\n")
            
            schema = schema_info['schema']
            if schema.get('type') == 'array':
                markdown.append("**요청 형식**: 배열\n\n")
                
            markdown.append(format_schema_as_table(schema_info['schema']))
        
        for content_type, content_details in request_body['content'].items():
            markdown.append(f"\n**Content Type**: {content_type}\n")
            markdown.append(process_content_examples(content_details, content_details.get('schema'), content_type, spec))

def process_response(status, response, markdown, spec):
    """응답을 처리합니다."""
    markdown.append(f"\n**상태 코드**: `{status}`\n")
    markdown.append(f"**설명**: {response.get('description', '-')}\n")
    
    if 'content' in response:
        schema_displayed = False
        schema_info = {}
        
        for content_type, content_details in response['content'].items():
            schema = content_details.get('schema')
            if schema and not schema_displayed:
                schema_info = {
                    'schema': schema,
                    'content_type': content_type
                }
                schema_displayed = True
          
        if schema_info:
            markdown.append("\n##### 응답 스키마\n")
            
            schema = schema_info['schema']
            if schema.get('type') == 'array':
                markdown.append("**응답 형식**: 배열\n\n")
                
            markdown.append(format_schema_as_table(schema_info['schema']))
        
        for content_type, content_details in response['content'].items():
            markdown.append(f"\n**Content Type**: {content_type}\n")
            markdown.append(process_content_examples(content_details, content_details.get('schema'), content_type, spec))

def process_schema_example(schema_name, schema, markdown, spec):
    """스키마에 대한 예시를 생성하여 처리합니다."""
    example = None
    if 'example' in schema:
        example = schema['example']
    else:
        example = generate_example_from_schema(schema, spec)
    
    if example:
        markdown.append("\n**예시:**\n")
        
        markdown.append("```json\n")
        markdown.append(json.dumps(example, indent=2, ensure_ascii=False))
        markdown.append("\n```\n")
        
        if 'xml' in schema:
            xml_root = schema['xml'].get('name', schema_name)
            xml_example = dict_to_xml_example(example, schema, spec, xml_root)
            markdown.append("\n**XML 예시:**\n")
            markdown.append("```xml\n")
            markdown.append(xml_example)
            markdown.append("\n```\n")

def generate_markdown(spec):
    """OpenAPI 스펙에서 마크다운 문서를 생성합니다."""
    markdown = []
    resolved_spec = convert_refs(spec)

    title = spec['info'].get('title', 'API Documentation')
    description = spec['info'].get('description', '')
    version = spec['info'].get('version', '')
    markdown.append(f"# {title} v{version}\n")
    markdown.append(f"{description}\n")

    if 'servers' in spec and spec['servers']:
        markdown.append("## 서버 정보\n")
        for server in spec['servers']:
            server_url = server.get('url', '')
            server_desc = server.get('description', '')
            markdown.append(f"- {server_url} - {server_desc}")
        markdown.append("\n")

    markdown.append("## 목차\n")
    
    tags = {tag['name']: tag.get('description', '') for tag in spec.get('tags', [])}
    endpoints_by_tag = {}
    
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
    
    for tag in sorted(endpoints_by_tag.keys()):
        tag_description = tags.get(tag, '')
        markdown.append(f"### {tag} {tag_description}\n")
        
        for endpoint in sorted(endpoints_by_tag[tag], key=lambda x: x['path']):
            markdown.append(f"- [{endpoint['method']} {endpoint['path']}](#{endpoint['anchor']}) - {endpoint['summary']}")
        
        markdown.append("\n")    # 엔드포인트 처리 함수 정의
    def process_endpoint(path, method, details, anchor, markdown):
        """각 API 엔드포인트를 처리하여 마크다운을 생성합니다."""
        method_upper = method.upper()
        summary = details.get('summary', 'No summary provided')
        description = details.get('description', 'No description provided')
        
        # 앵커와 헤더를 분리하여 생성
        markdown.append(f"<h3 id='{anchor}'></h3>\n")
        markdown.append(f"### {method_upper} {path}\n")
        markdown.append(f"**{summary}**\n")
        markdown.append(f"{description}\n")

        # 인증 정보 처리
        if 'security' in details and details['security']:
            markdown.append("\n**인증 요구사항:**\n")
            for security_req in details['security']:
                for scheme_name, scopes in security_req.items():
                    markdown.append(f"- {scheme_name}")
                    if scopes:
                        markdown.append(f"  - 접근 권한: {', '.join(scopes)}")
            markdown.append("\n")

        # 요청 정보 처리
        markdown.append("#### 요청\n")
        process_parameters(details.get('parameters'), markdown, spec)

        if 'requestBody' in details:
            process_request_body(details['requestBody'], markdown, spec)

        markdown.append("\n")

        # 응답 정보 처리
        markdown.append("#### 응답\n")
        for status, response in details.get('responses', {}).items():
            process_response(status, response, markdown, spec)
        
        markdown.append("\n")
        markdown.append("---\n")
        
    # 태그별 엔드포인트 처리
    for tag, endpoints in sorted(endpoints_by_tag.items()):
        markdown.append(f"## {tag}\n")
        
        if tag in tags:
            markdown.append(f"{tags[tag]}\n")
        
        for endpoint in sorted(endpoints, key=lambda x: x['path']):
            path = endpoint['path']
            method = endpoint['method'].lower()
            details = resolved_spec['paths'][path][method]
            anchor = endpoint['anchor']
            
            # 엔드포인트 처리 함수 호출
            process_endpoint(path, method, details, anchor, markdown)

    if 'components' in spec and 'schemas' in spec['components']:
        markdown.append("## 스키마\n")
        markdown.append("API에서 사용되는 데이터 모델 스키마입니다.\n\n")
        
        for schema_name, schema in spec['components']['schemas'].items():
            markdown.append(f"### {schema_name}\n")
            
            if 'description' in schema:
                markdown.append(f"{schema['description']}\n\n")
            
            if schema.get('type') == 'array':
                markdown.append("**타입**: 배열\n\n")
                
            markdown.append(format_schema_as_table(schema))
            markdown.append("\n")
            
            process_schema_example(schema_name, schema, markdown, spec)
            markdown.append("\n")

    return "\n".join(markdown)

def save_markdown(file_path, content):
    """생성된 마크다운 내용을 파일로 저장합니다."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    """메인 함수: OpenAPI 스펙을 로드하고 마크다운 문서를 생성합니다."""
    input_file = 'swagger.yaml'
    output_file = 'markdown.md'
    
    spec = load_openapi_spec(input_file)
    
    markdown_text = generate_markdown(spec)
    
    save_markdown(output_file, markdown_text)
    
    print(f"Markdown documentation generated: {output_file}")

if __name__ == "__main__":
    main()
