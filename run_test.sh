#!/bin/bash
# 리팩토링된 OpenAPI to Markdown 변환기 테스트를 위한 스크립트

echo "OpenAPI to Markdown 테스트 시작"

# 현재 디렉토리 확인
CURRENT_DIR=$(pwd)
echo "현재 디렉토리: $CURRENT_DIR"

# 테스트 실행
echo "테스트 스크립트 실행 중..."
python test_converter.py

# 종료 상태 확인
if [ $? -eq 0 ]; then
    echo "테스트 성공"
    echo "생성된 파일: swagger_refactored.md"
else
    echo "테스트 실패"
fi
