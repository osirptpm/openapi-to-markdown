#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
리팩토링된 OpenAPI to Markdown 변환기의 동작 테스트 스크립트입니다.
"""
import os
import sys

# 경로 설정
# 상위 디렉토리를 모듈 검색 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# 모듈 임포트
from openapi_to_markdown.core.spec_loader import OpenApiSpecLoader
from openapi_to_markdown.core.reference_resolver import ReferenceResolver
from openapi_to_markdown.generators.markdown_generator import MarkdownGenerator
from openapi_to_markdown.utils.file_utils import FileUtils

def main():
    """
    테스트 스크립트의 진입점 함수입니다.
    """
    # 현재 디렉토리 확인
    print(f"현재 디렉토리: {os.getcwd()}")
    
    # 스펙 파일 경로
    spec_file = 'swagger.yaml'
    output_file = 'swagger.md'
    
    # 스펙 파일이 존재하는지 확인
    if not os.path.exists(spec_file):
        print(f"스펙 파일 '{spec_file}'이 존재하지 않습니다.")
        return False
    
    try:
        # 스펙 로드
        spec_loader = OpenApiSpecLoader()
        print(f"스펙 로드 시도: {spec_file}")
        spec = spec_loader.load_spec(spec_file)
        print("스펙 로드 성공")
        
        # 스펙 유효성 검증
        if not spec_loader.validate_spec(spec):
            print(f"오류: {spec_file}은 유효한 OpenAPI 3.0 스펙 파일이 아닙니다.")
            return False
        print("스펙 유효성 검증 통과")
        
        # 참조 해결
        resolver = ReferenceResolver()
        print("참조 해결 시작")
        resolved_spec = resolver.resolve_all_refs(spec)
        print("참조 해결 완료")
        
        # 마크다운 생성
        markdown_generator = MarkdownGenerator()
        print("마크다운 생성 시작")
        markdown = markdown_generator.generate(resolved_spec)
        print("마크다운 생성 완료")
        
        # 파일 저장
        file_utils = FileUtils()
        print(f"마크다운 파일 저장 시작: {output_file}")
        file_utils.save_markdown(markdown, output_file)
        print(f"마크다운 파일 저장 완료: {output_file}")
        
        print(f"변환 완료: {spec_file} -> {output_file}")
        return True
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
