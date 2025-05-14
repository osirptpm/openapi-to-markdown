# OpenAPI to Markdown Converter (리팩토링 버전)

OpenAPI/Swagger 스펙 문서를 마크다운 형식으로 변환하는 파이썬 라이브러리입니다.

이 프로젝트는 기존의 단일 파일 구조에서 객체 지향 디자인으로 리팩토링된 버전입니다.

## 기능

- OpenAPI 3.0 스펙 문서(YAML 형식)를 마크다운으로 변환
- 계층 구조와 참조(`$ref`) 적절히 처리
- 요청/응답 예시 자동 생성 (JSON, XML, form-data 등의 형식 지원)
- 단일 파일 및 디렉토리 내 모든 YAML 파일 일괄 처리 지원
- 출력 파일 위치 사용자 지정 가능

## 설치 및 요구사항

이 라이브러리를 실행하기 위해서는 Python 3.6 이상과 다음 패키지가 필요합니다:

```bash
pip install -r requirements.txt
```

또는 직접 설치:

```bash
pip install pyyaml
```

## 사용법

### 직접 실행

```bash
python openapi_to_markdown.py -f path/to/openapi.yaml
```

### 패키지로 설치 후 실행

```bash
pip install .
openapi-to-markdown -f path/to/openapi.yaml
```

### API로 사용

```python
from openapi_to_markdown.core.spec_loader import OpenApiSpecLoader
from openapi_to_markdown.core.reference_resolver import ReferenceResolver
from openapi_to_markdown.generators.markdown_generator import MarkdownGenerator
from openapi_to_markdown.utils.file_utils import FileUtils

# 스펙 로드
spec_loader = OpenApiSpecLoader()
spec = spec_loader.load_spec("path/to/openapi.yaml")

# 참조 해결
resolver = ReferenceResolver()
resolved_spec = resolver.resolve_all_refs(spec)

# 마크다운 생성
markdown_generator = MarkdownGenerator()
markdown = markdown_generator.generate(resolved_spec)

# 파일로 저장
file_utils = FileUtils()
file_utils.save_markdown(markdown, "output.md")
```

## 프로젝트 구조

```
openapi_to_markdown/
│
├── __init__.py           # 패키지 초기화
├── cli.py                # 명령줄 인터페이스
│
├── core/
│   ├── __init__.py
│   ├── spec_loader.py    # OpenAPI 스펙 로딩
│   └── reference_resolver.py  # $ref 참조 해결
│
├── generators/
│   ├── __init__.py
│   ├── markdown_generator.py   # 마크다운 생성
│   ├── example_generator.py    # 예시 데이터 생성 (인터페이스)
│   ├── json_example.py         # JSON 예시 생성
│   ├── xml_example.py          # XML 예시 생성
│   └── form_example.py         # Form 예시 생성
│
├── processors/
│   ├── __init__.py
│   ├── schema_processor.py     # 스키마 처리
│   ├── parameter_processor.py  # 파라미터 처리
│   ├── request_processor.py    # 요청 처리
│   └── response_processor.py   # 응답 처리
│
└── utils/
    ├── __init__.py
    ├── markdown_utils.py       # 마크다운 관련 유틸리티
    └── file_utils.py           # 파일 처리 유틸리티
```

## 테스트 방법

리팩토링된 코드를 테스트하려면 다음 단계를 따르세요:

1. 테스트 스크립트 실행:

```bash
# 프로젝트 루트 디렉토리로 이동
cd sources/openapi-to-markdown-refactored

# 테스트 스크립트 실행
python test_converter.py
```

2. 또는 CLI 실행:

```bash
# 프로젝트 루트 디렉토리로 이동
cd sources/openapi-to-markdown-refactored

# 직접 CLI 실행
python -m openapi_to_markdown.cli -f swagger.yaml -o swagger_cli.md
```

## 적용된 디자인 패턴

- **전략 패턴(Strategy Pattern)**: 컨텐츠 타입(JSON, XML, form-data)에 따른 예시 생성 전략
- **팩토리 패턴(Factory Pattern)**: `ExampleGeneratorFactory`를 통한 예시 생성기 생성
- **단일 책임 원칙(SRP)**: 각 클래스가 명확한 하나의 책임만 갖도록 설계

## 라이선스

MIT License
