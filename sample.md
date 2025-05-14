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