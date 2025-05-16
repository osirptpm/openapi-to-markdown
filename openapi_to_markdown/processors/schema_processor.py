#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
스키마를 처리하고 마크다운 테이블로 변환하는 모듈입니다.
"""
from openapi_to_markdown.core.reference_resolver import ReferenceResolver
from openapi_to_markdown.utils.markdown_utils import MarkdownUtils


class SchemaProcessor:
    """
    스키마를 처리하고 마크다운 테이블로 변환하는 클래스입니다.
    """
    
    def __init__(self):
        """
        SchemaProcessor 초기화
        """
        self.reference_resolver = ReferenceResolver()
        self.markdown_utils = MarkdownUtils()
    
    def format_schema_as_table(self, schema, title=None, spec=None):
        """
        스키마를 마크다운 테이블로 변환합니다.
        
        Args:
            schema: 변환할 스키마
            title: 테이블 제목 (옵션)
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            str: 생성된 마크다운 테이블
        """
        if not schema or not isinstance(schema, dict):
            return "스키마 정보가 없습니다."
            
        # $ref 처리
        if '$ref' in schema and spec:
            resolved_schema = self.reference_resolver.resolve_ref(schema['$ref'], spec)
            if resolved_schema:
                schema = resolved_schema
        
        # 배열 스키마 처리
        if schema.get('type') == 'array' and 'items' in schema:
            array_schema = schema['items']
            array_title = title or "배열 아이템 스키마"
            array_info = f"**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**\n\n"
            
            # $ref 처리
            if '$ref' in array_schema and spec:
                ref_schema = self.reference_resolver.resolve_ref(array_schema['$ref'], spec)
                if ref_schema:
                    array_schema = ref_schema
                    # 참조된 스키마 이름 추출
                    ref_path = array_schema['$ref'].split('/') if '$ref' in array_schema else []
                    ref_name = ref_path[-1] if ref_path else "Schema"
                    array_title = f"{ref_name} 스키마"
                    
            return array_info + self.format_schema_as_table(array_schema, array_title, spec)
        
        # 기본 타입 (객체가 아닌 경우) 처리
        if 'properties' not in schema:
            type_info = f"**타입**: {schema.get('type', '알 수 없음')}\n"
            if 'format' in schema:
                type_info += f"\n**포맷**: {schema['format']}\n"
            if 'description' in schema:
                type_info += f"\n**설명**: {schema['description']}\n"
            if 'enum' in schema:
                enum_values = schema['enum']
                enum_str = ', '.join([f"`{val}`" for val in enum_values])
                type_info += f"\n**가능한 값**: {enum_str}\n"
            return type_info

        # 객체 타입 처리
        table = []
        if title:
            table.append(f"{title}\n")
        
        table.append("| 이름 | 타입 | 필수 여부 | 설명 |")
        table.append("|------|------|:--------:|------|")
        
        flat_fields = []
        required_props = schema.get('required', [])
        
        self._collect_fields(schema.get('properties', {}), flat_fields, required_props, spec)
        
        for field in flat_fields:
            table.append(f"| {field['name']} | {field['type']} | {field['required']} | {field['desc']} |")
        
        return "\n".join(table)
    
    def _collect_fields(self, properties, flat_fields, required_props, spec, prefix="", is_required=False, parent_required=False, parent_required_fields=None):
        """
        스키마 속성을 재귀적으로 처리하여 평면화된 필드 목록을 생성합니다.
        
        Args:
            properties: 처리할 속성
            flat_fields: 결과를 담을 평면화된 필드 목록
            required_props: 필수 속성 목록
            spec: 전체 OpenAPI 스펙
            prefix: 속성 이름 접두사
            is_required: 속성 필수 여부
            parent_required: 부모 객체의 필수 여부
            parent_required_fields: 부모 객체의 필수 필드 목록
        """
        # 상위 레벨 required_props와 부모로부터 전달된 required_fields 통합
        effective_required = required_props or []
        if parent_required_fields:
            effective_required = list(set(effective_required + parent_required_fields))
        
        for prop_name, prop in properties.items():
            if not isinstance(prop, dict):
                continue
                
            # $ref 처리
            ref_required_props = []
            if '$ref' in prop and spec:
                resolved_prop = self.reference_resolver.resolve_ref(prop['$ref'], spec)
                if resolved_prop:
                    # 참조된 스키마의 필수 필드 목록 가져오기
                    if 'required' in resolved_prop and isinstance(resolved_prop['required'], list):
                        ref_required_props = resolved_prop['required']
                    
                    # 원본 속성 보존하면서 참조된 속성 병합
                    prop = {**resolved_prop, **{k: v for k, v in prop.items() if k != '$ref'}}
                
            field_name = f"{prefix}{prop_name}"
            prop_type = prop.get('type', '-')
            prop_desc = self.markdown_utils.escape_markdown(prop.get('description', '-'))
            
            # 필수 필드 여부 확인 - 명확하고 통합된 로직
            field_required = (prop_name in effective_required or 
                             is_required or parent_required)
                
            required_mark = "true" if field_required else "false"
            
            # enum 값 처리
            if 'enum' in prop:
                prop_desc = self._process_enum_values(prop, prop_desc)
            
            # 타입 처리
            if isinstance(prop_type, list):
                # 복합 타입에서 'null'을 제외한 주요 타입 추출
                non_null_types = [t for t in prop_type if t != 'null']
                if non_null_types:
                    main_type = non_null_types[0]  # 주요 타입 선택
                    prop_type_display = str(prop_type)  # 표시용 타입은 원래 형태 유지
                    
                    # 주요 타입이 object이고 properties가 있는 경우 내부 속성 처리
                    if main_type == 'object' and 'properties' in prop:
                        flat_fields.append({
                            "name": f"`{field_name}`",
                            "type": prop_type_display,
                            "required": required_mark,
                            "desc": prop_desc
                        })
                        
                        # 객체 내부 속성의 required 필드 처리
                        sub_required_props = prop.get('required', [])
                        self._collect_fields(
                            prop['properties'], flat_fields, sub_required_props, spec,
                            f"{field_name}.", False, field_required, sub_required_props
                        )
                        continue
                else:
                    # 모든 타입이 'null'인 경우 null로 처리
                    prop_type = 'null'
            
            if prop_type == 'array' and 'items' in prop:
                items = prop['items']
                if isinstance(items, dict):
                    # $ref가 있는 경우 처리
                    if '$ref' in items and spec:
                        ref = items['$ref']
                        ref_parts = ref.split('/')
                        ref_name = ref_parts[-1] if ref_parts else "object"
                        ref_schema = self.reference_resolver.resolve_ref(ref, spec)
                        
                        flat_fields.append({
                            "name": f"`{field_name}[]`",
                            "type": f"array&lt;{ref_name}&gt;",
                            "required": required_mark,
                            "desc": prop_desc
                        })
                        
                        # ref_schema가 있고 properties가 있으면 하위 항목도 표시
                        if ref_schema and 'properties' in ref_schema:
                            ref_required_props = ref_schema.get('required', [])
                            for sub_name, sub_prop in ref_schema['properties'].items():
                                # $ref 처리 - 배열 항목 내부의 스키마도 참조가 있을 수 있음
                                if '$ref' in sub_prop and spec:
                                    sub_resolved = self.reference_resolver.resolve_ref(sub_prop['$ref'], spec)
                                    if sub_resolved:
                                        sub_prop = {**sub_resolved, **{k: v for k, v in sub_prop.items() if k != '$ref'}}
                                
                                sub_type = sub_prop.get('type', '-')
                                sub_desc = self.markdown_utils.escape_markdown(sub_prop.get('description', '-'))
                                sub_required = sub_name in ref_required_props
                                
                                # enum 값 처리
                                if 'enum' in sub_prop:
                                    sub_desc = self._process_enum_values(sub_prop, sub_desc)
                                
                                flat_fields.append({
                                    "name": f"`{field_name}[].{sub_name}`",
                                    "type": sub_type,
                                    "required": "true" if sub_required else "false",
                                    "desc": sub_desc
                                })
                    # 일반 객체 타입인 경우
                    elif items.get('type') == 'object' or 'properties' in items:
                        flat_fields.append({
                            "name": f"`{field_name}[]`",
                            "type": f"array&lt;object&gt;",
                            "required": required_mark,
                            "desc": prop_desc
                        })
                        if 'properties' in items:
                            items_required_props = items.get('required', [])
                            for sub_name, sub_prop in items['properties'].items():
                                # $ref 처리 - 배열 내부의 스키마도 참조가 있을 수 있음
                                if '$ref' in sub_prop and spec:
                                    sub_resolved = self.reference_resolver.resolve_ref(sub_prop['$ref'], spec)
                                    if sub_resolved:
                                        sub_prop = {**sub_resolved, **{k: v for k, v in sub_prop.items() if k != '$ref'}}
                                
                                sub_type = sub_prop.get('type', '-')
                                sub_desc = self.markdown_utils.escape_markdown(sub_prop.get('description', '-'))
                                sub_required = sub_name in items_required_props
                                
                                # enum 값 처리
                                if 'enum' in sub_prop:
                                    sub_desc = self._process_enum_values(sub_prop, sub_desc)
                                
                                flat_fields.append({
                                    "name": f"`{field_name}[].{sub_name}`",
                                    "type": sub_type,
                                    "required": "true" if sub_required else "false",
                                    "desc": sub_desc
                                })
                    # 기타 기본 타입인 경우
                    else:
                        item_type = items.get('type', '-')
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
                # 객체 내부 속성의 required 필드 처리
                sub_required_props = prop.get('required', [])
                
                # 참조된 스키마의 필수 필드 목록도 통합
                if ref_required_props:
                    sub_required_props = list(set(sub_required_props + ref_required_props))
                
                self._collect_fields(
                    prop['properties'], flat_fields, sub_required_props, spec,
                    f"{field_name}.", False, field_required, sub_required_props
                )
            else:
                flat_fields.append({
                    "name": f"`{field_name}`",
                    "type": prop_type,
                    "required": required_mark,
                    "desc": prop_desc
                })
    
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
