#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
마크다운 형식 변환 및 처리를 위한 유틸리티 함수를 제공합니다.
"""


class MarkdownUtils:
    """
    마크다운 형식 변환 및 처리를 위한 유틸리티 클래스입니다.
    """
    
    @staticmethod
    def escape_markdown(text):
        """
        마크다운에서 특수 문자를 이스케이프 처리합니다.
        
        Args:
            text: 이스케이프 처리할 텍스트
            
        Returns:
            str: 이스케이프 처리된 텍스트
        """
        if not text or not isinstance(text, str):
            return text
            
        # 마크다운에서 이스케이프해야 하는 특수 문자들
        escape_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!', '|']
        
        for char in escape_chars:
            text = text.replace(char, '\\' + char)
            
        return text
    
    @staticmethod
    def create_table(headers, rows):
        """
        마크다운 테이블을 생성합니다.
        
        Args:
            headers: 테이블 헤더
            rows: 테이블 데이터 행
            
        Returns:
            str: 마크다운 테이블 문자열
        """
        table = []
        
        # 헤더 행 추가
        header_row = "| " + " | ".join(headers) + " |"
        table.append(header_row)
        
        # 구분선 추가
        separator = "|"
        for _ in headers:
            separator += "------|"
        table.append(separator)
        
        # 데이터 행 추가
        for row in rows:
            row_str = "| " + " | ".join(row) + " |"
            table.append(row_str)
            
        return "\n".join(table)
    
    @staticmethod
    def create_anchor(text):
        """
        텍스트에서 마크다운 앵커를 생성합니다.
        
        Args:
            text: 앵커를 생성할 텍스트
            
        Returns:
            str: 마크다운 앵커 문자열
        """
        if not text:
            return ""
            
        # 모든 특수 문자 제거하고 공백을 하이픈으로 변경
        anchor = text.lower()
        anchor = ''.join(c if c.isalnum() or c == ' ' else '-' for c in anchor)
        anchor = anchor.replace(' ', '-')
        
        # 연속된 하이픈을 하나로 통합
        while '--' in anchor:
            anchor = anchor.replace('--', '-')
            
        return anchor
