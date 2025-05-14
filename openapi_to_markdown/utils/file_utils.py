#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
파일 처리 관련 유틸리티 함수를 제공합니다.
"""
import os
import glob


class FileUtils:
    """
    파일 처리 관련 유틸리티 클래스입니다.
    """
    
    @staticmethod
    def save_markdown(content, file_path):
        """
        마크다운 콘텐츠를 파일로 저장합니다.
        
        Args:
            content: 저장할 마크다운 콘텐츠
            file_path: 저장할 파일 경로
        """
        # 디렉토리가 없으면 생성
        os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    
    @staticmethod
    def find_yaml_files(directory):
        """
        디렉토리에서 모든 YAML 파일을 찾습니다.
        
        Args:
            directory: 검색할 디렉토리 경로
            
        Returns:
            list: 발견된 YAML 파일 경로 목록
        """
        yaml_files = []
        
        # .yaml 확장자 파일 찾기
        yaml_files.extend(glob.glob(os.path.join(directory, '**', '*.yaml'), recursive=True))
        
        # .yml 확장자 파일 찾기
        yaml_files.extend(glob.glob(os.path.join(directory, '**', '*.yml'), recursive=True))
        
        return yaml_files
    
    @staticmethod
    def get_output_path(input_path, output_path=None, output_dir=None):
        """
        입력 파일 경로를 기반으로 출력 파일 경로를 결정합니다.
        
        Args:
            input_path: 입력 파일 경로
            output_path: 출력 파일 경로 (지정된 경우)
            output_dir: 출력 디렉토리 경로 (지정된 경우)
            
        Returns:
            str: 출력 파일 경로
        """
        if output_path:
            return output_path
            
        # 입력 파일의 확장자를 .md로 변경
        filename = os.path.basename(input_path)
        basename = os.path.splitext(filename)[0]
        output_filename = f"{basename}.md"
        
        if output_dir:
            return os.path.join(output_dir, output_filename)
        else:
            # 같은 디렉토리에 저장
            return os.path.join(os.path.dirname(input_path), output_filename)
