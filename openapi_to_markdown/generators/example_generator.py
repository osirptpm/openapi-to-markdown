#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
스키마에서 예시 데이터를 생성하는 인터페이스를 제공합니다.
"""
from abc import ABC, abstractmethod


class ExampleGenerator(ABC):
    """
    스키마에서 예시 데이터를 생성하는 인터페이스입니다.
    """
    
    @abstractmethod
    def generate_example(self, schema, spec=None):
        """
        스키마에서 예시 데이터를 생성합니다.
        
        Args:
            schema: 예시 데이터를 생성할 스키마
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            object: 생성된 예시 데이터
        """
        pass
    
    @abstractmethod
    def format_example(self, example, schema=None, spec=None):
        """
        예시 데이터를 포맷팅합니다.
        
        Args:
            example: 포맷팅할 예시 데이터
            schema: 관련 스키마 (필요한 경우)
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            str: 포맷팅된 예시 데이터 문자열
        """
        pass


class ExampleGeneratorFactory:
    """
    컨텐츠 타입에 따라 적절한 예시 생성기를 생성하는 팩토리 클래스입니다.
    """
    
    @staticmethod
    def create(content_type):
        """
        컨텐츠 타입에 맞는 예시 생성기를 반환합니다.
        
        Args:
            content_type: 컨텐츠 타입 (예: 'application/json')
            
        Returns:
            ExampleGenerator: 해당 타입의 예시 생성기
        """
        if content_type.startswith('application/json'):
            from openapi_to_markdown.generators.json_example import JsonExampleGenerator
            return JsonExampleGenerator()
        elif content_type.startswith('application/xml'):
            from openapi_to_markdown.generators.xml_example import XmlExampleGenerator
            return XmlExampleGenerator()
        elif content_type.startswith('application/x-www-form-urlencoded'):
            from openapi_to_markdown.generators.form_example import FormExampleGenerator
            return FormExampleGenerator()
        else:
            # 기본값으로 JSON 반환
            from openapi_to_markdown.generators.json_example import JsonExampleGenerator
            return JsonExampleGenerator()
