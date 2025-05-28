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
          # oneOf 스키마 처리
        if 'oneOf' in schema:
            return self._format_oneof_schema(schema, title, spec)
        
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
            elif 'oneOf' in prop:
                # oneOf 타입 처리 - object 타입으로 표시하고 가능한 타입들을 설명에 추가
                oneof_type = "object"
                discriminator = prop.get('discriminator')
                additional_desc = ""
                
                if discriminator:
                    mapping = discriminator.get('mapping', {})
                    if mapping:
                        type_options = list(mapping.keys())
                        additional_desc = f"가능한 타입: {', '.join(type_options)}"
                    
                    property_name = discriminator.get('propertyName', 'type')
                    if additional_desc:
                        additional_desc += f" (discriminator: {property_name})"
                    else:
                        additional_desc = f"discriminator 속성: {property_name}"
                
                # 설명에 oneOf 정보 추가
                final_desc = prop_desc
                if additional_desc:
                    final_desc = f"{prop_desc} {additional_desc}".strip()
                
                flat_fields.append({
                    "name": f"`{field_name}`",
                    "type": oneof_type,
                    "required": required_mark,
                    "desc": final_desc
                })
                
                # oneOf 스키마들의 공통/대표 properties 표시
                self._add_oneof_properties(prop, field_name, flat_fields, spec)
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
    
    def _format_oneof_schema(self, schema, title=None, spec=None):
        """
        oneOf 스키마를 마크다운으로 변환합니다.
        
        Args:
            schema: oneOf를 포함하는 스키마
            title: 테이블 제목 (옵션)
            spec: 전체 OpenAPI 스펙 (참조 해결 시 필요)
            
        Returns:
            str: 생성된 마크다운
        """
        result = []
        
        if title:
            result.append(f"{title}\n")
        
        # discriminator 정보가 있는 경우
        discriminator = schema.get('discriminator')
        description = schema.get('description', '')
        
        if description:
            result.append(f"{description}\n")
        
        if discriminator:
            property_name = discriminator.get('propertyName', 'type')
            mapping = discriminator.get('mapping', {})
            
            result.append(f"**구분자**: `{property_name}` 필드 값에 따라 다음 중 하나의 스키마를 사용합니다.\n")
            
            # mapping이 있는 경우 각 타입별로 설명
            if mapping:
                result.append("**가능한 타입들:**\n")
                for discriminator_value, schema_ref in mapping.items():
                    # 스키마 참조 해결
                    if spec:
                        resolved_schema = self.reference_resolver.resolve_ref(schema_ref, spec)
                        if resolved_schema:
                            schema_name = schema_ref.split('/')[-1]
                            result.append(f"- `{discriminator_value}`: {schema_name} 스키마")
                            
                            # 각 스키마의 필드들을 간단히 표시
                            if 'properties' in resolved_schema:
                                field_names = list(resolved_schema['properties'].keys())
                                if len(field_names) > 3:
                                    field_display = ', '.join(field_names[:3]) + f" 외 {len(field_names)-3}개"
                                else:
                                    field_display = ', '.join(field_names)
                                result.append(f"  - 필드: {field_display}")
                        else:
                            result.append(f"- `{discriminator_value}`: {schema_ref}")
                    else:
                        result.append(f"- `{discriminator_value}`: {schema_ref}")
                
                result.append("")
            
            # 통합된 스키마 테이블 생성 (공통 필드 + discriminator)
            result.append("**공통 스키마 구조:**\n")
            
            # oneOf의 첫 번째 스키마를 기준으로 공통 구조 파악
            oneof_schemas = schema.get('oneOf', [])
            if oneof_schemas and spec:
                base_schema_ref = oneof_schemas[0]
                if '$ref' in base_schema_ref:
                    base_schema = self.reference_resolver.resolve_ref(base_schema_ref['$ref'], spec)
                    if base_schema and 'properties' in base_schema:
                        # discriminator 필드를 명시적으로 추가
                        enhanced_schema = base_schema.copy()
                        if 'properties' not in enhanced_schema:
                            enhanced_schema['properties'] = {}
                        
                        # discriminator 속성을 스키마에 추가
                        if property_name not in enhanced_schema['properties']:
                            enhanced_schema['properties'][property_name] = {
                                'type': 'string',
                                'description': f'객체 타입을 구분하는 필드 (가능한 값: {", ".join([f"`{v}`" for v in mapping.keys()])})'
                            }
                            if 'required' not in enhanced_schema:
                                enhanced_schema['required'] = []
                            if property_name not in enhanced_schema['required']:
                                enhanced_schema['required'].append(property_name)
                        
                        # 테이블 형태로 표시
                        table_result = self.format_schema_as_table(enhanced_schema, None, spec)
                        result.append(table_result)
                    else:
                        result.append("스키마 정보를 불러올 수 없습니다.")
        else:
            # discriminator가 없는 경우 각 스키마를 순서대로 표시
            result.append("**다음 중 하나의 스키마를 사용합니다:**\n")
            
            oneof_schemas = schema.get('oneOf', [])
            for i, schema_item in enumerate(oneof_schemas, 1):
                if '$ref' in schema_item and spec:
                    schema_name = schema_item['$ref'].split('/')[-1]
                    resolved_schema = self.reference_resolver.resolve_ref(schema_item['$ref'], spec)
                    
                    result.append(f"**옵션 {i}: {schema_name}**")
                    if resolved_schema:
                        schema_table = self.format_schema_as_table(resolved_schema, None, spec)
                        result.append(schema_table)
                        result.append("")
                else:
                    result.append(f"**옵션 {i}:**")
                    schema_table = self.format_schema_as_table(schema_item, None, spec)
                    result.append(schema_table)
                    result.append("")
        
        return "\n".join(result)
    
    def _add_oneof_properties(self, oneof_schema, field_name, flat_fields, spec):
        """
        oneOf 스키마의 내부 properties를 flat_fields에 추가합니다.
        
        Args:
            oneof_schema: oneOf를 포함하는 스키마
            field_name: 현재 필드명
            flat_fields: 결과를 담을 평면화된 필드 목록
            spec: 전체 OpenAPI 스펙
        """
        discriminator = oneof_schema.get('discriminator')
        mapping = discriminator.get('mapping', {}) if discriminator else {}
        
        if not mapping:
            return
        
        # 가장 대표적인 스키마 선택 (첫 번째 스키마)
        first_schema_ref = list(mapping.values())[0]
        
        if spec:
            resolved_schema = self.reference_resolver.resolve_ref(first_schema_ref, spec)
            if resolved_schema and 'properties' in resolved_schema:
                required_props = resolved_schema.get('required', [])
                
                # discriminator 속성 먼저 추가
                if discriminator:
                    property_name = discriminator.get('propertyName', 'type')
                    flat_fields.append({
                        "name": f"`{field_name}.{property_name}`",
                        "type": "string",
                        "required": "true",
                        "desc": f"객체 타입 구분자 (가능한 값: {', '.join([f'`{k}`' for k in mapping.keys()])})"
                    })
                
                # 나머지 properties 추가
                for prop_name, prop_schema in resolved_schema['properties'].items():
                    # discriminator 속성은 이미 추가했으므로 스킵
                    if discriminator and prop_name == discriminator.get('propertyName', 'type'):
                        continue
                    
                    # $ref 처리
                    if '$ref' in prop_schema and spec:
                        resolved_prop = self.reference_resolver.resolve_ref(prop_schema['$ref'], spec)
                        if resolved_prop:
                            prop_schema = {**resolved_prop, **{k: v for k, v in prop_schema.items() if k != '$ref'}}
                    
                    prop_type = prop_schema.get('type', '-')
                    prop_desc = self.markdown_utils.escape_markdown(prop_schema.get('description', '-'))
                    is_required = prop_name in required_props
                    
                    # enum 값 처리
                    if 'enum' in prop_schema:
                        prop_desc = self._process_enum_values(prop_schema, prop_desc)
                    
                    flat_fields.append({
                        "name": f"`{field_name}.{prop_name}`",
                        "type": prop_type,
                        "required": "true" if is_required else "false",
                        "desc": prop_desc
                    })
                    
                    # 중첩된 object나 array 처리
                    if prop_type == 'object' and 'properties' in prop_schema:
                        sub_required_props = prop_schema.get('required', [])
                        self._collect_fields(
                            prop_schema['properties'], flat_fields, sub_required_props, spec,
                            f"{field_name}.{prop_name}.", False, is_required, sub_required_props
                        )
                    elif prop_type == 'array' and 'items' in prop_schema:
                        items = prop_schema['items']
                        if isinstance(items, dict) and ('properties' in items or '$ref' in items):
                            # 배열 항목 처리는 기존 로직 재사용
                            self._process_array_items(items, f"{field_name}.{prop_name}", flat_fields, spec, prop_desc)

    def _process_array_items(self, items_schema, field_name, flat_fields, spec, parent_desc):
        """
        배열 항목의 스키마를 처리합니다.
        
        Args:
            items_schema: 배열 항목 스키마
            field_name: 필드명
            flat_fields: 결과를 담을 평면화된 필드 목록
            spec: 전체 OpenAPI 스펙
            parent_desc: 부모 설명
        """
        if '$ref' in items_schema and spec:
            ref = items_schema['$ref']
            ref_parts = ref.split('/')
            ref_name = ref_parts[-1] if ref_parts else "object"
            ref_schema = self.reference_resolver.resolve_ref(ref, spec)
            
            if ref_schema and 'properties' in ref_schema:
                ref_required_props = ref_schema.get('required', [])
                for sub_name, sub_prop in ref_schema['properties'].items():
                    if '$ref' in sub_prop and spec:
                        sub_resolved = self.reference_resolver.resolve_ref(sub_prop['$ref'], spec)
                        if sub_resolved:
                            sub_prop = {**sub_resolved, **{k: v for k, v in sub_prop.items() if k != '$ref'}}
                    
                    sub_type = sub_prop.get('type', '-')
                    sub_desc = self.markdown_utils.escape_markdown(sub_prop.get('description', '-'))
                    sub_required = sub_name in ref_required_props
                    
                    if 'enum' in sub_prop:
                        sub_desc = self._process_enum_values(sub_prop, sub_desc)
                    
                    flat_fields.append({
                        "name": f"`{field_name}[].{sub_name}`",
                        "type": sub_type,
                        "required": "true" if sub_required else "false",
                        "desc": sub_desc
                    })
        elif 'properties' in items_schema:
            items_required_props = items_schema.get('required', [])
            for sub_name, sub_prop in items_schema['properties'].items():
                sub_type = sub_prop.get('type', '-')
                sub_desc = self.markdown_utils.escape_markdown(sub_prop.get('description', '-'))
                sub_required = sub_name in items_required_props
                
                if 'enum' in sub_prop:
                    sub_desc = self._process_enum_values(sub_prop, sub_desc)
                
                flat_fields.append({
                    "name": f"`{field_name}[].{sub_name}`",
                    "type": sub_type,
                    "required": "true" if sub_required else "false",
                    "desc": sub_desc
                })
