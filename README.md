# OpenAPI to Markdown Converter

OpenAPI/Swagger 스펙 문서를 마크다운 형식으로 변환하는 파이썬 스크립트입니다. 이 프로젝트는 Vibe Coding 방식으로 작성되었습니다.

## 기능

- OpenAPI 3.0 스펙 문서(YAML 형식)를 마크다운으로 변환
- 계층 구조와 참조(`$ref`) 적절히 처리
- 요청/응답 예시 자동 생성 (JSON, XML, form-data 등의 형식 지원)
- 단일 파일 및 디렉토리 내 모든 YAML 파일 일괄 처리 지원
- 출력 파일 위치 사용자 지정 가능

**참고**: 현재 버전에서는 YAML 파일만 지원하며, JSON 형식의 OpenAPI 스펙은 직접 지원하지 않습니다. JSON 파일을 처리하려면 먼저 YAML로 변환해야 합니다.

## 설치 및 요구사항

이 스크립트를 실행하기 위해서는 Python 3.6 이상과 다음 패키지가 필요합니다:

```bash
pip install pyyaml
```

## 사용법

### 기본 사용법

단일 파일 변환:

```bash
python openapi_to_markdown.py -f path/to/openapi.yaml
```

출력 파일을 지정하여 변환:

```bash
python openapi_to_markdown.py -f path/to/openapi.yaml -o path/to/output.md
```

### 디렉토리 일괄 처리

디렉토리 내 모든 YAML 파일을 변환:

```bash
python openapi_to_markdown.py -d path/to/directory
```

출력 디렉토리를 지정하여 변환:

```bash
python openapi_to_markdown.py -d path/to/directory -od path/to/output_directory
```

## 명령줄 옵션

| 옵션 | 설명 |
|------|------|
| `-f`, `--file` | 변환할 OpenAPI 스펙 파일 경로 (YAML 형식) |
| `-d`, `--directory` | OpenAPI 스펙 파일이 포함된 디렉토리 경로 (하위 디렉토리의 모든 YAML 파일 처리) |
| `-o`, `--output` | 생성된 마크다운 파일 경로 (`--file` 옵션과 함께 사용) |
| `-od`, `--output-directory` | 생성된 마크다운 파일을 저장할 디렉토리 경로 (`--directory` 옵션과 함께 사용) |

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

## 예시

OpenAPI 스펙 파일:

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

- [GET /users](#get--users) - 사용자 목록 조회


## User

사용자 관련 API

<h3 id='get--users'></h3>

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

```json
[
  {
    "id": 0,
    "name": "example_name"
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
  "name": "example_name"
}

```
````

## 코드 구조

프로젝트의 주요 함수는 다음과 같습니다:

### 핵심 기능 함수
- `load_openapi_spec(file_path)`: YAML 파일에서 OpenAPI 스펙을 로드
- `resolve_schema_ref(ref, spec)`: $ref 참조를 통해 실제 스키마 객체 검색
- `convert_refs(spec)`: 전체 스펙의 모든 $ref 참조를 실제 객체로 변환
- `format_schema_as_table(schema, title, spec)`: 스키마를 마크다운 테이블로 변환
- `generate_markdown(spec)`: 전체 마크다운 문서 생성

### 데이터 변환 함수
- `dict_to_form(d, parent_key)`: 사전 형식의 데이터를 form-data 문자열로 변환
- `dict_to_xml_example(data, schema, spec, root_name, indent)`: 사전 형식의 데이터를 XML로 변환
- `generate_example_from_schema(schema, spec)`: 스키마 정의에서 예시 데이터 생성
- `format_example(example, schema, content_type, spec)`: 컨텐츠 타입에 맞게 예시 데이터 포맷팅

### 데이터 처리 함수
- `process_parameters(parameters, markdown, spec)`: API 엔드포인트 파라미터 처리
- `process_request_body(request_body, markdown, spec)`: API 요청 본문 처리
- `process_response(status, response, markdown, spec)`: API 응답 처리
- `process_enum_values(schema, description)`: enum 값 처리
- `process_explode_param(param, description)`: explode 파라미터 처리
- `process_array_param(schema, description)`: 배열 파라미터 처리

### 파일 처리 함수
- `process_file(input_file, output_file)`: 단일 YAML 파일 처리
- `process_directory(input_dir, output_dir)`: 디렉토리 내 모든 YAML 파일 처리

## 알려진 이슈

코드 분석을 통해 발견된 몇 가지 이슈가 있습니다:

1. **구조적 이슈**:
   - 모놀리식 구조: 모든 코드가 단일 파일에 존재하여 유지보수와 확장이 어려움
   - 함수간 높은 결합도: 함수들이 서로 밀접하게 결합되어 있어 분리가 어려움
   - 중복 코드: enum 값 처리, 예시 생성 등에서 중복 코드가 존재함
   - 너무 큰 함수들: 일부 함수(특히 format_schema_as_table, generate_markdown)가 매우 길고 복잡함

2. **기능적 이슈**:
   - JSON 형식의 OpenAPI 스펙 파일 직접 지원 부재
   - 일부 복잡한 스키마 구조에서 참조 해결이 부정확할 수 있음

## 기여하기

이 프로젝트는 오픈소스이며, 기여를 환영합니다. 기여 방법:

1. 이 저장소를 포크(Fork)합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`).
3. 변경사항을 커밋합니다 (`git commit -m '새로운 기능 추가'`).
4. 브랜치를 푸시합니다 (`git push origin feature/amazing-feature`).
5. Pull Request를 생성합니다.

## 향후 계획

이 프로젝트는 리팩토링을 통해 다음과 같은 개선을 계획하고 있습니다:

### 구조적 개선
- 객체지향 아키텍처 도입: 기능별 클래스로 분리
- 모듈화: 기능별로 파일 분리
- 테스트 코드 추가: 단위 테스트 및 통합 테스트

### 기능적 개선
- JSON 형식 OpenAPI 스펙 직접 지원
- 다양한 마크다운 형식 및 스타일 지원
- OpenAPI 3.1 지원

## 라이선스

MIT License