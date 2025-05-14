#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenAPI 스펙 내의 $ref 참조를 해결하는 모듈입니다.
"""
import copy


class ReferenceResolver:
    """
    OpenAPI 스펙 내의 $ref 참조를 해결하는 클래스입니다.
    """
    
    def resolve_ref(self, ref, spec):
        """
        $ref 문자열을 통해 실제 스키마 객체를 찾습니다.
        
        Args:
            ref: 참조 문자열 (예: '#/components/schemas/User')
            spec: OpenAPI 스펙
            
        Returns:
            dict: 참조된 객체
        """
        if not ref.startswith('#/'):
            return None
            
        ref_path = ref.replace('#/', '').split('/')
        ref_obj = spec
        for path in ref_path:
            if path in ref_obj:
                ref_obj = ref_obj[path]
            else:
                return None
                
        return ref_obj
    
    def resolve_all_refs(self, spec):
        """
        전체 스펙에서 모든 $ref 참조를 실제 객체로 변환합니다.
        
        Args:
            spec: OpenAPI 스펙
            
        Returns:
            dict: 모든 참조가 해결된 OpenAPI 스펙
        """
        def resolve_ref_recursive(obj):
            """객체 내의 $ref를 재귀적으로 해결합니다."""
            if isinstance(obj, dict):
                if '$ref' in obj:
                    ref_path = obj['$ref'].replace('#/', '').split('/')
                    ref_obj = spec
                    for path in ref_path:
                        ref_obj = ref_obj.get(path, {})
                    
                    resolved = copy.deepcopy(ref_obj)
                    obj.pop('$ref')
                    
                    for key, value in obj.items():
                        resolved[key] = value
                        
                    return resolve_ref_recursive(resolved)
                else:
                    return {k: resolve_ref_recursive(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [resolve_ref_recursive(item) for item in obj]
            else:
                return obj
        
        # paths 객체에 대해 참조 해결
        paths = spec.get('paths', {})
        resolved_paths = resolve_ref_recursive(paths)
        
        resolved_spec = copy.deepcopy(spec)
        resolved_spec['paths'] = resolved_paths
        
        return resolved_spec
