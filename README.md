# OpenAPI to Markdown 변환기

OpenAPI/Swagger 스펙 문서를 마크다운 형식으로 변환하는 파이썬 도구입니다. 모듈화된 구조로 설계되어 확장성과 유지보수성을 향상시켰습니다.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)

## 기능

- OpenAPI 3.0 스펙 문서(YAML 형식)를 마크다운으로 변환
- 계층 구조와 참조(`$ref`) 적절히 처리
- 요청/응답 예시 자동 생성 (JSON, XML, form-data 등의 형식 지원)
- 단일 파일 및 디렉토리 내 모든 YAML 파일 일괄 처리 지원
- 출력 파일 위치 사용자 지정 가능

**참고**: 현재 버전에서는 YAML 파일만 지원하며, JSON 형식의 OpenAPI 스펙은 직접 지원하지 않습니다.

## 설치 방법

### pip를 이용한 설치

```bash
pip install openapi-to-markdown
```

### 소스 코드를 이용한 설치

```bash
git clone https://github.com/your-username/openapi-to-markdown.git
cd openapi-to-markdown/sources/openapi-to-markdown
pip install -e .
```

## 요구사항

- Python 3.6 이상
- PyYAML 5.1 이상

## 사용 방법

### 명령줄 인터페이스 (CLI)

#### 기본 사용법

단일 파일 변환:

```bash
openapi-to-markdown -f path/to/openapi.yaml
```

출력 파일을 지정하여 변환:

```bash
openapi-to-markdown -f path/to/openapi.yaml -o path/to/output.md
```

#### 디렉토리 일괄 처리

디렉토리 내 모든 YAML 파일을 변환:

```bash
openapi-to-markdown -d path/to/directory
```

출력 디렉토리를 지정하여 변환:

```bash
openapi-to-markdown -d path/to/directory -od path/to/output_directory
```

### 파이썬 스크립트에서 직접 실행

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

# 파일 저장
file_utils = FileUtils()
file_utils.save_markdown(markdown, "output.md")
```

## 명령줄 옵션

| 옵션 | 설명 |
|------|------|
| `-f`, `--file` | 변환할 OpenAPI 스펙 파일 경로 (YAML 형식) |
| `-d`, `--directory` | OpenAPI 스펙 파일이 포함된 디렉토리 경로 (하위 디렉토리의 모든 YAML 파일 처리) |
| `-o`, `--output` | 생성된 마크다운 파일 경로 (`--file` 옵션과 함께 사용) |
| `-od`, `--output-directory` | 생성된 마크다운 파일을 저장할 디렉토리 경로 (`--directory` 옵션과 함께 사용) |

### 명령줄 사용 예시

**단일 파일 변환 (기본 출력 파일):**
```bash
# input.yaml을 input.md로 변환
openapi-to-markdown -f path/to/input.yaml
```

**단일 파일 변환 (사용자 지정 출력 파일):**
```bash
# input.yaml을 custom_output.md로 변환
openapi-to-markdown -f path/to/input.yaml -o path/to/custom_output.md
```

**디렉토리 처리 (기본 출력 디렉토리):**
```bash
# docs 디렉토리 내의 모든 YAML을 원본 디렉토리에 저장
openapi-to-markdown -d path/to/docs
```

**디렉토리 처리 (사용자 지정 출력 디렉토리):**
```bash
# docs 디렉토리 내의 모든 YAML을 markdown 디렉토리에 저장
openapi-to-markdown -d path/to/docs -od path/to/markdown
```

## 출력 형식

생성된 마크다운 문서는 다음 구조로 구성됩니다:

1. API 제목 및 설명
2. 서버 정보
3. 목차
4. 엔드포인트 목록 (태그별 그룹화)
5. 엔드포인트 상세 정보
   - 요청 파라미터
   - 요청 본문 스키마
   - 응답 스키마 및 예시
6. 데이터 모델 스키마

## 개발자 가이드

### 프로젝트 구조

```
openapi_to_markdown/
├── __init__.py
├── cli.py                  # 명령줄 인터페이스
├── core/                   # 핵심 기능
│   ├── __init__.py
│   ├── reference_resolver.py  # 참조 해결 
│   └── spec_loader.py      # 스펙 로드
├── generators/             # 생성 관련 모듈
│   ├── __init__.py
│   ├── example_generator.py  # 예시 생성
│   ├── form_example.py     # form-data 예시 생성
│   ├── json_example.py     # JSON 예시 생성
│   ├── markdown_generator.py  # 마크다운 생성
│   └── xml_example.py      # XML 예시 생성
├── processors/             # 데이터 처리 모듈
│   ├── __init__.py
│   ├── parameter_processor.py  # 파라미터 처리
│   ├── request_processor.py    # 요청 처리
│   ├── response_processor.py   # 응답 처리
│   └── schema_processor.py     # 스키마 처리
└── utils/                  # 유틸리티 모듈
    ├── __init__.py
    ├── file_utils.py       # 파일 처리
    └── markdown_utils.py   # 마크다운 유틸리티
```

### 핵심 모듈 설명

#### 1. 코어 모듈

- **spec_loader.py**: OpenAPI 스펙 파일을 로드하고 기본 유효성을 검증합니다.
- **reference_resolver.py**: 스펙 내의 참조(`$ref`)를 해결하고 완전한 객체로 변환합니다.

### 예제 입력 및 출력

예를 들어, 다음과 같은 간단한 OpenAPI 스펙 YAML 파일이 있다고 가정해 보겠습니다:

```yaml
openapi: 3.0.0
info:
  title: 샘플 API
  version: 1.0.0
  description: 이것은 샘플 API입니다.
tags:
  - name: User
    description: 사용자 관련 API
paths:
  /users:
    get:
      tags:
        - User
      summary: 사용자 목록 조회
      responses:
        '200':
          description: 성공
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
          description: 사용자 ID
        name:
          type: string
          description: 사용자 이름
```

위의 스펙 파일을 변환하면 다음과 같은 마크다운 문서가 생성됩니다:

````markdown
# 샘플 API v1.0.0

이것은 샘플 API입니다.

## 목차

### User 사용자 관련 API

- [GET /users](#get-users) - 사용자 목록 조회

## User

사용자 관련 API

<h3 id='get-users'></h3>

### GET /users

**사용자 목록 조회**

No description provided

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 성공


##### 응답 스키마

**응답 형식**: 배열


**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**

배열 아이템 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 사용자 ID |
| `name` | string | false | 사용자 이름 |


**Content Type**: application/json


**예시:**

```json
[
  {
    "id": 0,
    "name": "example_value"
  }
]
```



---

## 스키마

API에서 사용되는 데이터 모델 스키마입니다.


### User

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 사용자 ID |
| `name` | string | false | 사용자 이름 |


**예시:**

```json
{
  "id": 0,
  "name": "example_value"
}
```
````

#### 2. 제너레이터 모듈

- **markdown_generator.py**: 전체 마크다운 문서를 생성하는 메인 생성기입니다.
- **example_generator.py**: 스키마에서 예시 데이터를 생성하는 기본 클래스입니다.
- **json_example.py**: JSON 형식의 예시를 생성합니다.
- **xml_example.py**: XML 형식의 예시를 생성합니다.
- **form_example.py**: form-data 형식의 예시를 생성합니다.

#### 3. 프로세서 모듈

- **parameter_processor.py**: API 엔드포인트의 파라미터를 처리합니다.
- **request_processor.py**: API 요청 본문을 처리합니다.
- **response_processor.py**: API 응답을 처리합니다.
- **schema_processor.py**: 데이터 스키마를 처리합니다.

#### 4. 유틸리티 모듈

- **file_utils.py**: 파일 입출력과 관련된 유틸리티 함수를 제공합니다.
- **markdown_utils.py**: 마크다운 포맷팅 유틸리티를 제공합니다.

### 기여 방법

이 프로젝트에 기여하고 싶다면 다음 단계를 따라주세요:

1. 이 저장소를 포크(Fork)합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`).
3. 변경사항을 커밋합니다 (`git commit -m '새로운 기능 추가'`).
4. 브랜치를 푸시합니다 (`git push origin feature/amazing-feature`).
5. Pull Request를 생성합니다.

#### 코딩 스타일

- PEP 8 스타일 가이드를 따릅니다.
- 함수와 클래스에는 문서화 주석(docstring)을 작성합니다.
- 코드 변경 시 적절한 테스트를 추가합니다.

### 테스트

테스트를 실행하려면:

```bash
# 모든 테스트 실행
python -m unittest discover

# 특정 테스트 실행
python -m unittest test_converter.py
```

## 알려진 이슈 및 제한 사항

- JSON 형식의 OpenAPI 스펙 파일 직접 지원 부재
- 일부 복잡한 스키마 구조에서 참조 해결이 부정확할 수 있음
- 현재는 OpenAPI 3.0만 지원 (3.1 지원 계획 중)

## 향후 계획

- JSON 형식 OpenAPI 스펙 직접 지원
- OpenAPI 3.1 지원
- 다양한 마크다운 스타일 및 테마 지원
- 추가 유닛 테스트 및 통합 테스트
- 웹 인터페이스 추가

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.