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
            schema: 예시를 생성할 스키마
            spec: 전체 OpenAPI 스펙 (참조 해결용)
            
        Returns:
            dict/list/scalar: 생성된 예시 데이터
        """
        if not schema:
            return {}
            
        # $ref가 있는 경우 해결
        if '$ref' in schema:
            ref = schema['$ref']
            if spec is not None:
                resolver = ReferenceResolver()
                schema = resolver.resolve_ref(ref, spec)
            else:
                return {"$ref": ref}  # 참조를 해결할 수 없는 경우
        
        # 타입이 배열인 경우 (예: ['object', 'null'])
        if isinstance(schema.get('type'), list):
            # null 이외의 타입 중 첫 번째를 사용
            non_null_types = [t for t in schema['type'] if t != 'null']
            if non_null_types:
                # 임시 스키마를 생성하되, properties 등 다른 필드도 유지
                temp_schema = schema.copy()
                temp_schema['type'] = non_null_types[0]
                return self.generate_example(temp_schema, spec)
            else:
                return None
        
        # 나머지 타입들 처리...
        type_value = schema.get('type')
        
        if type_value == 'object':
            return self._generate_object_example(schema, spec)
        elif type_value == 'array':
            return self._generate_array_example(schema, spec)
        elif type_value == 'string':
            return self._generate_string_example(schema)
        elif type_value == 'integer':
            return self._generate_integer_example(schema)
        elif type_value == 'number':
            return self._generate_number_example(schema)
        elif type_value == 'boolean':
            return self._generate_boolean_example(schema)
        elif type_value == 'null':
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
        """객체 타입 예시 생성"""
        result = {}
        
        # 속성이 정의되어 있는 경우
        properties = schema.get('properties', {})
        for prop_name, prop_schema in properties.items():
            # 모든 속성에 대해 예시 생성 시도
            result[prop_name] = self.generate_example(prop_schema, spec)
        
        # 속성이 없는 경우 객체에 샘플 데이터 추가
        if not properties:
            # 빈 객체가 아닌 의미 있는 예시 데이터 제공
            result["property1"] = "value1"
            result["property2"] = "value2"
        
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
