#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenAPI 스펙 파일을 로드하는 모듈입니다.
"""
import yaml


class OpenApiSpecLoader:
    """
    OpenAPI 스펙 파일을 로드하고 관리하는 클래스입니다.
    """
    
    @staticmethod
    def load_spec(file_path):
        """
        OpenAPI 명세를 YAML 파일에서 로드합니다.
        
        Args:
            file_path: YAML 파일의 경로
            
        Returns:
            dict: 로드된 OpenAPI 스펙
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
            
    def validate_spec(self, spec):
        """
        OpenAPI 스펙의 유효성을 검증합니다.
        
        Args:
            spec: 검증할 OpenAPI 스펙
            
        Returns:
            bool: 유효성 여부
        """
        # 기본적인 유효성 검사
        required_fields = ['openapi', 'info', 'paths']
        for field in required_fields:
            if field not in spec:
                return False
        
        # OpenAPI 버전 검사
        if not spec['openapi'].startswith('3.'):
            return False
            
        return True
