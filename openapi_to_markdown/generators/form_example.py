#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Form 형식의 예시 데이터를 생성하는 모듈입니다.
"""
from openapi_to_markdown.generators.example_generator import ExampleGenerator
from openapi_to_markdown.generators.json_example import JsonExampleGenerator


class FormExampleGenerator(ExampleGenerator):
    """
    Form 형식의 예시 데이터를 생성하는 클래스입니다.
    """
    
    def generate_example(self, schema, spec=None):
        """
        스키마에서 Form 예시 데이터를 생성합니다. 내부적으로 JSON 예시 생성기를 사용합니다.
        
        Args:
            schema: 예시 데이터를 생성할 스키마
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            object: 생성된 예시 데이터 (파이썬 객체 형태)
        """
        # JSON 생성기로 기본 데이터 생성
        json_generator = JsonExampleGenerator()
        return json_generator.generate_example(schema, spec)
    
    def format_example(self, example, schema=None, spec=None):
        """
        Form 형식으로 예시 데이터를 포맷팅합니다.
        
        Args:
            example: 포맷팅할 예시 데이터
            schema: 관련 스키마 (필요한 경우)
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            str: 포맷팅된 Form 예시 데이터 문자열
        """
        form_example = self._dict_to_form(example)
        form_str = "\n".join(form_example)
        return f"```http\n{form_str}\n```"
    
    def _dict_to_form(self, d, parent_key=""):
        """
        Dict를 form 데이터로 변환합니다.
        
        Args:
            d: 변환할 사전 데이터
            parent_key: 부모 키 (중첩 구조를 위해 사용)
            
        Returns:
            list: form 데이터 문자열 목록
        """
        form_str = []
        
        if isinstance(d, dict):
            for key, value in d.items():
                new_key = f"{parent_key}.{key}" if parent_key else key
                if isinstance(value, dict):
                    form_str.extend(self._dict_to_form(value, new_key))
                elif isinstance(value, list):
                    for i, item in enumerate(value):
                        list_key = f"{new_key}[{i}]"
                        if isinstance(item, dict):
                            form_str.extend(self._dict_to_form(item, list_key))
                        else:
                            form_str.append(f"{list_key}={item}")
                else:
                    form_str.append(f"{new_key}={value}")
        elif isinstance(d, list):
            for i, item in enumerate(d):
                list_key = f"{parent_key}[{i}]"
                if isinstance(item, dict):
                    form_str.extend(self._dict_to_form(item, list_key))
                else:
                    form_str.append(f"{list_key}={item}")
        else:
            form_str.append(f"{parent_key}={d}")
            
        return form_str
