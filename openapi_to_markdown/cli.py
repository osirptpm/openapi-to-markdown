#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenAPI to Markdown 변환기의 명령줄 인터페이스를 제공합니다.
"""
import argparse
import os
import sys

from openapi_to_markdown.core.spec_loader import OpenApiSpecLoader
from openapi_to_markdown.core.reference_resolver import ReferenceResolver
from openapi_to_markdown.generators.markdown_generator import MarkdownGenerator
from openapi_to_markdown.utils.file_utils import FileUtils


def process_file(input_file, output_file=None):
    """
    단일 OpenAPI 스펙 파일을 처리합니다.
    
    Args:
        input_file: 입력 파일 경로
        output_file: 출력 파일 경로 (옵션)
    """
    # 기본 출력 파일 설정
    if not output_file:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}.md"
    
    try:
        # 스펙 로드
        spec_loader = OpenApiSpecLoader()
        spec = spec_loader.load_spec(input_file)
        
        # 스펙 유효성 검증
        if not spec_loader.validate_spec(spec):
            print(f"오류: {input_file}은 유효한 OpenAPI 3.0 스펙 파일이 아닙니다.")
            return
        
        # 참조 해결
        resolver = ReferenceResolver()
        resolved_spec = resolver.resolve_all_refs(spec)
        
        # 마크다운 생성
        markdown_generator = MarkdownGenerator()
        markdown = markdown_generator.generate(resolved_spec)
        
        # 파일 저장
        file_utils = FileUtils()
        file_utils.save_markdown(markdown, output_file)
        
        print(f"{input_file} -> {output_file} 변환 완료")
        
    except Exception as e:
        print(f"오류: {input_file} 처리 중 문제가 발생했습니다: {str(e)}")


def process_directory(input_dir, output_dir=None):
    """
    OpenAPI 스펙 파일이 포함된 디렉토리를 처리합니다.
    
    Args:
        input_dir: 입력 디렉토리 경로
        output_dir: 출력 디렉토리 경로 (옵션)
    """
    if not os.path.isdir(input_dir):
        print(f"오류: {input_dir}은 유효한 디렉토리가 아닙니다.")
        return
    
    # 출력 디렉토리가 지정되었으면 생성
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # YAML 파일 찾기
    file_utils = FileUtils()
    yaml_files = file_utils.find_yaml_files(input_dir)
    
    if not yaml_files:
        print(f"{input_dir} 디렉토리에서 YAML 파일을 찾을 수 없습니다.")
        return
    
    # 각 파일 처리
    for yaml_file in yaml_files:
        # 출력 파일 경로 결정
        output_file = file_utils.get_output_path(yaml_file, output_dir=output_dir)
        process_file(yaml_file, output_file)


def main():
    """
    프로그램의 진입점 함수입니다.
    """
    parser = argparse.ArgumentParser(
        description="OpenAPI 3.0 스펙 문서를 마크다운 형식으로 변환합니다."
    )
    
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "-f", "--file", 
        help="변환할 OpenAPI 스펙 파일 경로 (YAML 형식)"
    )
    input_group.add_argument(
        "-d", "--directory", 
        help="OpenAPI 스펙 파일이 포함된 디렉토리 경로"
    )
    
    parser.add_argument(
        "-o", "--output", 
        help="생성된 마크다운 파일 경로 (--file 옵션과 함께 사용)"
    )
    parser.add_argument(
        "-od", "--output-directory", 
        help="생성된 마크다운 파일을 저장할 디렉토리 경로 (--directory 옵션과 함께 사용)"
    )
    
    args = parser.parse_args()
    
    if args.file:
        if args.output_directory:
            print("오류: --output-directory 옵션은 --directory 옵션과 함께 사용해야 합니다.")
            sys.exit(1)
            
        process_file(args.file, args.output)
    
    elif args.directory:
        if args.output:
            print("오류: --output 옵션은 --file 옵션과 함께 사용해야 합니다.")
            sys.exit(1)
            
        process_directory(args.directory, args.output_directory)


if __name__ == "__main__":
    main()
