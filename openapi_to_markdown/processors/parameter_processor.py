#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
API 엔드포인트의 파라미터를 처리하는 모듈입니다.
"""
from openapi_to_markdown.processors.schema_processor import SchemaProcessor
from openapi_to_markdown.core.reference_resolver import ReferenceResolver
from openapi_to_markdown.utils.markdown_utils import MarkdownUtils


class ParameterProcessor:
    """
    API 엔드포인트의 파라미터를 처리하는 클래스입니다.
    """
    
    def __init__(self):
        """
        ParameterProcessor 초기화
        """
        self.schema_processor = SchemaProcessor()
        self.reference_resolver = ReferenceResolver()
        self.markdown_utils = MarkdownUtils()
    
    def process_parameters(self, parameters, spec):
        """
        API 엔드포인트의 파라미터를 처리합니다.
        
        Args:
            parameters: 처리할 파라미터 목록
            spec: 전체 OpenAPI 스펙
            
        Returns:
            list: 생성된 마크다운 문자열 목록
        """
        markdown = []
        
        if not parameters:
            return markdown
            
        # 파라미터를 위치별로 그룹화
        path_params = []
        query_params = []
        header_params = []
        cookie_params = []
        
        for param in parameters:
            # $ref 처리
            if '$ref' in param and spec:
                param = self.reference_resolver.resolve_ref(param['$ref'], spec) or param
                
            param_in = param.get('in', '')
            
            if param_in == 'path':
                path_params.append(param)
            elif param_in == 'query':
                query_params.append(param)
            elif param_in == 'header':
                header_params.append(param)
            elif param_in == 'cookie':
                cookie_params.append(param)
        
        # 각 파라미터 유형 처리
        if path_params:
            markdown.extend(self._process_param_group(path_params, "경로 파라미터"))
        
        if query_params:
            markdown.extend(self._process_param_group(query_params, "쿼리 파라미터"))
        
        if header_params:
            markdown.extend(self._process_param_group(header_params, "헤더 파라미터", is_header=True))
        
        if cookie_params:
            markdown.extend(self._process_param_group(cookie_params, "쿠키 파라미터"))
        
        return markdown

    def _process_param_group(self, params, group_name, is_header=False):
        """
        특정 그룹의 파라미터를 처리하여 마크다운 테이블을 생성합니다.
        
        Args:
            params: 처리할 파라미터 목록
            group_name: 파라미터 그룹 이름
            is_header: 헤더 파라미터인지 여부 (열 순서가 다름)
            
        Returns:
            list: 생성된 마크다운 문자열 목록
        """
        markdown = []
        
        markdown.append(f"\n##### {group_name}\n")
        markdown.append("| 이름 | 타입 | 설명 | 필수 |")
        markdown.append("|------|------|------|:----:|")
        
        for param in params:
            name = param.get('name', '')
            required = "O" if param.get('required', False) else "X"
            description = self.markdown_utils.escape_markdown(param.get('description', '-'))
            
            schema = param.get('schema', {})
            param_type = schema.get('type', '-')
            
            # 타입 표시 형식 개선
            if isinstance(param_type, list):
                param_type = " \\| ".join([t.capitalize() for t in param_type])
            else:
                param_type = param_type.capitalize()
            
            # enum 값 처리
            description = self._process_enum_values(schema, description)
            
            # 배열 아이템의 enum 값 처리
            description = self._process_array_param(schema, description)
            
            # explode 처리
            description = self._process_explode_param(param, description)

            # 헤더 파라미터는 열 순서가 다름
            if is_header:
                markdown.append(f"| `{name}` | {param_type} | {description} | {required} |")
            else:
                markdown.append(f"| `{name}` | {param_type} | {description} | {required} |")

        markdown.append("")
        return markdown
    
    def _process_enum_values(self, schema, description='-'):
        """
        스키마의 enum 값을 처리하여 설명에 개행과 함께 추가합니다.
        
        Args:
            schema: enum 값을 포함하는 스키마
            description: 기존 설명
            
        Returns:
            str: enum 값이 추가된 설명
        """
        if 'enum' in schema:
            enum_values = schema['enum']
            enum_str = ', '.join([f"`{val}`" for val in enum_values])
            if description != '-':
                description += f"<br>(Enum: {enum_str})"
            else:
                description = f"Enum: {enum_str}"
        return description
    
    def _process_explode_param(self, param, description='-'):
        """
        explode 파라미터를 처리하여 설명에 개행과 함께 추가합니다.
        
        Args:
            param: explode 설정을 포함하는 파라미터
            description: 기존 설명
            
        Returns:
            str: explode 정보가 추가된 설명
        """
        if 'explode' in param:
            explode_value = param['explode']
            explode_str = f"explode: {str(explode_value).lower()}"
            if description != '-':
                description += f"<br>({explode_str})"
            else:
                description = explode_str
        return description
    
    def _process_array_param(self, schema, description='-'):
        """
        배열 파라미터의 항목에 있는 enum 값을 처리하여 개행과 함께 추가합니다.
        
        Args:
            schema: 배열 스키마
            description: 기존 설명
            
        Returns:
            str: 배열 항목 정보가 추가된 설명
        """
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
