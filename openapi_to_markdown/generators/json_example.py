#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JSON 형식의 예시 데이터를 생성하는 모듈입니다.
"""
import json
from openapi_to_markdown.generators.example_generator import ExampleGenerator
from openapi_to_markdown.core.reference_resolver import ReferenceResolver


class JsonExampleGenerator(ExampleGenerator):
    """
    JSON 형식의 예시 데이터를 생성하는 클래스입니다.
    """
    def generate_example(self, schema, spec=None):
        """
        스키마에서 JSON 예시 데이터를 생성합니다.
        
        Args:
            schema: 예시 데이터를 생성할 스키마
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            object: 생성된 JSON 예시 데이터
        """
        if not schema:
            return {}
        
        # $ref 처리
        if '$ref' in schema and spec:
            resolver = ReferenceResolver()
            resolved_schema = resolver.resolve_ref(schema['$ref'], spec)
            if resolved_schema:
                schema = resolved_schema
            
        # 스키마 자체에 example이 있는 경우
        if 'example' in schema:
            return schema['example']
            
        # 스키마 타입에 따라 예시 생성
        schema_type = schema.get('type')
        
        if schema_type == 'object':
            return self._generate_object_example(schema, spec)
        elif schema_type == 'array':
            return self._generate_array_example(schema, spec)
        elif schema_type == 'string':
            return self._generate_string_example(schema)
        elif schema_type == 'integer':
            return self._generate_integer_example(schema)
        elif schema_type == 'number':
            return self._generate_number_example(schema)
        elif schema_type == 'boolean':
            return self._generate_boolean_example(schema)
        elif schema_type == 'null':
            return None
        else:
            return {}
            
    def format_example(self, example, schema=None, spec=None):
        """
        JSON 예시 데이터를 포맷팅합니다.
        
        Args:
            example: 포맷팅할 JSON 예시 데이터
            schema: 관련 스키마 (필요한 경우)
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            str: 포맷팅된 JSON 예시 데이터 문자열
        """
        return f"```json\n{json.dumps(example, indent=2, ensure_ascii=False)}\n```"
            
    def _generate_object_example(self, schema, spec):
        """객체 타입의 예시를 생성합니다."""
        result = {}
        
        # $ref 처리
        if '$ref' in schema and spec:
            resolver = ReferenceResolver()
            ref_schema = resolver.resolve_ref(schema['$ref'], spec)
            if ref_schema:
                # 참조된 스키마의 속성을 사용하여 객체 생성
                ref_result = {}
                # 참조된 스키마에 properties가 있는 경우
                ref_properties = ref_schema.get('properties', {})
                for prop_name, prop_schema in ref_properties.items():
                    ref_result[prop_name] = self.generate_example(prop_schema, spec)
                return ref_result
                
        # properties가 있는 경우
        properties = schema.get('properties', {})
        for prop_name, prop_schema in properties.items():
            result[prop_name] = self.generate_example(prop_schema, spec)
            
        return result
        
    def _generate_array_example(self, schema, spec):
        """배열 타입의 예시를 생성합니다."""
        # 항목이 정의되지 않은 경우
        if 'items' not in schema:
            return []
            
        items_schema = schema['items']
        item_example = self.generate_example(items_schema, spec)
        
        # 예시로 1개의 항목만 생성
        return [item_example]
        
    def _generate_string_example(self, schema):
        """문자열 타입의 예시를 생성합니다."""
        # enum 값이 있는 경우 첫 번째 값 사용
        if 'enum' in schema and schema['enum']:
            return schema['enum'][0]
            
        # format에 따른 예시
        string_format = schema.get('format', '')
        
        if string_format == 'date':
            return "2023-01-01"
        elif string_format == 'date-time':
            return "2023-01-01T00:00:00Z"
        elif string_format == 'email':
            return "user@example.com"
        elif string_format == 'uri':
            return "https://example.com"
        elif string_format == 'uuid':
            return "123e4567-e89b-12d3-a456-426614174000"
        else:
            # 속성 이름에 따른 예시 생성
            return "example_value"
        
    def _generate_integer_example(self, schema):
        """정수 타입의 예시를 생성합니다."""
        # enum 값이 있는 경우 첫 번째 값 사용
        if 'enum' in schema and schema['enum']:
            return schema['enum'][0]
            
        # 최소값/최대값 범위 내에서 생성
        minimum = schema.get('minimum', 0)
        maximum = schema.get('maximum', 100)
        
        # 적절한 예시 값 반환
        if minimum <= 0 <= maximum:
            return 0
        else:
            return minimum
        
    def _generate_number_example(self, schema):
        """숫자 타입의 예시를 생성합니다."""
        # enum 값이 있는 경우 첫 번째 값 사용
        if 'enum' in schema and schema['enum']:
            return schema['enum'][0]
            
        # 최소값/최대값 범위 내에서 생성
        minimum = schema.get('minimum', 0.0)
        maximum = schema.get('maximum', 100.0)
        
        # 적절한 예시 값 반환
        if minimum <= 0.0 <= maximum:
            return 0.0
        else:
            return float(minimum)
        
    def _generate_boolean_example(self, schema):
        """불리언 타입의 예시를 생성합니다."""
        # 기본값으로 false 반환
        return False
