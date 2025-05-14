#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
마크다운 문서를 생성하는 모듈입니다.
"""
from openapi_to_markdown.processors.schema_processor import SchemaProcessor
from openapi_to_markdown.processors.parameter_processor import ParameterProcessor
from openapi_to_markdown.processors.request_processor import RequestProcessor
from openapi_to_markdown.processors.response_processor import ResponseProcessor
from openapi_to_markdown.utils.markdown_utils import MarkdownUtils


class MarkdownGenerator:
    """
    OpenAPI 스펙에서 마크다운 문서를 생성하는 클래스입니다.
    """
    
    def __init__(self):
        """
        MarkdownGenerator 초기화
        """
        self.schema_processor = SchemaProcessor()
        self.parameter_processor = ParameterProcessor()
        self.request_processor = RequestProcessor()
        self.response_processor = ResponseProcessor()
        self.markdown_utils = MarkdownUtils()
    
    def generate(self, spec):
        """
        OpenAPI 스펙에서 전체 마크다운 문서를 생성합니다.
        
        Args:
            spec: 변환할 OpenAPI 스펙
            
        Returns:
            str: 생성된 마크다운 문서
        """
        markdown = []
        
        # 1. 제목 및 설명
        info = spec.get('info', {})
        title = info.get('title', 'API Documentation')
        version = info.get('version', '')
        description = info.get('description', '')
        
        markdown.append(f"# {title} v{version}\n")
        
        if description:
            markdown.append(f"{description}\n")
        
        # 2. 서버 정보
        servers = spec.get('servers', [])
        if servers:
            markdown.append("## 서버\n")
            
            for server in servers:
                server_url = server.get('url', '')
                server_desc = server.get('description', '')
                
                markdown.append(f"* **{server_url}**")
                if server_desc:
                    markdown.append(f"  * {server_desc}")
            
            markdown.append("")
        
        # 3. 목차 생성
        markdown.append(self._generate_toc(spec))
        
        # 4. 엔드포인트 문서 생성
        markdown.append(self._generate_endpoints_docs(spec))
        
        # 5. 스키마 문서 생성
        markdown.append(self._generate_schemas_docs(spec))
        
        return "\n".join(markdown)
    
    def _generate_toc(self, spec):
        """
        OpenAPI 스펙에서 목차를 생성합니다.
        
        Args:
            spec: OpenAPI 스펙
            
        Returns:
            str: 생성된 목차 마크다운
        """
        toc = ["## 목차\n"]
        
        # 태그 정보 수집
        tags_dict = {}
        tags_list = spec.get('tags', [])
        
        for tag in tags_list:
            tag_name = tag.get('name')
            tag_description = tag.get('description', '')
            if tag_name:
                tags_dict[tag_name] = tag_description
        
        # 태그별 엔드포인트 그룹화
        paths = spec.get('paths', {})
        endpoints_by_tag = {}
        
        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method in ['get', 'post', 'put', 'delete', 'patch', 'head', 'options']:
                    op_tags = operation.get('tags', ['기타'])
                    op_summary = operation.get('summary', path)
                    
                    for tag in op_tags:
                        if tag not in endpoints_by_tag:
                            endpoints_by_tag[tag] = []
                            
                        endpoint_info = {
                            'path': path,
                            'method': method.upper(),
                            'summary': op_summary
                        }
                        
                        endpoints_by_tag[tag].append(endpoint_info)
        
        # 태그별 목차 생성
        for tag, endpoints in endpoints_by_tag.items():
            tag_description = tags_dict.get(tag, '')
            if tag_description:
                toc.append(f"### {tag} {tag_description}\n")
            else:
                toc.append(f"### {tag}\n")
            
            for endpoint in endpoints:
                path = endpoint['path']
                method = endpoint['method']
                summary = endpoint['summary']
                
                # 앵커 생성
                anchor = self.markdown_utils.create_anchor(f"{method.lower()}-{path}")
                
                toc.append(f"- [{method} {path}](#{anchor}) - {summary}")
            
            toc.append("")
        
        return "\n".join(toc)
    
    def _generate_endpoints_docs(self, spec):
        """
        OpenAPI 스펙에서 엔드포인트 문서를 생성합니다.
        
        Args:
            spec: OpenAPI 스펙
            
        Returns:
            str: 생성된 엔드포인트 마크다운
        """
        markdown = []
        
        # 태그 정보 수집
        tags_dict = {}
        tags_list = spec.get('tags', [])
        
        for tag in tags_list:
            tag_name = tag.get('name')
            tag_description = tag.get('description', '')
            if tag_name:
                tags_dict[tag_name] = tag_description
        
        # 태그별 엔드포인트 그룹화
        paths = spec.get('paths', {})
        endpoints_by_tag = {}
        
        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method in ['get', 'post', 'put', 'delete', 'patch', 'head', 'options']:
                    op_tags = operation.get('tags', ['기타'])
                    
                    for tag in op_tags:
                        if tag not in endpoints_by_tag:
                            endpoints_by_tag[tag] = []
                            
                        endpoint_info = {
                            'path': path,
                            'method': method,
                            'operation': operation
                        }
                        
                        endpoints_by_tag[tag].append(endpoint_info)
        
        # 태그별 엔드포인트 문서 생성
        for tag, endpoints in endpoints_by_tag.items():
            markdown.append(f"## {tag}\n")
            
            tag_description = tags_dict.get(tag, '')
            if tag_description:
                markdown.append(f"{tag_description}\n")
            
            for endpoint in endpoints:
                path = endpoint['path']
                method = endpoint['method']
                operation = endpoint['operation']
                
                # 앵커 생성
                anchor = self.markdown_utils.create_anchor(f"{method}-{path}")
                markdown.append(f"<h3 id='{anchor}'></h3>\n")
                
                # 1. 엔드포인트 헤더
                markdown.append(f"### {method.upper()} {path}\n")
                
                # 2. 요약 및 설명
                summary = operation.get('summary', '')
                if summary:
                    markdown.append(f"**{summary}**\n")
                    
                description = operation.get('description', '')
                if description:
                    markdown.append(f"{description}\n")
                else:
                    markdown.append("No description provided\n")
                
                # 3. 파라미터
                parameters = operation.get('parameters', [])
                if parameters:
                    markdown.append("#### 요청 파라미터\n")
                    markdown.extend(self.parameter_processor.process_parameters(parameters, spec))
                
                # 4. 요청 본문
                request_body = operation.get('requestBody')
                if request_body:
                    markdown.append("#### 요청 본문\n")
                    markdown.extend(self.request_processor.process_request_body(request_body, spec))
                else:
                    markdown.append("#### 요청\n\n")
                
                # 5. 응답
                responses = operation.get('responses', {})
                if responses:
                    markdown.append("#### 응답\n")
                    
                    for status, response in responses.items():
                        markdown.extend(self.response_processor.process_response(status, response, spec))
                
                markdown.append("\n---\n")
        
        return "\n".join(markdown)
    
    def _generate_schemas_docs(self, spec):
        """
        OpenAPI 스펙에서 스키마 문서를 생성합니다.
        
        Args:
            spec: OpenAPI 스펙
            
        Returns:
            str: 생성된 스키마 마크다운
        """
        markdown = []
        
        components = spec.get('components', {})
        schemas = components.get('schemas', {})
        
        if schemas:
            markdown.append("## 스키마\n")
            markdown.append("API에서 사용되는 데이터 모델 스키마입니다.\n")
            
            for schema_name, schema in schemas.items():
                markdown.append(f"\n### {schema_name}\n")
                
                # $ref 처리
                if '$ref' in schema and spec:
                    from openapi_to_markdown.core.reference_resolver import ReferenceResolver
                    resolver = ReferenceResolver()
                    resolved_schema = resolver.resolve_ref(schema['$ref'], spec)
                    if resolved_schema:
                        schema = resolved_schema
                
                markdown.append(self.schema_processor.format_schema_as_table(schema, spec=spec))
                
                # 스키마의 예시 추가
                if 'example' in schema or 'examples' in schema:
                    markdown.append("\n\n**예시:**\n")
                    
                    if 'example' in schema:
                        from openapi_to_markdown.generators.json_example import JsonExampleGenerator
                        generator = JsonExampleGenerator()
                        example = schema['example']
                        markdown.append(generator.format_example(example, schema=schema, spec=spec))
                    elif 'examples' in schema:
                        for example_name, example_value in schema['examples'].items():
                            actual_value = None
                            if isinstance(example_value, dict) and 'value' in example_value:
                                actual_value = example_value['value']
                            else:
                                actual_value = example_value
                                
                            if example_name:
                                markdown.append(f"\n**{example_name}:**\n")
                                
                            from openapi_to_markdown.generators.json_example import JsonExampleGenerator
                            generator = JsonExampleGenerator()
                            markdown.append(generator.format_example(actual_value, schema=schema, spec=spec))
                else:                    # 예시가 없는 경우 생성
                    from openapi_to_markdown.generators.json_example import JsonExampleGenerator
                    generator = JsonExampleGenerator()
                    
                    # $ref가 있을 수 있으므로 schema를 generate_example에 전달
                    example = generator.generate_example(schema, spec)
                    markdown.append("\n\n**예시:**\n")
                    markdown.append(generator.format_example(example, schema=schema, spec=spec))
        
        return "\n".join(markdown)
