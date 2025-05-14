#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
XML 형식의 예시 데이터를 생성하는 모듈입니다.
"""
from openapi_to_markdown.generators.example_generator import ExampleGenerator
from openapi_to_markdown.generators.json_example import JsonExampleGenerator


class XmlExampleGenerator(ExampleGenerator):
    """
    XML 형식의 예시 데이터를 생성하는 클래스입니다.
    """
    
    def generate_example(self, schema, spec=None):
        """
        스키마에서 XML 예시 데이터를 생성합니다. 내부적으로 JSON 예시 생성기를 사용합니다.
        
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
        XML 형식으로 예시 데이터를 포맷팅합니다.
        
        Args:
            example: 포맷팅할 예시 데이터
            schema: XML 태그 정보를 포함하는 스키마
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            str: 포맷팅된 XML 예시 데이터 문자열
        """
        xml_root = "root"
        if schema and 'xml' in schema:
            xml_root = schema['xml'].get('name', xml_root)
            
        xml_example = self._dict_to_xml(example, schema, spec, xml_root)
        return f"```xml\n{xml_example}\n```"
    
    def _dict_to_xml(self, data, schema=None, spec=None, root_name="root", indent=""):
        """
        Python 사전을 XML 문자열로 변환합니다.
        
        Args:
            data: 변환할 데이터
            schema: XML 태그 정보를 포함하는 스키마
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            root_name: 최상위 요소의 이름
            indent: 현재 들여쓰기 수준
            
        Returns:
            str: 생성된 XML 문자열
        """
        xml_parts = []
        
        if isinstance(data, dict):
            xml_parts.append(f"{indent}<{root_name}>")
            
            for key, value in data.items():
                # 속성에 해당하는 XML 이름 결정
                element_name = key
                if schema and 'properties' in schema and key in schema['properties']:
                    prop_schema = schema['properties'][key]
                    if 'xml' in prop_schema and 'name' in prop_schema['xml']:
                        element_name = prop_schema['xml']['name']
                
                # 해당 속성의 스키마 가져오기
                prop_schema = None
                if schema and 'properties' in schema and key in schema['properties']:
                    prop_schema = schema['properties'][key]
                
                # 재귀적으로 XML 생성
                xml_parts.append(self._dict_to_xml(value, prop_schema, spec, element_name, indent + "  "))
                
            xml_parts.append(f"{indent}</{root_name}>")
            
        elif isinstance(data, list):
            # 배열인 경우 한 번 감싸고, 개별 항목은 item 태그로 처리
            is_wrapped = False
            wrapper_name = root_name
            item_name = "item"
            
            # 스키마에서 배열 래핑 설정 확인
            if schema and 'xml' in schema:
                is_wrapped = schema['xml'].get('wrapped', False)
                wrapper_name = schema['xml'].get('name', root_name)
            
            # 배열 항목의 이름 결정
            if schema and 'items' in schema:
                items_schema = schema['items']
                if 'xml' in items_schema and 'name' in items_schema['xml']:
                    item_name = items_schema['xml']['name']
            
            # 래핑 여부에 따라 처리
            if is_wrapped:
                xml_parts.append(f"{indent}<{wrapper_name}>")
                next_indent = indent + "  "
            else:
                next_indent = indent
            
            # 각 항목 처리
            for item in data:
                xml_parts.append(self._dict_to_xml(item, schema.get('items') if schema else None, spec, item_name, next_indent))
            
            if is_wrapped:
                xml_parts.append(f"{indent}</{wrapper_name}>")
                
        else:
            # 기본 타입인 경우
            xml_parts.append(f"{indent}<{root_name}>{self._escape_xml(str(data))}</{root_name}>")
        
        return "\n".join(xml_parts)
    
    def _escape_xml(self, text):
        """XML 특수 문자를 이스케이프 처리합니다."""
        return (text.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&apos;"))
