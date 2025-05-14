# Swagger Petstore - OpenAPI 3.0 v1.0.12

This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about
Swagger at [https://swagger.io](https://swagger.io). In the third iteration of the pet store, we've switched to the design first approach!
You can now help us improve the API whether it's by making changes to the definition itself or to the code.
That way, with time, we can improve the API in general, and expose some of the new features in OAS3.

Some useful links:
- [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
- [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)

## 서버

* **https://petstore3.swagger.io/api/v3**

## 목차

### pet Everything about your Pets

- [PUT /pet](#put-pet) - Update an existing pet.
- [POST /pet](#post-pet) - Add a new pet to the store.
- [GET /pet/findByStatus](#get-pet-findbystatus) - Finds Pets by status.
- [GET /pet/findByTags](#get-pet-findbytags) - Finds Pets by tags.
- [GET /pet/{petId}](#get-pet-petid-) - Find pet by ID.
- [POST /pet/{petId}](#post-pet-petid-) - Updates a pet in the store with form data.
- [DELETE /pet/{petId}](#delete-pet-petid-) - Deletes a pet.
- [POST /pet/{petId}/uploadImage](#post-pet-petid-uploadimage) - Uploads an image.

### store Access to Petstore orders

- [GET /store/inventory](#get-store-inventory) - Returns pet inventories by status.
- [POST /store/order](#post-store-order) - Place an order for a pet.
- [GET /store/order/{orderId}](#get-store-order-orderid-) - Find purchase order by ID.
- [DELETE /store/order/{orderId}](#delete-store-order-orderid-) - Delete purchase order by identifier.

### user Operations about user

- [POST /user](#post-user) - Create user.
- [POST /user/createWithList](#post-user-createwithlist) - Creates list of users with given input array.
- [GET /user/login](#get-user-login) - Logs user into the system.
- [GET /user/logout](#get-user-logout) - Logs out current logged in user session.
- [GET /user/{username}](#get-user-username-) - Get user by user name.
- [PUT /user/{username}](#put-user-username-) - Update user resource.
- [DELETE /user/{username}](#delete-user-username-) - Delete user resource.

## pet

Everything about your Pets

<h3 id='put-pet'></h3>

### PUT /pet

**Update an existing pet.**

Update an existing pet by Id.

#### 요청 본문

Update an existent pet in the store

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**예시:**

```json
{
  "id": 10,
  "name": "doggie",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "example_value"
  ],
  "tags": [
    {
      "id": 0,
      "name": "example_value"
    }
  ],
  "status": "available"
}
```


**Content Type**: application/xml

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**예시:**

```xml
<pet>
  <id>10</id>
  <name>doggie</name>
  <category>
    <id>1</id>
    <name>Dogs</name>
  </category>
  <photoUrls>
    <photoUrl>example_value</photoUrl>
  </photoUrls>
  <tags>
    <tag>
      <id>0</id>
      <name>example_value</name>
    </tag>
  </tags>
  <status>available</status>
</pet>
```


**Content Type**: application/x-www-form-urlencoded

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**예시:**

```http
id=10
name=doggie
category.id=1
category.name=Dogs
photoUrls[0]=example_value
tags[0].id=0
tags[0].name=example_value
status=available
```

#### 응답


**상태 코드**: `200`

**설명**: Successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "name": "doggie",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "example_value"
  ],
  "tags": [
    {
      "id": 0,
      "name": "example_value"
    }
  ],
  "status": "available"
}
```


| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/xml


**예시:**

```xml
<pet>
  <id>10</id>
  <name>doggie</name>
  <category>
    <id>1</id>
    <name>Dogs</name>
  </category>
  <photoUrls>
    <photoUrl>example_value</photoUrl>
  </photoUrls>
  <tags>
    <tag>
      <id>0</id>
      <name>example_value</name>
    </tag>
  </tags>
  <status>available</status>
</pet>
```



**상태 코드**: `400`

**설명**: Invalid ID supplied


**상태 코드**: `404`

**설명**: Pet not found


**상태 코드**: `422`

**설명**: Validation exception


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='post-pet'></h3>

### POST /pet

**Add a new pet to the store.**

Add a new pet to the store.

#### 요청 본문

Create a new pet in the store

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**예시:**

```json
{
  "id": 10,
  "name": "doggie",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "example_value"
  ],
  "tags": [
    {
      "id": 0,
      "name": "example_value"
    }
  ],
  "status": "available"
}
```


**Content Type**: application/xml

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**예시:**

```xml
<pet>
  <id>10</id>
  <name>doggie</name>
  <category>
    <id>1</id>
    <name>Dogs</name>
  </category>
  <photoUrls>
    <photoUrl>example_value</photoUrl>
  </photoUrls>
  <tags>
    <tag>
      <id>0</id>
      <name>example_value</name>
    </tag>
  </tags>
  <status>available</status>
</pet>
```


**Content Type**: application/x-www-form-urlencoded

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**예시:**

```http
id=10
name=doggie
category.id=1
category.name=Dogs
photoUrls[0]=example_value
tags[0].id=0
tags[0].name=example_value
status=available
```

#### 응답


**상태 코드**: `200`

**설명**: Successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "name": "doggie",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "example_value"
  ],
  "tags": [
    {
      "id": 0,
      "name": "example_value"
    }
  ],
  "status": "available"
}
```


| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/xml


**예시:**

```xml
<pet>
  <id>10</id>
  <name>doggie</name>
  <category>
    <id>1</id>
    <name>Dogs</name>
  </category>
  <photoUrls>
    <photoUrl>example_value</photoUrl>
  </photoUrls>
  <tags>
    <tag>
      <id>0</id>
      <name>example_value</name>
    </tag>
  </tags>
  <status>available</status>
</pet>
```



**상태 코드**: `400`

**설명**: Invalid input


**상태 코드**: `422`

**설명**: Validation exception


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='get-pet-findbystatus'></h3>

### GET /pet/findByStatus

**Finds Pets by status.**

Multiple status values can be provided with comma separated strings.

#### 요청 파라미터


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `status` | string | false | Status values that need to be considered for filter<br>(Enum: `available`, `pending`, `sold`)<br>(explode: true) |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

**응답 형식**: 배열


**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**

배열 아이템 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/json


**예시:**

```json
[
  {
    "id": 10,
    "name": "doggie",
    "category": {
      "id": 1,
      "name": "Dogs"
    },
    "photoUrls": [
      "example_value"
    ],
    "tags": [
      {
        "id": 0,
        "name": "example_value"
      }
    ],
    "status": "available"
  }
]
```


**응답 형식**: 배열


**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**

배열 아이템 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/xml


**예시:**

```xml
<pet>
  <id>10</id>
  <name>doggie</name>
  <category>
    <id>1</id>
    <name>Dogs</name>
  </category>
  <photoUrls>
    <photoUrl>example_value</photoUrl>
  </photoUrls>
  <tags>
    <tag>
      <id>0</id>
      <name>example_value</name>
    </tag>
  </tags>
  <status>available</status>
</pet>
```



**상태 코드**: `400`

**설명**: Invalid status value


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='get-pet-findbytags'></h3>

### GET /pet/findByTags

**Finds Pets by tags.**

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

#### 요청 파라미터


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `tags` | array | false | Tags to filter by<br>(explode: true) |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

**응답 형식**: 배열


**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**

배열 아이템 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/json


**예시:**

```json
[
  {
    "id": 10,
    "name": "doggie",
    "category": {
      "id": 1,
      "name": "Dogs"
    },
    "photoUrls": [
      "example_value"
    ],
    "tags": [
      {
        "id": 0,
        "name": "example_value"
      }
    ],
    "status": "available"
  }
]
```


**응답 형식**: 배열


**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**

배열 아이템 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/xml


**예시:**

```xml
<pet>
  <id>10</id>
  <name>doggie</name>
  <category>
    <id>1</id>
    <name>Dogs</name>
  </category>
  <photoUrls>
    <photoUrl>example_value</photoUrl>
  </photoUrls>
  <tags>
    <tag>
      <id>0</id>
      <name>example_value</name>
    </tag>
  </tags>
  <status>available</status>
</pet>
```



**상태 코드**: `400`

**설명**: Invalid tag value


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='get-pet-petid-'></h3>

### GET /pet/{petId}

**Find pet by ID.**

Returns a single pet.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `petId` | integer | true | ID of pet to return |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "name": "doggie",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "example_value"
  ],
  "tags": [
    {
      "id": 0,
      "name": "example_value"
    }
  ],
  "status": "available"
}
```


| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/xml


**예시:**

```xml
<pet>
  <id>10</id>
  <name>doggie</name>
  <category>
    <id>1</id>
    <name>Dogs</name>
  </category>
  <photoUrls>
    <photoUrl>example_value</photoUrl>
  </photoUrls>
  <tags>
    <tag>
      <id>0</id>
      <name>example_value</name>
    </tag>
  </tags>
  <status>available</status>
</pet>
```



**상태 코드**: `400`

**설명**: Invalid ID supplied


**상태 코드**: `404`

**설명**: Pet not found


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='post-pet-petid-'></h3>

### POST /pet/{petId}

**Updates a pet in the store with form data.**

Updates a pet resource based on the form data.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `petId` | integer | true | ID of pet that needs to be updated |


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `name` | string | false | Name of pet that needs to be updated |
| `status` | string | false | Status of pet that needs to be updated |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "name": "doggie",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "example_value"
  ],
  "tags": [
    {
      "id": 0,
      "name": "example_value"
    }
  ],
  "status": "available"
}
```


| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;object&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**Content Type**: application/xml


**예시:**

```xml
<pet>
  <id>10</id>
  <name>doggie</name>
  <category>
    <id>1</id>
    <name>Dogs</name>
  </category>
  <photoUrls>
    <photoUrl>example_value</photoUrl>
  </photoUrls>
  <tags>
    <tag>
      <id>0</id>
      <name>example_value</name>
    </tag>
  </tags>
  <status>available</status>
</pet>
```



**상태 코드**: `400`

**설명**: Invalid input


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='delete-pet-petid-'></h3>

### DELETE /pet/{petId}

**Deletes a pet.**

Delete a pet.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `petId` | integer | true | Pet id to delete |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `api_key` | string | false |  |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: Pet deleted


**상태 코드**: `400`

**설명**: Invalid pet value


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='post-pet-petid-uploadimage'></h3>

### POST /pet/{petId}/uploadImage

**Uploads an image.**

Upload image of the pet.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `petId` | integer | true | ID of pet to update |


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `additionalMetadata` | string | false | Additional Metadata |

#### 요청 본문


**Content Type**: application/octet-stream

**타입**: string

**포맷**: binary



**예시:**

```json
"example_value"
```

#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | integer | false | \- |
| `type` | string | false | \- |
| `message` | string | false | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": 0,
  "type": "example_value",
  "message": "example_value"
}
```



**상태 코드**: `400`

**설명**: No file uploaded


**상태 코드**: `404`

**설명**: Pet not found


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

## store

Access to Petstore orders

<h3 id='get-store-inventory'></h3>

### GET /store/inventory

**Returns pet inventories by status.**

Returns a map of status codes to quantities.

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

**타입**: object



**Content Type**: application/json


**예시:**

```json
{}
```



**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='post-store-order'></h3>

### POST /store/order

**Place an order for a pet.**

Place a new order in the store.

#### 요청 본문


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `petId` | integer | false | \- |
| `quantity` | integer | false | \- |
| `shipDate` | string | false | \- |
| `status` | string | false | Order Status<br>(Enum: `placed`, `approved`, `delivered`) |
| `complete` | boolean | false | \- |


**예시:**

```json
{
  "id": 10,
  "petId": 198772,
  "quantity": 7,
  "shipDate": "2023-01-01T00:00:00Z",
  "status": "approved",
  "complete": false
}
```


**Content Type**: application/xml

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `petId` | integer | false | \- |
| `quantity` | integer | false | \- |
| `shipDate` | string | false | \- |
| `status` | string | false | Order Status<br>(Enum: `placed`, `approved`, `delivered`) |
| `complete` | boolean | false | \- |


**예시:**

```xml
<order>
  <id>10</id>
  <petId>198772</petId>
  <quantity>7</quantity>
  <shipDate>2023-01-01T00:00:00Z</shipDate>
  <status>approved</status>
  <complete>False</complete>
</order>
```


**Content Type**: application/x-www-form-urlencoded

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `petId` | integer | false | \- |
| `quantity` | integer | false | \- |
| `shipDate` | string | false | \- |
| `status` | string | false | Order Status<br>(Enum: `placed`, `approved`, `delivered`) |
| `complete` | boolean | false | \- |


**예시:**

```http
id=10
petId=198772
quantity=7
shipDate=2023-01-01T00:00:00Z
status=approved
complete=False
```

#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `petId` | integer | false | \- |
| `quantity` | integer | false | \- |
| `shipDate` | string | false | \- |
| `status` | string | false | Order Status<br>(Enum: `placed`, `approved`, `delivered`) |
| `complete` | boolean | false | \- |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "petId": 198772,
  "quantity": 7,
  "shipDate": "2023-01-01T00:00:00Z",
  "status": "approved",
  "complete": false
}
```



**상태 코드**: `400`

**설명**: Invalid input


**상태 코드**: `422`

**설명**: Validation exception


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='get-store-order-orderid-'></h3>

### GET /store/order/{orderId}

**Find purchase order by ID.**

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `orderId` | integer | true | ID of order that needs to be fetched |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `petId` | integer | false | \- |
| `quantity` | integer | false | \- |
| `shipDate` | string | false | \- |
| `status` | string | false | Order Status<br>(Enum: `placed`, `approved`, `delivered`) |
| `complete` | boolean | false | \- |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "petId": 198772,
  "quantity": 7,
  "shipDate": "2023-01-01T00:00:00Z",
  "status": "approved",
  "complete": false
}
```


| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `petId` | integer | false | \- |
| `quantity` | integer | false | \- |
| `shipDate` | string | false | \- |
| `status` | string | false | Order Status<br>(Enum: `placed`, `approved`, `delivered`) |
| `complete` | boolean | false | \- |


**Content Type**: application/xml


**예시:**

```xml
<order>
  <id>10</id>
  <petId>198772</petId>
  <quantity>7</quantity>
  <shipDate>2023-01-01T00:00:00Z</shipDate>
  <status>approved</status>
  <complete>False</complete>
</order>
```



**상태 코드**: `400`

**설명**: Invalid ID supplied


**상태 코드**: `404`

**설명**: Order not found


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='delete-store-order-orderid-'></h3>

### DELETE /store/order/{orderId}

**Delete purchase order by identifier.**

For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `orderId` | integer | true | ID of the order that needs to be deleted |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: order deleted


**상태 코드**: `400`

**설명**: Invalid ID supplied


**상태 코드**: `404`

**설명**: Order not found


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

## user

Operations about user

<h3 id='post-user'></h3>

### POST /user

**Create user.**

This can only be done by the logged in user.

#### 요청 본문

Created user object


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**예시:**

```json
{
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
```


**Content Type**: application/xml

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**예시:**

```xml
<user>
  <id>10</id>
  <username>theUser</username>
  <firstName>John</firstName>
  <lastName>James</lastName>
  <email>john@email.com</email>
  <password>12345</password>
  <phone>12345</phone>
  <userStatus>1</userStatus>
</user>
```


**Content Type**: application/x-www-form-urlencoded

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**예시:**

```http
id=10
username=theUser
firstName=John
lastName=James
email=john@email.com
password=12345
phone=12345
userStatus=1
```

#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
```


| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**Content Type**: application/xml


**예시:**

```xml
<user>
  <id>10</id>
  <username>theUser</username>
  <firstName>John</firstName>
  <lastName>James</lastName>
  <email>john@email.com</email>
  <password>12345</password>
  <phone>12345</phone>
  <userStatus>1</userStatus>
</user>
```



**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='post-user-createwithlist'></h3>

### POST /user/createWithList

**Creates list of users with given input array.**

Creates list of users with given input array.

#### 요청 본문


**Content Type**: application/json

**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**

배열 아이템 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**예시:**

```json
[
  {
    "id": 10,
    "username": "theUser",
    "firstName": "John",
    "lastName": "James",
    "email": "john@email.com",
    "password": "12345",
    "phone": "12345",
    "userStatus": 1
  }
]
```

#### 응답


**상태 코드**: `200`

**설명**: Successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
```


| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**Content Type**: application/xml


**예시:**

```xml
<user>
  <id>10</id>
  <username>theUser</username>
  <firstName>John</firstName>
  <lastName>James</lastName>
  <email>john@email.com</email>
  <password>12345</password>
  <phone>12345</phone>
  <userStatus>1</userStatus>
</user>
```



**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='get-user-login'></h3>

### GET /user/login

**Logs user into the system.**

Log into the system.

#### 요청 파라미터


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `username` | string | false | The user name for login |
| `password` | string | false | The password for login in clear text |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `X-Rate-Limit` | integer (int32) | calls per hour allowed by the user |
| `X-Expires-After` | string (date-time) | date in UTC when token expires |


##### 응답 스키마

**타입**: string



**Content Type**: application/xml


**예시:**

```xml
<root>example_value</root>
```


**타입**: string



**Content Type**: application/json


**예시:**

```json
"example_value"
```



**상태 코드**: `400`

**설명**: Invalid username/password supplied


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='get-user-logout'></h3>

### GET /user/logout

**Logs out current logged in user session.**

Log user out of the system.

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='get-user-username-'></h3>

### GET /user/{username}

**Get user by user name.**

Get user detail based on username.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `username` | string | true | The name that needs to be fetched\. Use user1 for testing |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: successful operation


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**Content Type**: application/json


**예시:**

```json
{
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
```


| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**Content Type**: application/xml


**예시:**

```xml
<user>
  <id>10</id>
  <username>theUser</username>
  <firstName>John</firstName>
  <lastName>James</lastName>
  <email>john@email.com</email>
  <password>12345</password>
  <phone>12345</phone>
  <userStatus>1</userStatus>
</user>
```



**상태 코드**: `400`

**설명**: Invalid username supplied


**상태 코드**: `404`

**설명**: User not found


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='put-user-username-'></h3>

### PUT /user/{username}

**Update user resource.**

This can only be done by the logged in user.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `username` | string | true | name that need to be deleted |

#### 요청 본문

Update an existent user in the store


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**예시:**

```json
{
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
```


**Content Type**: application/xml

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**예시:**

```xml
<user>
  <id>10</id>
  <username>theUser</username>
  <firstName>John</firstName>
  <lastName>James</lastName>
  <email>john@email.com</email>
  <password>12345</password>
  <phone>12345</phone>
  <userStatus>1</userStatus>
</user>
```


**Content Type**: application/x-www-form-urlencoded

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**예시:**

```http
id=10
username=theUser
firstName=John
lastName=James
email=john@email.com
password=12345
phone=12345
userStatus=1
```

#### 응답


**상태 코드**: `200`

**설명**: successful operation


**상태 코드**: `400`

**설명**: bad request


**상태 코드**: `404`

**설명**: user not found


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

<h3 id='delete-user-username-'></h3>

### DELETE /user/{username}

**Delete user resource.**

This can only be done by the logged in user.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `username` | string | true | The name that needs to be deleted |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: User deleted


**상태 코드**: `400`

**설명**: Invalid username supplied


**상태 코드**: `404`

**설명**: User not found


**상태 코드**: `default`

**설명**: Unexpected error


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```



---

## 스키마

API에서 사용되는 데이터 모델 스키마입니다.


### Order

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `petId` | integer | false | \- |
| `quantity` | integer | false | \- |
| `shipDate` | string | false | \- |
| `status` | string | false | Order Status<br>(Enum: `placed`, `approved`, `delivered`) |
| `complete` | boolean | false | \- |


**예시:**

```json
{
  "id": 10,
  "petId": 198772,
  "quantity": 7,
  "shipDate": "2023-01-01T00:00:00Z",
  "status": "approved",
  "complete": false
}
```

### Category

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | false | \- |


**예시:**

```json
{
  "id": 1,
  "name": "Dogs"
}
```

### User

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `username` | string | false | \- |
| `firstName` | string | false | \- |
| `lastName` | string | false | \- |
| `email` | string | false | \- |
| `password` | string | false | \- |
| `phone` | string | false | \- |
| `userStatus` | integer | false | User Status |


**예시:**

```json
{
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
```

### Tag

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | false | \- |


**예시:**

```json
{
  "id": 0,
  "name": "example_value"
}
```

### Pet

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | \- |
| `name` | string | true | \- |
| `category` | object | false | \- |
| `category.id` | integer | false | \- |
| `category.name` | string | false | \- |
| `photoUrls[]` | array&lt;string&gt; | true | \- |
| `tags[]` | array&lt;Tag&gt; | false | \- |
| `tags[].id` | integer | false | \- |
| `tags[].name` | string | false | \- |
| `status` | string | false | pet status in the store<br>(Enum: `available`, `pending`, `sold`) |


**예시:**

```json
{
  "id": 10,
  "name": "doggie",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "example_value"
  ],
  "tags": [
    {
      "id": 0,
      "name": "example_value"
    }
  ],
  "status": "available"
}
```

### ApiResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | integer | false | \- |
| `type` | string | false | \- |
| `message` | string | false | \- |


**예시:**

```json
{
  "code": 0,
  "type": "example_value",
  "message": "example_value"
}
```

### Error

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `code` | string | true | \- |
| `message` | string | true | \- |


**예시:**

```json
{
  "code": "example_value",
  "message": "example_value"
}
```