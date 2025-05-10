# 테스트 API v1.0.0

예시 테스트 API

## 목차

### 기타 

- [GET /test](#get--test) - 테스트 API 엔드포인트
- [POST /test](#post--test) - 테스트 데이터 생성


## 기타

<h3 id='get--test'></h3>

### GET /test

**테스트 API 엔드포인트**

테스트 API 설명

#### 요청



#### 응답


**상태 코드**: `200`

**설명**: 성공적인 응답


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | false | \- |

**Content Type**: application/json

```json
{
  "id": 1,
  "name": "테스트 이름"
}
```


---

<h3 id='post--test'></h3>

### POST /test

**테스트 데이터 생성**

테스트 데이터 생성 API

#### 요청


**요청 본문:**


##### 요청 본문 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `name` | string | false | \- |

**Content Type**: application/json

```json
{
  "name": "새 테스트 이름"
}
```

**Content Type**: application/xml

```xml
<root><test><name>XML 테스트 이름</name></test></root>
```


#### 응답


**상태 코드**: `201`

**설명**: 생성됨


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | false | \- |

**Content Type**: application/json


**성공 예시:**

```json
{
  "id": 100,
  "name": "생성된 테스트"
}
```

**다른 예시:**

```json
{
  "id": 101,
  "name": "또 다른 테스트"
}
```


---
