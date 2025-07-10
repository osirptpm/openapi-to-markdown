#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
API 응답을 처리하는 모듈입니다.
"""
from openapi_to_markdown.processors.schema_processor import SchemaProcessor
from openapi_to_markdown.core.reference_resolver import ReferenceResolver
from openapi_to_markdown.generators.example_generator import ExampleGeneratorFactory
from openapi_to_markdown.utils.markdown_utils import MarkdownUtils


class ResponseProcessor:
    """
    API 응답을 처리하는 클래스입니다.
    """
    
    def __init__(self):
        """
        ResponseProcessor 초기화
        """
        self.schema_processor = SchemaProcessor()
        self.reference_resolver = ReferenceResolver()
        self.markdown_utils = MarkdownUtils()
    def process_response(self, status, response, spec, context=None):
        """
        응답을 처리합니다.
        
        Args:
            status: 응답 상태 코드
            response: 처리할 응답 객체
            spec: 전체 OpenAPI 스펙
            context: API 컨텍스트 정보 (path, method, tag 등)
            
        Returns:
            list: 생성된 마크다운 문자열 목록
        """
        markdown = []
        
        if not response:
            return markdown
        
        # $ref 처리
        if '$ref' in response and spec:
            response = self.reference_resolver.resolve_ref(response['$ref'], spec) or response
        
        # 상태 코드 및 설명
        # markdown.append(f"\n**상태 코드**: `{status}`\n")
        
        # description = response.get('description', '')
        # if description:
        #     markdown.append(f"**설명**: {description}\n")
        
        # 컨텐츠 타입별 처리
        content = response.get('content', {})
        if content:
            for content_type, content_details in content.items():
        
                # 헤더 처리
                headers = response.get('headers', {})
                if headers:
                    markdown.append("\n#### API 응답 헤더\n")
                    markdown.append("| 이름 | 타입 | 필수 |")
                    markdown.append("|------|------|------|")
                    
                    for header_name, header in headers.items():
                        # $ref 처리
                        if '$ref' in header and spec:
                            header = self.reference_resolver.resolve_ref(header['$ref'], spec) or header
                        
                        header_type = '-'
                        if 'schema' in header:
                            schema = header['schema']
                            header_type = schema.get('type', '-')
                            if 'format' in schema:
                                header_type += f" ({schema['format']})"
                        
                        header_desc = self.markdown_utils.escape_markdown(header.get('description', '-'))
                        markdown.append(f"| `{header_name}` | {content_type} | O |")
                    
                    markdown.append("")
                
                # 스키마가 있는 경우
                markdown.append("\n#### API 응답 데이터\n")
                schema = content_details.get('schema', {})
                
                # $ref 처리
                if '$ref' in schema and spec:
                    schema = self.reference_resolver.resolve_ref(schema['$ref'], spec) or schema
                
                # 배열인지 확인
                if schema.get('type') == 'array':
                    markdown.append("**응답 형식**: 배열\n\n")
                
                # 스키마를 테이블로 변환
                if schema:
                    schema_md = self.schema_processor.format_schema_as_table(schema, spec=spec)
                    markdown.append(schema_md)
                    markdown.append("\n")
                
                # Content Type 추가
                # markdown.append(f"**Content Type**: {content_type}\n")
                  # 예시 처리
                # example_md = self.process_content_examples(content_details, schema, content_type, spec, context)
                # if example_md:
                #     markdown.append(example_md)
                #     markdown.append("\n")
        
        return markdown
    def process_content_examples(self, content_details, schema, content_type, spec=None, context=None):
        """
        컨텐츠 세부 정보에서 예시 데이터를 처리합니다.
        
        Args:
            content_details: 컨텐츠 세부 정보
            schema: 관련 스키마
            content_type: 컨텐츠 타입
            spec: 전체 OpenAPI 스펙
            context: API 컨텍스트 정보
            
        Returns:
            str: 생성된 예시 마크다운 문자열
        """
        result = []
        
        # $ref 처리
        if schema and '$ref' in schema and spec:
            resolver = ReferenceResolver()
            resolved_schema = resolver.resolve_ref(schema['$ref'], spec)
            if resolved_schema:
                schema = resolved_schema
        
        # 1. 스키마 자체에 example이 있는 경우 처리
        if schema and 'example' in schema:
            generator = ExampleGeneratorFactory.create(content_type)
            return generator.format_example(schema['example'], schema, spec)
        
        # 2. 스키마 자체에 examples가 있는 경우 처리
        if schema and 'examples' in schema:
            return self.format_schema_examples(schema, content_type, spec)
        
        # 3. content 레벨에 example이 있는 경우 처리
        example = content_details.get('example')
        examples = content_details.get('examples')
        
        if examples:
            for example_name, example_obj in examples.items():
                example_value = None
                if isinstance(example_obj, dict):
                    example_value = example_obj.get('value')
                else:
                    example_value = example_obj
                    
                if example_value:
                    if example_name:
                        result.append(f"\n**예시 - {example_name}:**\n")
                    else:
                        result.append("\n**예시:**\n")
                        
                    generator = ExampleGeneratorFactory.create(content_type)
                    result.append(generator.format_example(example_value, schema, spec))
        elif example:
            result.append("\n**예시:**\n")
            generator = ExampleGeneratorFactory.create(content_type)
            result.append(generator.format_example(example, schema, spec))        # 4. 예시가 없는 경우 생성
        else:
            # 스키마가 있는 경우에만 예시 생성
            if schema:
                generator = ExampleGeneratorFactory.create(content_type)
                  # generate_example 메서드에서 참조 처리가 진행되므로 schema를 바로 전달
                example_value = generator.generate_example(schema, spec, context)
                
                result.append("\n**예시:**\n")
                result.append(generator.format_example(example_value, schema, spec))
        
        return "\n".join(result)
    
    def format_schema_examples(self, schema, content_type, spec):
        """
        스키마에 정의된 examples 속성을 처리합니다.
        
        Args:
            schema: examples 속성을 포함하는 스키마
            content_type: 컨텐츠 타입
            spec: 전체 OpenAPI 스펙
            
        Returns:
            str: 생성된 예시 마크다운 문자열
        """
        if not schema or not isinstance(schema, dict) or 'examples' not in schema:
            return ""
        
        examples_md = []
        examples_md.append("\n**예시:**\n")
        
        for example_name, example_value in schema['examples'].items():
            # examples 객체가 value 속성을 가질 경우 해당 값을 사용
            actual_value = None
            if isinstance(example_value, dict) and 'value' in example_value:
                actual_value = example_value['value']
            else:
                actual_value = example_value
                
            if example_name:
                examples_md.append(f"\n**{example_name}:**\n")
            
            generator = ExampleGeneratorFactory.create(content_type)
            examples_md.append(generator.format_example(actual_value, schema, spec))
        
        return "\n".join(examples_md)
