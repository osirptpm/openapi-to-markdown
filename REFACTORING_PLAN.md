# OpenAPI to Markdown 리팩토링 계획

이 문서는 OpenAPI to Markdown 프로젝트의 구조적 리팩토링을 위한 계획을 담고 있습니다. 이 계획의 주요 목표는 현재의 단일 파일, 함수 기반 구현에서 모듈화된 객체지향 설계로 전환하는 것입니다.

## 현재 구조의 문제점

1. **모놀리식 구조**: 모든 코드가 단일 파일에 존재하여 유지보수와 확장이 어려움
2. **함수간 높은 결합도**: 함수들이 서로 밀접하게 결합되어 있어 분리가 어려움
3. **중복 코드**: enum 값 처리, 예시 생성 등에서 중복 코드 발견
4. **너무 큰 함수들**: 일부 함수(특히 format_schema_as_table, generate_markdown)가 매우 길고 복잡함
5. **테스트 어려움**: 모듈화되지 않아 단위 테스트가 어려움

## 리팩토링 목표

1. **모듈화**: 기능별로 분리된 모듈 구조 도입
2. **객체 지향 설계**: 적절한 클래스와 인터페이스 설계
3. **설계 패턴 적용**: 적절한 디자인 패턴 적용
4. **테스트 용이성**: 단위 테스트 작성이 용이하도록 구성
5. **기능 유지**: 기존 기능과 완전히 동일하게 작동

## 새로운 패키지 구조

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

## 클래스 설계

### 코어 클래스

#### `OpenApiSpecLoader` (core/spec_loader.py)
- 책임: OpenAPI 스펙 파일 로드
- 주요 메소드:
  - `load_spec(file_path)`: 파일에서 스펙 로드
  - `validate_spec(spec)`: 스펙 유효성 검증

#### `ReferenceResolver` (core/reference_resolver.py)
- 책임: $ref 참조 해결
- 주요 메소드:
  - `resolve_ref(ref, spec)`: 단일 참조 해결
  - `resolve_all_refs(spec)`: 모든 참조 해결

### 생성기 클래스

#### `MarkdownGenerator` (generators/markdown_generator.py)
- 책임: 마크다운 문서 생성
- 주요 메소드:
  - `generate(spec)`: 전체 마크다운 문서 생성
  - `generate_toc(spec)`: 목차 생성
  - `generate_endpoints(spec)`: 엔드포인트 문서 생성
  - `generate_schemas(spec)`: 스키마 문서 생성

#### `ExampleGenerator` (generators/example_generator.py)
- 타입: 인터페이스 (추상 클래스)
- 책임: 예시 데이터 생성 인터페이스 정의
- 주요 메소드:
  - `generate_example(schema, spec)`: 스키마에서 예시 생성
  - `format_example(example, schema)`: 예시 포맷팅

#### `JsonExampleGenerator` (generators/json_example.py)
- 타입: `ExampleGenerator` 구현
- 책임: JSON 형식의 예시 생성

#### `XmlExampleGenerator` (generators/xml_example.py)
- 타입: `ExampleGenerator` 구현
- 책임: XML 형식의 예시 생성

#### `FormExampleGenerator` (generators/form_example.py)
- 타입: `ExampleGenerator` 구현
- 책임: Form 형식의 예시 생성

### 프로세서 클래스

#### `SchemaProcessor` (processors/schema_processor.py)
- 책임: 스키마 처리
- 주요 메소드:
  - `format_as_table(schema, title, spec)`: 스키마를 마크다운 테이블로 변환

#### `ParameterProcessor` (processors/parameter_processor.py)
- 책임: API 파라미터 처리
- 주요 메소드:
  - `process_parameters(parameters, spec)`: 파라미터 처리 및 마크다운 생성

#### `RequestProcessor` (processors/request_processor.py)
- 책임: 요청 본문 처리
- 주요 메소드:
  - `process_request_body(request_body, spec)`: 요청 본문 처리

#### `ResponseProcessor` (processors/response_processor.py)
- 책임: 응답 처리
- 주요 메소드:
  - `process_response(status, response, spec)`: 응답 처리

### 유틸리티 클래스

#### `MarkdownUtils` (utils/markdown_utils.py)
- 책임: 마크다운 관련 유틸리티
- 주요 메소드:
  - `escape_markdown(text)`: 특수 문자 이스케이프
  - `create_table(headers, rows)`: 마크다운 테이블 생성

#### `FileUtils` (utils/file_utils.py)
- 책임: 파일 처리 유틸리티
- 주요 메소드:
  - `save_markdown(content, file_path)`: 마크다운 파일 저장
  - `process_directory(input_dir, output_dir)`: 디렉토리 처리

## 적용할 디자인 패턴

1. **전략 패턴 (Strategy Pattern)**
   - 목적: 다양한 예시 생성 알고리즘 캡슐화
   - 적용: `ExampleGenerator` 인터페이스와 구현 클래스들 (JSON, XML, Form)

2. **팩토리 패턴 (Factory Pattern)**
   - 목적: 컨텐츠 타입에 따른 적절한 예시 생성기 생성
   - 적용: `ExampleGeneratorFactory` 클래스

3. **빌더 패턴 (Builder Pattern)**
   - 목적: 복잡한 마크다운 문서 구성 과정 단순화
   - 적용: `MarkdownBuilder` 클래스

4. **싱글톤 패턴 (Singleton Pattern)**
   - 목적: 전역적으로 접근 가능한 설정 관리
   - 적용: `Configuration` 클래스

5. **방문자 패턴 (Visitor Pattern)**
   - 목적: OpenAPI 스펙의 다양한 요소를 효율적으로 처리
   - 적용: `OpenApiVisitor` 및 관련 클래스

## 마이그레이션 접근 방식

1. **점진적 리팩토링**
   - 기존 기능을 유지하면서 점진적으로 새로운 구조 도입
   - 단계별 구현 및 테스트

2. **기존 함수의 클래스화**
   - 기존 함수를 관련 클래스의 메소드로 이동
   - 필요한 상태를 클래스 멤버로 이동

3. **인터페이스 도입**
   - 중요 기능에 대한 인터페이스 정의
   - 플러그인 형태의 확장성 제공

4. **의존성 주입 활용**
   - 클래스 간 의존성 명시적으로 관리
   - 테스트 용이성 향상

## 테스트 전략

1. **단위 테스트**
   - 각 클래스 및 메소드의 독립적인 동작 검증
   - 모킹을 통한 의존성 분리

2. **통합 테스트**
   - 여러 컴포넌트가 함께 동작하는 시나리오 검증
   - 실제 OpenAPI 스펙 파일을 사용한 테스트

3. **회귀 테스트**
   - 리팩토링 전후의 출력 일관성 검증
   - 기존 기능이 정확히 유지되는지 확인

## 타임라인

1. **준비 단계** (1주)
   - 패키지 구조 생성
   - 기본 인터페이스 정의
   - 테스트 환경 구성

2. **코어 모듈 구현** (1주)
   - `OpenApiSpecLoader` 구현
   - `ReferenceResolver` 구현

3. **생성기 모듈 구현** (2주)
   - `MarkdownGenerator` 구현
   - 예시 생성기 구현 (JSON, XML, Form)

4. **프로세서 모듈 구현** (2주)
   - 스키마, 파라미터, 요청, 응답 프로세서 구현

5. **유틸리티 모듈 구현** (1주)
   - 마크다운, 파일 유틸리티 구현

6. **명령줄 인터페이스 구현** (1주)
   - CLI 기능 재구현

7. **테스트 및 문서화** (2주)
   - 단위/통합 테스트 작성
   - 문서 업데이트
