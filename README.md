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

## 라이선스

MIT License