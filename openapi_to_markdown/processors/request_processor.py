#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
API 요청 본문을 처리하는 모듈입니다.
"""
from openapi_to_markdown.processors.schema_processor import SchemaProcessor
from openapi_to_markdown.core.reference_resolver import ReferenceResolver
from openapi_to_markdown.generators.example_generator import ExampleGeneratorFactory
from openapi_to_markdown.utils.markdown_utils import MarkdownUtils


class RequestProcessor:
    """
    API 요청 본문을 처리하는 클래스입니다.
    """
    
    def __init__(self):
        """
        RequestProcessor 초기화
        """
        self.schema_processor = SchemaProcessor()
        self.reference_resolver = ReferenceResolver()
        self.markdown_utils = MarkdownUtils()
    
    def process_request_body(self, request_body, spec):
        """
        요청 본문을 처리합니다.
        
        Args:
            request_body: 처리할 요청 본문
            spec: 전체 OpenAPI 스펙
            
        Returns:
            list: 생성된 마크다운 문자열 목록
        """
        markdown = []
        
        if not request_body:
            return markdown
        
        # $ref 처리
        if '$ref' in request_body and spec:
            request_body = self.reference_resolver.resolve_ref(request_body['$ref'], spec) or request_body
        
        # 설명 추가
        description = request_body.get('description')
        if description:
            markdown.append(f"{description}\n")
        
        # 필수 여부 추가
        required = request_body.get('required', False)
        if required:
            markdown.append("**필수**: 예\n")
        
        # 컨텐츠 타입별 처리
        content = request_body.get('content', {})
        for content_type, content_details in content.items():
            markdown.append(f"\n**Content Type**: {content_type}\n")
            
            # 스키마 처리
            schema = content_details.get('schema', {})
            
            # $ref 처리
            if '$ref' in schema and spec:
                schema = self.reference_resolver.resolve_ref(schema['$ref'], spec) or schema
            
            # 스키마를 테이블로 변환
            if schema:
                schema_md = self.schema_processor.format_schema_as_table(schema, spec=spec)
                markdown.append(schema_md)
            
            # 예시 처리
            example_md = self.process_content_examples(content_details, schema, content_type, spec)
            if example_md:
                markdown.append(f"\n{example_md}\n")
        
        return markdown
    
    def process_content_examples(self, content_details, schema, content_type, spec=None):
        """
        컨텐츠 세부 정보에서 예시 데이터를 처리합니다.
        
        Args:
            content_details: 컨텐츠 세부 정보
            schema: 관련 스키마
            content_type: 컨텐츠 타입
            spec: 전체 OpenAPI 스펙
            
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
            result.append(generator.format_example(example, schema, spec))
        # 4. 예시가 없는 경우 생성
        else:
            # 스키마가 있는 경우에만 예시 생성
            if schema:
                generator = ExampleGeneratorFactory.create(content_type)
                example_value = generator.generate_example(schema, spec)
                
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
