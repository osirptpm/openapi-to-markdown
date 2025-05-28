# Magic Tool API v2.0.0

API documentation for Magic Tool services.

## 서버

* **http://localhost:1122**

## 목차

### Image Generation 이미지 생성 관련 API

- [POST /apis/generations/image-generation](#post-apis-generations-image-generation) - 이미지 생성 요청
- [GET /apis/generations/image-generation/{id}](#get-apis-generations-image-generation-id-) - 이미지 생성 상태 조회

### Image Constancy 이미지 일관성 관련 API

- [POST /apis/generations/image-constancy](#post-apis-generations-image-constancy) - 이미지 일관성 작업 요청
- [GET /apis/generations/image-constancy/{id}](#get-apis-generations-image-constancy-id-) - 이미지 일관성 작업 상태 조회

### Video Generation Kling Kling 비디오 생성 관련 API

- [POST /apis/generations/video-generation-kling](#post-apis-generations-video-generation-kling) - Kling 비디오 생성 요청
- [GET /apis/generations/video-generation-kling/{id}](#get-apis-generations-video-generation-kling-id-) - Kling 비디오 생성 상태 조회
- [GET /apis/generations/video-generation-kling/templates](#get-apis-generations-video-generation-kling-templates) - Kling 비디오 템플릿 목록 조회
- [POST /apis/generations/video-generation-kling/templates](#post-apis-generations-video-generation-kling-templates) - Kling 비디오 생성 템플릿 생성
- [GET /apis/generations/video-generation-kling/templates/{templateId}](#get-apis-generations-video-generation-kling-templates-templateid-) - Kling 비디오 생성 템플릿 상세 조회
- [PUT /apis/generations/video-generation-kling/templates/{templateId}](#put-apis-generations-video-generation-kling-templates-templateid-) - Kling 비디오 생성 템플릿 수정
- [DELETE /apis/generations/video-generation-kling/templates/{templateId}](#delete-apis-generations-video-generation-kling-templates-templateid-) - Kling 비디오 생성 템플릿 삭제

### Video Generation Gen3 Gen3 비디오 생성 관련 API

- [POST /apis/generations/video-generation-gen3](#post-apis-generations-video-generation-gen3) - Gen3 비디오 생성 요청
- [GET /apis/generations/video-generation-gen3/{id}](#get-apis-generations-video-generation-gen3-id-) - Gen3 비디오 생성 상태 조회
- [GET /apis/generations/video-generation-gen3/templates](#get-apis-generations-video-generation-gen3-templates) - Gen3 비디오 템플릿 목록 조회
- [POST /apis/generations/video-generation-gen3/templates](#post-apis-generations-video-generation-gen3-templates) - Gen3 비디오 생성 템플릿 생성
- [GET /apis/generations/video-generation-gen3/templates/{templateId}](#get-apis-generations-video-generation-gen3-templates-templateid-) - Gen3 비디오 생성 템플릿 상세 조회
- [PUT /apis/generations/video-generation-gen3/templates/{templateId}](#put-apis-generations-video-generation-gen3-templates-templateid-) - Gen3 비디오 생성 템플릿 수정
- [DELETE /apis/generations/video-generation-gen3/templates/{templateId}](#delete-apis-generations-video-generation-gen3-templates-templateid-) - Gen3 비디오 생성 템플릿 삭제

### Voice Generation Clova Clova 음성 생성 관련 API

- [POST /apis/generations/voice-generation-clova](#post-apis-generations-voice-generation-clova) - Clova 음성 생성 요청
- [GET /apis/generations/voice-generation-clova/{id}](#get-apis-generations-voice-generation-clova-id-) - Clova 음성 생성 상태 조회

### History AI 요청 이력 관련 API

- [GET /histories/apis](#get-histories-apis) - 사용자의 AI 작업 요청 이력 조회
- [DELETE /histories/apis/{id}](#delete-histories-apis-id-) - AI 작업 요청 이력 삭제

### Assets Asset 관리 관련 API

- [POST /assets](#post-assets) - Asset 등록
- [GET /assets](#get-assets) - Asset 목록 조회
- [GET /assets/{id}](#get-assets-id-) - Asset 상세 조회
- [DELETE /assets/{id}](#delete-assets-id-) - Asset 삭제
- [POST /assets/files](#post-assets-files) - Asset 파일 등록

### Encode 인코딩 관련 API

- [POST /magic-paint/encodes](#post-magic-paint-encodes) - 인코딩 작업 요청
- [GET /magic-paint/encodes](#get-magic-paint-encodes) - 인코딩 작업 목록 조회
- [GET /magic-paint/encodes/{id}](#get-magic-paint-encodes-id-) - 특정 인코딩 작업 조회
- [DELETE /magic-paint/encodes/{id}](#delete-magic-paint-encodes-id-) - 특정 인코딩 작업 삭제

### Auth 사용자 인증 관련 API

- [POST /auth/key](#post-auth-key) - 로그인 키 요청
- [POST /auth/login](#post-auth-login) - 사용자 로그인
- [POST /auth/logout](#post-auth-logout) - 사용자 로그아웃
- [POST /auth/reissue](#post-auth-reissue) - 토큰 재발급

### Project 프로젝트 관리 관련 API

- [GET /projects](#get-projects) - 프로젝트 목록 조회

### PaintProject 페인트 프로젝트 관리 관련 API

- [POST /magic-paint/paint-projects](#post-magic-paint-paint-projects) - 페인트 프로젝트 생성
- [GET /magic-paint/paint-projects/{id}](#get-magic-paint-paint-projects-id-) - 페인트 프로젝트 상세 조회
- [PUT /magic-paint/paint-projects/{id}](#put-magic-paint-paint-projects-id-) - 페인트 프로젝트 수정
- [DELETE /magic-paint/paint-projects/{id}](#delete-magic-paint-paint-projects-id-) - 페인트 프로젝트 삭제

### User 사용자 관련 API

- [GET /tokens](#get-tokens) - 사용자 토큰 정보 조회

### Static 정적 콘텐츠 제공 API

- [GET /assets/{year}/{month}/{day}/{assetId}/{filename}](#get-assets-year-month-day-assetid-filename-) - 정적 Asset 파일 서빙

### Resources 외부 리소스 관련 API

- [GET /resources/voices](#get-resources-voices) - 음성 리소스 목록 조회
- [GET /resources/voices/tags](#get-resources-voices-tags) - 음성 리소스 태그 목록 조회

### Cuts 컷 관리 관련 API

- [GET /magic-paint/paint-projects/{paint-project-id}/paint-cuts](#get-magic-paint-paint-projects-paint-project-id-paint-cuts) - 컷 목록 조회
- [POST /magic-paint/paint-projects/{paint-project-id}/paint-cuts](#post-magic-paint-paint-projects-paint-project-id-paint-cuts) - 컷 생성
- [PUT /magic-paint/paint-projects/{paint-project-id}/paint-cuts](#put-magic-paint-paint-projects-paint-project-id-paint-cuts) - 컷 목록 일괄 업데이트
- [GET /magic-paint/paint-projects/{paint-project-id}/paint-cuts/{paint-cut-id}](#get-magic-paint-paint-projects-paint-project-id-paint-cuts-paint-cut-id-) - 단일 컷 조회
- [PUT /magic-paint/paint-projects/{paint-project-id}/paint-cuts/{paint-cut-id}](#put-magic-paint-paint-projects-paint-project-id-paint-cuts-paint-cut-id-) - 단일 컷 업데이트
- [DELETE /magic-paint/paint-projects/{paint-project-id}/paint-cuts/{paint-cut-id}](#delete-magic-paint-paint-projects-paint-project-id-paint-cuts-paint-cut-id-) - 단일 컷 삭제

## Image Generation

이미지 생성 관련 API

<h3 id='post-apis-generations-image-generation'></h3>

### POST /apis/generations/image-generation

**이미지 생성 요청**

프롬프트 기반 이미지 생성 작업을 요청합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: multipart/form-data

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `file` | string | false | 이미지 파일 \(img2img 모드일 때 필수\) |
| `param` | object | true | JSON 문자열로 param 값에 전달 |
| `param.prompt` | string | true | 프롬프트 |
| `param.negativePrompt` | string | true | 네거티브 프롬프트 |
| `param.guidanceScale` | number | true | Guidance Scale |
| `param.steps` | integer | true | Inference Steps |
| `param.refinerStrength` | number | true | Refiner Strength |
| `param.seed` | integer | true | Seed |
| `param.numImages` | integer | true | 생성할 이미지 수 |
| `param.width` | integer | true | 생성할 이미지 너비 \(width \* height 의 픽셀 수가 512\*512보다 커야하고 4096\*4096보다 작아야 함\) |
| `param.height` | integer | true | 생성할 이미지 높이 \(width \* height 의 픽셀 수가 512\*512보다 커야하고 4096\*4096보다 작아야 함\) |
| `param.mode` | integer | true | 모드 \(0: text2img, 1: img2img\)<br>(Enum: `0`, `1`) |
| `param.modelType` | integer | true | 모델 타입 \(0: SDXL, 1: Flux\.1 dev\)<br>(Enum: `0`, `1`) |
| `param.loraModel` | integer | true | LoRA 모델 타입 \(Flux\.1\-dev 모델용, \-1: None, 0~7: 각 모델\) 기본값 \-1: None 0: "Flux\.1 D Painting Style \- v1\.0" 1: "Pen drawing \+ watercolor style" 2: "FLUX \- Oil painting" 3: "Impressionist Landscape LoRA for Flux" 4: "35mm\-Photo" 5: "Eldritch Watercolor for Flux" 6: "Flux Dreamscape" 7: "painters\_sketchbook"<br>(Enum: `-1`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`) |
| `param.loraModelScale` | number | true | LoRA 모델 스케일 |
| `param.loraModelSub` | integer | true | Sub LoRA 모델 타입 \(loraModel과 동일한 범위\)<br>(Enum: `-1`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`) |
| `param.loraModelSubScale` | number | true | Sub LoRA 모델 스케일 |
| `paintProjectId` | string | true | 프로젝트 ID |


**예시:**

```json
{
  "file": "example_value",
  "param": {
    "prompt": "example_value",
    "negativePrompt": "example_value",
    "guidanceScale": 0.0,
    "steps": 1,
    "refinerStrength": 0.0,
    "seed": 0,
    "numImages": 1,
    "width": 0,
    "height": 0,
    "mode": 0,
    "modelType": 0,
    "loraModel": -1,
    "loraModelScale": 0.0,
    "loraModelSub": -1,
    "loraModelSubScale": 0.0
  },
  "paintProjectId": "example_value"
}
```

#### 응답


**상태 코드**: `201`

**설명**: 작업 생성 완료


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 작업아이디 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='get-apis-generations-image-generation-id-'></h3>

### GET /apis/generations/image-generation/{id}

**이미지 생성 상태 조회**

요청한 이미지 생성 작업의 현재 상태를 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | \- |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 작업 상태 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업아이디 |
| `status` | string | true | 작업상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `percent` | integer | false | 작업 진행도 |
| `result` | object | false | 작업 결과 데이터 \(completed 상태일 때만 존재\) 가능한 타입: ImageGeneration, ImageConstancy, VideoGenerationGen3, VideoGenerationKling, VoiceGenerationClova (discriminator: type) |
| `errorString` | string | false | 에러 메시지 \(failed 상태일 때만 존재\) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "status": "pending",
  "percent": 0,
  "result": {
    "type": "ImageGeneration",
    "generatedImageList": [
      "example_value"
    ],
    "assets": [
      {
        "id": "example_value",
        "uiRequestId": 0,
        "type": "image",
        "name": "example_value",
        "src": "example_value",
        "size": 0,
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "metadata": {
          "width": 0,
          "height": 0,
          "duration": 0.0,
          "mimeType": "example_value",
          "fps": "example_value"
        },
        "thumbnailSrc": "example_value",
        "isFavorite": 0,
        "createdAt": "example_value",
        "updatedAt": "example_value"
      }
    ]
  },
  "errorString": "example_value"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

## Image Constancy

이미지 일관성 관련 API

<h3 id='post-apis-generations-image-constancy'></h3>

### POST /apis/generations/image-constancy

**이미지 일관성 작업 요청**

스타일을 유지하는 이미지 생성 작업을 요청합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: multipart/form-data

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `styleFiles[]` | array&lt;string&gt; | true | 참조할 스타일 파일<br>용량: 25MB<br>확장자: 'jpg', 'jpeg', 'png'<br>최대 해상도: 3840x2160 |
| `param` | object | true | JSON 문자열로 param 값에 전달 |
| `param.prompt` | string | true | 생성 프롬프트 |
| `param.styleIndex` | integer | true | 스타일 인덱스 |
| `param.matting` | boolean | true | 생성할 이미지 배경 투명 여부 |
| `param.width` | integer | true | 생성할 이미지 가로 픽셀 |
| `param.height` | integer | true | 생성할 이미지 세로 픽셀 |
| `paintProjectId` | string | true | 프로젝트 ID |
| `numImages` | integer | false | 생성할 이미지 개수 |


**예시:**

```json
{
  "styleFiles": [
    "example_value"
  ],
  "param": {
    "prompt": "example_value",
    "styleIndex": 0,
    "matting": false,
    "width": 0,
    "height": 0
  },
  "paintProjectId": "example_value",
  "numImages": 1
}
```

#### 응답


**상태 코드**: `201`

**설명**: 작업 생성 완료


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 작업아이디 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='get-apis-generations-image-constancy-id-'></h3>

### GET /apis/generations/image-constancy/{id}

**이미지 일관성 작업 상태 조회**

요청한 이미지 일관성 작업의 현재 진행 상태를 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | 작업아이디 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 작업 상태 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업아이디 |
| `status` | string | true | 작업상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `percent` | integer | false | 작업 진행도 |
| `result` | object | false | 작업 결과 데이터 \(completed 상태일 때만 존재\) 가능한 타입: ImageGeneration, ImageConstancy, VideoGenerationGen3, VideoGenerationKling, VoiceGenerationClova (discriminator: type) |
| `errorString` | string | false | 에러 메시지 \(failed 상태일 때만 존재\) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "status": "pending",
  "percent": 0,
  "result": {
    "type": "ImageGeneration",
    "generatedImageList": [
      "example_value"
    ],
    "assets": [
      {
        "id": "example_value",
        "uiRequestId": 0,
        "type": "image",
        "name": "example_value",
        "src": "example_value",
        "size": 0,
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "metadata": {
          "width": 0,
          "height": 0,
          "duration": 0.0,
          "mimeType": "example_value",
          "fps": "example_value"
        },
        "thumbnailSrc": "example_value",
        "isFavorite": 0,
        "createdAt": "example_value",
        "updatedAt": "example_value"
      }
    ]
  },
  "errorString": "example_value"
}
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 해당 콘텐츠 경로가 존재하지 않음


---

## Video Generation Kling

Kling 비디오 생성 관련 API

<h3 id='post-apis-generations-video-generation-kling'></h3>

### POST /apis/generations/video-generation-kling

**Kling 비디오 생성 요청**

Kling 기술을 사용한 비디오 생성 작업을 요청합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: multipart/form-data

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `imageInputFile` | string | false | 대상 이미지<br>용량: 10MB 이하<br>확장자: 'jpg', 'jpeg', 'png'<br>해상도: 300x300 이상<br>비율: 1:2\.5 ~ 2\.5:1<br>\*imageInputFile이나 imageTailInputFile 둘 중 하나는 있어야 함 |
| `imageTailInputFile` | string | false | 대상 이미지<br>용량: 10MB 이하<br>확장자: 'jpg', 'jpeg', 'png'<br>해상도: 300x300 이상<br>비율: 1:2\.5 ~ 2\.5:1<br>\*imageInputFile이나 imageTailInputFile 둘 중 하나는 있어야 함 |
| `staticMaskInputFile` | string | false | 사용자가 모션 브러시를 사용하여 만든 마스크 이미지<br>확장자: 'jpg', 'jpeg', 'png'<br>image와 비율이 같아야 함<br>dynamic\_mask와 해상도가 일치해야 함 |
| `dynamicMaskInputFiles[]` | array&lt;string&gt; | false | param\.dynamicMasks\[\]\.trajectories와 순서 일치 필요<br>확장자: 'jpg', 'jpeg', 'png'<br>image와 비율이 같아야 함<br>static\_mask와 해상도가 일치해야 함 |
| `param` | object | false | JSON 문자열로 param 값에 전달 |
| `param.modelName` | string | false | Kling 모델 이름 kling\-v1\-5 만 camera control 사용 가능<br>(Enum: `kling-v1`, `kling-v1-5`, `kling-v1-6`) |
| `param.prompt` | string | true | 비디오 생성 프롬프트 |
| `param.negativePrompt` | string | false | 제외할 내용 프롬프트 |
| `param.cfgScale` | number | false | 비디오 생성의 유연성 \(값이 높을수록 모델의 유연성이 낮고 사용자 프롬프트와의 관련성이 강해짐\) |
| `param.mode` | string | false | 비디오 생성 모드 pro만 camera control 사용 가능<br>(Enum: `std`, `pro`) |
| `param.dynamicMasks[]` | array&lt;object&gt; | false | 동적 브러시 설정 리스트 |
| `param.dynamicMasks[].trajectories` | array | false | 모션 궤적 좌표 리스트 \(5초 동영상을 위해 최대 77개\) |
| `param.cameraControl` | object | false | 카메라 움직임 제어 조건 |
| `param.cameraControl.type` | string | false | 사전 정의된 카메라 움직임 유형<br>(Enum: `simple`, `down_back`, `forward_up`, `right_turn_forward`, `left_turn_forward`) |
| `param.cameraControl.config` | object | false | 카메라 이동 설정 \(type이 simple일 경우만 사용\) |
| `param.cameraControl.config.horizontal` | number | false | 수평이동 \(음수 값은 왼쪽으로, 양수 값은 오른쪽으로 이동\) |
| `param.cameraControl.config.vertical` | number | false | 수직이동 \(음수 값은 하향 이동, 양수 값은 상향 이동\) |
| `param.cameraControl.config.pan` | number | false | 수평면에서의 카메라 회전 \(음수 값은 y축 왼쪽 회전, 양수 값은 y축 오른쪽 회전\) |
| `param.cameraControl.config.tilt` | number | false | 수직면 회전 \(음수 값은 x축 하향 회전, 양수 값은 x축 상향 회전\) |
| `param.cameraControl.config.roll` | number | false | 카메라 롤링 \(음수 값은 z축 반시계 방향, 양수 값은 z축 시계 방향\) |
| `param.cameraControl.config.zoom` | number | false | 줌 \(음수 값은 시야 좁아짐, 양수 값은 시야 넓어짐\) |
| `param.duration` | string | false | 비디오 길이 \(초\)<br>(Enum: `5`, `10`) |
| `paintProjectId` | string | true | 프로젝트 ID |


**예시:**

```json
{
  "imageInputFile": "example_value",
  "imageTailInputFile": "example_value",
  "staticMaskInputFile": "example_value",
  "dynamicMaskInputFiles": [
    "example_value"
  ],
  "param": {
    "modelName": "kling-v1",
    "prompt": "example_value",
    "negativePrompt": "example_value",
    "cfgScale": 0.0,
    "mode": "std",
    "dynamicMasks": [
      {
        "trajectories": [
          {
            "x": 0,
            "y": 0
          }
        ]
      }
    ],
    "cameraControl": {
      "type": "simple",
      "config": {
        "horizontal": 0.0,
        "vertical": 0.0,
        "pan": 0.0,
        "tilt": 0.0,
        "roll": 0.0,
        "zoom": 0.0
      }
    },
    "duration": "5"
  },
  "paintProjectId": "example_value"
}
```

#### 응답


**상태 코드**: `201`

**설명**: 작업 생성 완료


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 작업아이디 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='get-apis-generations-video-generation-kling-id-'></h3>

### GET /apis/generations/video-generation-kling/{id}

**Kling 비디오 생성 상태 조회**

요청한 Kling 비디오 생성 작업의 현재 진행 상태를 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | 작업아이디 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 작업 상태 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업아이디 |
| `status` | string | true | 작업상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `percent` | integer | false | 작업 진행도 |
| `result` | object | false | 작업 결과 데이터 \(completed 상태일 때만 존재\) 가능한 타입: ImageGeneration, ImageConstancy, VideoGenerationGen3, VideoGenerationKling, VoiceGenerationClova (discriminator: type) |
| `errorString` | string | false | 에러 메시지 \(failed 상태일 때만 존재\) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "status": "pending",
  "percent": 0,
  "result": {
    "type": "VideoGenerationKling",
    "generatedVideoList": [
      "example_value"
    ],
    "assets": [
      {
        "id": "example_value",
        "uiRequestId": 0,
        "type": "image",
        "name": "example_value",
        "src": "example_value",
        "size": 0,
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "metadata": {
          "width": 0,
          "height": 0,
          "duration": 0.0,
          "mimeType": "example_value",
          "fps": "example_value"
        },
        "thumbnailSrc": "example_value",
        "isFavorite": 0,
        "createdAt": "example_value",
        "updatedAt": "example_value"
      }
    ]
  },
  "errorString": "example_value"
}
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 해당 콘텐츠 경로가 존재하지 않음


---

<h3 id='get-apis-generations-video-generation-kling-templates'></h3>

### GET /apis/generations/video-generation-kling/templates

**Kling 비디오 템플릿 목록 조회**

사용 가능한 Kling 비디오 생성 템플릿 목록을 조회합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: Kling 비디오 생성 템플릿 목록 조회 성공


##### 응답 스키마

**응답 형식**: 배열


**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**

배열 아이템 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
[
  {
    "id": 0,
    "type": "VIDEO_GENERATION_GEN3",
    "data": "example_value",
    "createdAt": "2023-01-01T00:00:00Z",
    "updatedAt": "2023-01-01T00:00:00Z"
  }
]
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='post-apis-generations-video-generation-kling-templates'></h3>

### POST /apis/generations/video-generation-kling/templates

**Kling 비디오 생성 템플릿 생성**

No description provided

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | string | true | 템플릿 설정 JSON 데이터 |


**예시:**

```json
{
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value"
}
```

#### 응답


**상태 코드**: `201`

**설명**: Kling 비디오 생성 템플릿 생성 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='get-apis-generations-video-generation-kling-templates-templateid-'></h3>

### GET /apis/generations/video-generation-kling/templates/{templateId}

**Kling 비디오 생성 템플릿 상세 조회**

No description provided

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `templateId` | integer | true | 템플릿 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: Kling 비디오 생성 템플릿 조회 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='put-apis-generations-video-generation-kling-templates-templateid-'></h3>

### PUT /apis/generations/video-generation-kling/templates/{templateId}

**Kling 비디오 생성 템플릿 수정**

No description provided

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `templateId` | integer | true | 템플릿 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | string | true | 템플릿 설정 JSON 데이터 |


**예시:**

```json
{
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value"
}
```

#### 응답


**상태 코드**: `200`

**설명**: Kling 비디오 생성 템플릿 수정 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='delete-apis-generations-video-generation-kling-templates-templateid-'></h3>

### DELETE /apis/generations/video-generation-kling/templates/{templateId}

**Kling 비디오 생성 템플릿 삭제**

No description provided

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `templateId` | integer | true | 템플릿 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `204`

**설명**: Kling 비디오 생성 템플릿 삭제 성공 (No Content)


**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

## Video Generation Gen3

Gen3 비디오 생성 관련 API

<h3 id='post-apis-generations-video-generation-gen3'></h3>

### POST /apis/generations/video-generation-gen3

**Gen3 비디오 생성 요청**

Gen3 기술을 사용한 비디오 생성 작업을 요청합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: multipart/form-data

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `file` | string | true | 참조 이미지 \(첫 프레임\) |
| `param` | object | false | JSON 문자열로 param 값에 전달 |
| `param.promptText` | string | false | 생성 프롬프트 |
| `param.seed` | integer | false | 랜덤 시드 값 |
| `param.watermark` | boolean | false | 워터마크 여부 |
| `param.duration` | integer | false | 비디오 길이<br>(Enum: `5`, `10`) |
| `param.ratio` | string | false | 비디오 비율<br>(Enum: `1280:768`, `768:1280`) |
| `paintProjectId` | string | true | 프로젝트 ID |
| `numVideos` | integer | false | 생성할 비디오 개수 |


**예시:**

```json
{
  "file": "example_value",
  "param": {
    "promptText": "example_value",
    "seed": 0,
    "watermark": false,
    "duration": 5,
    "ratio": "1280:768"
  },
  "paintProjectId": "example_value",
  "numVideos": 1
}
```

#### 응답


**상태 코드**: `201`

**설명**: 작업 생성 완료


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 작업아이디 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='get-apis-generations-video-generation-gen3-id-'></h3>

### GET /apis/generations/video-generation-gen3/{id}

**Gen3 비디오 생성 상태 조회**

요청한 Gen3 비디오 생성 작업의 현재 진행 상태를 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | 작업아이디 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 작업 상태 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업아이디 |
| `status` | string | true | 작업상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `percent` | integer | false | 작업 진행도 |
| `result` | object | false | 작업 결과 데이터 \(completed 상태일 때만 존재\) 가능한 타입: ImageGeneration, ImageConstancy, VideoGenerationGen3, VideoGenerationKling, VoiceGenerationClova (discriminator: type) |
| `errorString` | string | false | 에러 메시지 \(failed 상태일 때만 존재\) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "status": "pending",
  "percent": 0,
  "result": {
    "type": "VideoGenerationGen3",
    "generatedVideoList": [
      "example_value"
    ],
    "assets": [
      {
        "id": "example_value",
        "uiRequestId": 0,
        "type": "image",
        "name": "example_value",
        "src": "example_value",
        "size": 0,
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "metadata": {
          "width": 0,
          "height": 0,
          "duration": 0.0,
          "mimeType": "example_value",
          "fps": "example_value"
        },
        "thumbnailSrc": "example_value",
        "isFavorite": 0,
        "createdAt": "example_value",
        "updatedAt": "example_value"
      }
    ]
  },
  "errorString": "example_value"
}
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 해당 콘텐츠 경로가 존재하지 않음


---

<h3 id='get-apis-generations-video-generation-gen3-templates'></h3>

### GET /apis/generations/video-generation-gen3/templates

**Gen3 비디오 템플릿 목록 조회**

사용 가능한 Gen3 비디오 생성 템플릿 목록을 조회합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: Gen3 비디오 생성 템플릿 목록 조회 성공


##### 응답 스키마

**응답 형식**: 배열


**이 응답은 아래 스키마의 배열 형태로 반환됩니다.**

배열 아이템 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
[
  {
    "id": 0,
    "type": "VIDEO_GENERATION_GEN3",
    "data": "example_value",
    "createdAt": "2023-01-01T00:00:00Z",
    "updatedAt": "2023-01-01T00:00:00Z"
  }
]
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='post-apis-generations-video-generation-gen3-templates'></h3>

### POST /apis/generations/video-generation-gen3/templates

**Gen3 비디오 생성 템플릿 생성**

No description provided

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | string | true | 템플릿 설정 JSON 데이터 |


**예시:**

```json
{
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value"
}
```

#### 응답


**상태 코드**: `201`

**설명**: Gen3 비디오 생성 템플릿 생성 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='get-apis-generations-video-generation-gen3-templates-templateid-'></h3>

### GET /apis/generations/video-generation-gen3/templates/{templateId}

**Gen3 비디오 생성 템플릿 상세 조회**

No description provided

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `templateId` | integer | true | 템플릿 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: Gen3 비디오 생성 템플릿 조회 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='put-apis-generations-video-generation-gen3-templates-templateid-'></h3>

### PUT /apis/generations/video-generation-gen3/templates/{templateId}

**Gen3 비디오 생성 템플릿 수정**

No description provided

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `templateId` | integer | true | 템플릿 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | string | true | 템플릿 설정 JSON 데이터 |


**예시:**

```json
{
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value"
}
```

#### 응답


**상태 코드**: `200`

**설명**: Gen3 비디오 생성 템플릿 수정 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='delete-apis-generations-video-generation-gen3-templates-templateid-'></h3>

### DELETE /apis/generations/video-generation-gen3/templates/{templateId}

**Gen3 비디오 생성 템플릿 삭제**

No description provided

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `templateId` | integer | true | 템플릿 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `204`

**설명**: Gen3 비디오 생성 템플릿 삭제 성공 (No Content)


**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

## Voice Generation Clova

Clova 음성 생성 관련 API

<h3 id='post-apis-generations-voice-generation-clova'></h3>

### POST /apis/generations/voice-generation-clova

**Clova 음성 생성 요청**

Clova 기술을 사용한 음성 생성 작업을 요청합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: multipart/form-data

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `param` | object | true | JSON 문자열로 param 값에 전달 |
| `param.speaker` | string | true | 음성 합성 시 사용할 목소리 종류 |
| `param.text` | string | true | 음성으로 변환할 텍스트 \(UTF\-8 인코딩\)\. 언어별 최대 글자 수: 한국어, 일본어, 중국어, 대만어는 2,000자, 영어, 스페인어는 3,000자 |
| `param.volume` | integer | true | 음성 크기: \-5~5 \(기본값: 0\)\. \-5: 0\.5배 작게, 0: 정상 크기, 5: 1\.5배 크게 |
| `param.speed` | integer | true | 음성 속도: \-5~10 \(기본값: 0\)\. \-5: 2\.0배 속도 \(빠르게\), 0: 원음의 속도, 10: 0\.5배 속도 \(느리게\) |
| `param.pitch` | integer | true | 음성 높낮이: \-5~5 \(기본값: 0\)\. \-5: 1\.2배 높게, 0: 정상 높낮이, 5: 0\.8배 낮게 |
| `param.emotion` | integer | true | 음성 감정 정도 \(지원 목소리: nara, vara, vmikyung, vdain, vyuna, vgoeun, vdaeseong\): 0~3 \(기본값: 0\)\. 0: 중립, 1: 슬픔, 2: 기쁨, 3: 분노 \(nara 미지원\)<br>(Enum: `0`, `1`, `2`, `3`) |
| `param.emotionStrength` | integer | true | 음성 감정 강도 \(지원 목소리: vara, vmikyung, vdain, vyuna, vgoeun, vdaeseong\): 0~2 \(기본값: 1\)\. 0: 약함, 1: 보통, 2: 강함<br>(Enum: `0`, `1`, `2`) |
| `param.format` | string | true | 음성 파일 형식<br>(Enum: `mp3`, `wav`) |
| `param.samplingRate` | integer | true | 음성의 샘플링 레이트 \(wav 형식만 지원\)\. 예외적으로 mijin은 16000 레이트만 지원<br>(Enum: `8000`, `16000`, `24000`, `48000`) |
| `param.alpha` | integer | true | 음색: \-5~5 \(기본값: 0\)\. 0보다 클 경우: 높은 음색, 0보다 작을 경우: 낮은 음색 |
| `param.endPitch` | integer | true | 음성의 끝음 처리 \(지원 목소리: clara, matt, meimei, liangliang, chiahua, kuanlin, carmen, jose, d\-로 시작하는 모든 목소리\): \-5~5 \(기본값: 0\)\. 0보다 클 경우: 높은 끝음, 0보다 작을 경우: 낮은 끝음 |
| `paintProjectId` | string | true | 프로젝트 ID |


**예시:**

```json
{
  "param": {
    "speaker": "example_value",
    "text": "example_value",
    "volume": 0,
    "speed": 0,
    "pitch": 0,
    "emotion": 0,
    "emotionStrength": 0,
    "format": "mp3",
    "samplingRate": 8000,
    "alpha": 0,
    "endPitch": 0
  },
  "paintProjectId": "example_value"
}
```

#### 응답


**상태 코드**: `201`

**설명**: 작업 생성 완료


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 작업아이디 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='get-apis-generations-voice-generation-clova-id-'></h3>

### GET /apis/generations/voice-generation-clova/{id}

**Clova 음성 생성 상태 조회**

요청한 Clova 음성 생성 작업의 현재 진행 상태를 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | 작업아이디 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 작업 상태 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업아이디 |
| `status` | string | true | 작업상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `percent` | integer | false | 작업 진행도 |
| `result` | object | false | 작업 결과 데이터 \(completed 상태일 때만 존재\) 가능한 타입: ImageGeneration, ImageConstancy, VideoGenerationGen3, VideoGenerationKling, VoiceGenerationClova (discriminator: type) |
| `errorString` | string | false | 에러 메시지 \(failed 상태일 때만 존재\) |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "status": "pending",
  "percent": 0,
  "result": {
    "type": "VoiceGenerationClova",
    "generatedVoiceList": [
      "example_value"
    ],
    "assets": [
      {
        "id": "example_value",
        "uiRequestId": 0,
        "type": "image",
        "name": "example_value",
        "src": "example_value",
        "size": 0,
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "metadata": {
          "width": 0,
          "height": 0,
          "duration": 0.0,
          "mimeType": "example_value",
          "fps": "example_value"
        },
        "thumbnailSrc": "example_value",
        "isFavorite": 0,
        "createdAt": "example_value",
        "updatedAt": "example_value"
      }
    ]
  },
  "errorString": "example_value"
}
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 해당 콘텐츠 경로가 존재하지 않음


---

## History

AI 요청 이력 관련 API

<h3 id='get-histories-apis'></h3>

### GET /histories/apis

**사용자의 AI 작업 요청 이력 조회**

사용자가 요청한 AI 작업 이력을 조회하는 API

#### 요청 파라미터


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `paintProjectId` | integer | false | 프로젝트 ID로 필터링 |
| `cursorCreatedAt` | string | false | 커서 기반 페이징을 위한 기준 생성 시간 |
| `cursorId` | integer | false | 커서 기반 페이징을 위한 기준 ID |
| `limit` | integer | false | 한 번에 조회할 이력 수 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: AI 작업 요청 이력 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `items[]` | array&lt;object&gt; | true | AI 요청 이력 목록 |
| `items[].id` | integer | true | AI 요청 고유 ID |
| `items[].paintProjectId` | integer | false | 프로젝트 ID |
| `items[].requestType` | string | true | 생성 종류 \(API 별\) |
| `items[].requestData` | string | true | 요청 데이터 |
| `items[].responseData` | string | false | 응답 데이터 |
| `items[].status` | string | true | 요청 상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `items[].errorMessage` | ['string', 'null'] | false | 오류 메시지 \(실패한 경우에만 값 포함\) |
| `items[].createdAt` | string | true | 생성 시간 |
| `items[].updatedAt` | string | false | 수정 시간 |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회를 위한 커서 정보 |
| `cursor.cursorCreatedAt` | string | false | 다음 조회 시 생성 시간 조건에 사용 |
| `cursor.cursorId` | integer | false | 다음 조회 시 ID 조건에 사용 |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**Content Type**: application/json


**예시:**

```json
{
  "items": [
    {
      "id": 0,
      "paintProjectId": 0,
      "requestType": "example_value",
      "requestData": "example_value",
      "responseData": "example_value",
      "status": "pending",
      "errorMessage": "example_value",
      "createdAt": "2023-01-01T00:00:00Z",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ],
  "cursor": {
    "cursorCreatedAt": "example_value",
    "cursorId": 0
  },
  "hasMore": false
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='delete-histories-apis-id-'></h3>

### DELETE /histories/apis/{id}

**AI 작업 요청 이력 삭제**

특정 AI 작업 요청 이력을 삭제하는 API

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 삭제할 AI 요청 이력의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `204`

**설명**: AI 작업 요청 이력 삭제 성공


**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 요청한 ID의 이력을 찾을 수 없음


---

## Assets

Asset 관리 관련 API

<h3 id='post-assets'></h3>

### POST /assets

**Asset 등록**

No description provided

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `url` | string | true | Asset URL |
| `thumbnailUrl` | string | false | 썸네일 URL \(미사용시 url에서 추출\) |
| `type` | string | true | Asset 타입 \(지원: 'image', 'video', 'audio'\)<br>(Enum: `image`, `video`, `audio`) |
| `name` | string | false | Asset 이름 \(미사용시 url에서 추출\) |


**예시:**

```json
{
  "url": "example_value",
  "thumbnailUrl": "example_value",
  "type": "image",
  "name": "example_value"
}
```

#### 응답


**상태 코드**: `201`

**설명**: Asset 등록 완료


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `asset` | object | false | \- |
| `asset.id` | string | true | Asset 고유 식별자\(ID\) |
| `asset.uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `asset.type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `asset.name` | string | true | Asset 이름 |
| `asset.src` | ['string', 'null'] | true | Asset 소스 URL |
| `asset.size` | integer | true | Asset 파일 크기\(바이트\) |
| `asset.width` | integer | true | Asset 너비\(픽셀\) |
| `asset.height` | integer | true | Asset 높이\(픽셀\) |
| `asset.duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `asset.mimeType` | string | true | Asset의 MIME 타입 |
| `asset.metadata` | object | false | 파일 메타데이터 정보 |
| `asset.metadata.width` | integer | false | 원본 파일의 너비\(픽셀\) |
| `asset.metadata.height` | integer | false | 원본 파일의 높이\(픽셀\) |
| `asset.metadata.duration` | ['number', 'null'] | false | 원본 파일의 길이\(초\) |
| `asset.metadata.mimeType` | string | false | 원본 파일의 MIME 타입 |
| `asset.metadata.fps` | ['string', 'null'] | false | 비디오의 초당 프레임 수 \(분수 형태\) |
| `asset.thumbnailSrc` | string | true | Asset 썸네일 URL |
| `asset.isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `asset.createdAt` | string | true | 생성 시간 |
| `asset.updatedAt` | string | true | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "asset": {
    "id": "example_value",
    "uiRequestId": 0,
    "type": "image",
    "name": "example_value",
    "src": "example_value",
    "size": 0,
    "width": 0,
    "height": 0,
    "duration": 0.0,
    "mimeType": "example_value",
    "metadata": {
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "fps": "example_value"
    },
    "thumbnailSrc": "example_value",
    "isFavorite": 0,
    "createdAt": "example_value",
    "updatedAt": "example_value"
  }
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='get-assets'></h3>

### GET /assets

**Asset 목록 조회**

필터 조건에 맞는 Asset 목록을 조회합니다.

#### 요청 파라미터


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | false | 미사용시 해당 유저 전체 목록<br>"video"<br>"audio"<br>"image" |
| `cursorCreatedAt` | string | false | 커서 기반 페이징을 위한 기준 생성 시간\. 이 시간보다 이전에 생성된 항목을 조회 |
| `cursorId` | string | false | 동일 생성 시간 내에서 이 ID보다 작은 항목만 조회하기 위한 보조 커서 |
| `limit` | integer | false | 한 번에 가져올 개수 |
| `isFavorite` | boolean | false | 즐겨찾기 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 자산 목록 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `total` | integer | true | 총 Asset 개수 |
| `assets[]` | array&lt;object&gt; | true | \- |
| `assets[].id` | string | true | Asset 고유 식별자\(ID\) |
| `assets[].uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `assets[].type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `assets[].name` | string | true | Asset 이름 |
| `assets[].src` | ['string', 'null'] | true | Asset 소스 URL |
| `assets[].size` | integer | true | Asset 파일 크기\(바이트\) |
| `assets[].width` | integer | true | Asset 너비\(픽셀\) |
| `assets[].height` | integer | true | Asset 높이\(픽셀\) |
| `assets[].duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `assets[].mimeType` | string | true | Asset의 MIME 타입 |
| `assets[].metadata` | object | false | 파일 메타데이터 정보 |
| `assets[].thumbnailSrc` | string | true | Asset 썸네일 URL |
| `assets[].isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `assets[].createdAt` | string | true | 생성 시간 |
| `assets[].updatedAt` | string | true | 수정 시간 |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회용 커서 정보\. 더 이상 불러올 데이터가 없으면 null을 반환 |
| `cursor.cursorCreatedAt` | string | false | 다음 조회 시 created\_at < 이 값 조건에 사용 |
| `cursor.cursorId` | string | false | 다음 조회 시 \(created\_at = created\_at\_cursor AND id < 이 값\) 조건에 사용 |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**Content Type**: application/json


**예시:**

```json
{
  "total": 0,
  "assets": [
    {
      "id": "example_value",
      "uiRequestId": 0,
      "type": "image",
      "name": "example_value",
      "src": "example_value",
      "size": 0,
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "metadata": {
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "fps": "example_value"
      },
      "thumbnailSrc": "example_value",
      "isFavorite": 0,
      "createdAt": "example_value",
      "updatedAt": "example_value"
    }
  ],
  "cursor": {
    "cursorCreatedAt": "example_value",
    "cursorId": "example_value"
  },
  "hasMore": false
}
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 해당 콘텐츠 경로가 존재하지 않음.


---

<h3 id='get-assets-id-'></h3>

### GET /assets/{id}

**Asset 상세 조회**

특정 ID의 Asset 정보를 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | Asset key \(or id\)\. |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 자산 상세 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | Asset 고유 식별자\(ID\) |
| `uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `name` | string | true | Asset 이름 |
| `src` | ['string', 'null'] | true | Asset 소스 URL |
| `size` | integer | true | Asset 파일 크기\(바이트\) |
| `width` | integer | true | Asset 너비\(픽셀\) |
| `height` | integer | true | Asset 높이\(픽셀\) |
| `duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `mimeType` | string | true | Asset의 MIME 타입 |
| `metadata` | object | false | 파일 메타데이터 정보 |
| `metadata.width` | integer | false | 원본 파일의 너비\(픽셀\) |
| `metadata.height` | integer | false | 원본 파일의 높이\(픽셀\) |
| `metadata.duration` | ['number', 'null'] | false | 원본 파일의 길이\(초\) |
| `metadata.mimeType` | string | false | 원본 파일의 MIME 타입 |
| `metadata.fps` | ['string', 'null'] | false | 비디오의 초당 프레임 수 \(분수 형태\) |
| `thumbnailSrc` | string | true | Asset 썸네일 URL |
| `isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `createdAt` | string | true | 생성 시간 |
| `updatedAt` | string | true | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": "example_value",
  "uiRequestId": 0,
  "type": "image",
  "name": "example_value",
  "src": "example_value",
  "size": 0,
  "width": 0,
  "height": 0,
  "duration": 0.0,
  "mimeType": "example_value",
  "metadata": {
    "width": 0,
    "height": 0,
    "duration": 0.0,
    "mimeType": "example_value",
    "fps": "example_value"
  },
  "thumbnailSrc": "example_value",
  "isFavorite": 0,
  "createdAt": "example_value",
  "updatedAt": "example_value"
}
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 해당 콘텐츠 경로가 존재하지 않음.


---

<h3 id='delete-assets-id-'></h3>

### DELETE /assets/{id}

**Asset 삭제**

특정 ID의 Asset을 삭제합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | Asset key \(or id\)\. |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `204`

**설명**: 삭제 성공.


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='post-assets-files'></h3>

### POST /assets/files

**Asset 파일 등록**

No description provided

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: multipart/form-data

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `file` | string | true | 업로드할 파일 |
| `type` | string | true | Asset 타입<br>(Enum: `image`, `video`, `audio`) |
| `name` | string | false | Asset 이름 \(미사용시 파일명에서 추출\) |


**예시:**

```json
{
  "file": "example_value",
  "type": "image",
  "name": "example_value"
}
```

#### 응답


**상태 코드**: `201`

**설명**: Asset 파일 등록 완료


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `asset` | object | false | \- |
| `asset.id` | string | true | Asset 고유 식별자\(ID\) |
| `asset.uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `asset.type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `asset.name` | string | true | Asset 이름 |
| `asset.src` | ['string', 'null'] | true | Asset 소스 URL |
| `asset.size` | integer | true | Asset 파일 크기\(바이트\) |
| `asset.width` | integer | true | Asset 너비\(픽셀\) |
| `asset.height` | integer | true | Asset 높이\(픽셀\) |
| `asset.duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `asset.mimeType` | string | true | Asset의 MIME 타입 |
| `asset.metadata` | object | false | 파일 메타데이터 정보 |
| `asset.metadata.width` | integer | false | 원본 파일의 너비\(픽셀\) |
| `asset.metadata.height` | integer | false | 원본 파일의 높이\(픽셀\) |
| `asset.metadata.duration` | ['number', 'null'] | false | 원본 파일의 길이\(초\) |
| `asset.metadata.mimeType` | string | false | 원본 파일의 MIME 타입 |
| `asset.metadata.fps` | ['string', 'null'] | false | 비디오의 초당 프레임 수 \(분수 형태\) |
| `asset.thumbnailSrc` | string | true | Asset 썸네일 URL |
| `asset.isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `asset.createdAt` | string | true | 생성 시간 |
| `asset.updatedAt` | string | true | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "asset": {
    "id": "example_value",
    "uiRequestId": 0,
    "type": "image",
    "name": "example_value",
    "src": "example_value",
    "size": 0,
    "width": 0,
    "height": 0,
    "duration": 0.0,
    "mimeType": "example_value",
    "metadata": {
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "fps": "example_value"
    },
    "thumbnailSrc": "example_value",
    "isFavorite": 0,
    "createdAt": "example_value",
    "updatedAt": "example_value"
  }
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

## Encode

인코딩 관련 API

<h3 id='post-magic-paint-encodes'></h3>

### POST /magic-paint/encodes

**인코딩 작업 요청**

비디오/이미지 파일을 인코딩하기 위한 작업을 생성합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: multipart/form-data

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `file` | string | true | 인코딩할 파일 \(비디오/이미지\) |
| `name` | string | true | 출력 파일의 이름 |
| `type` | string | true | 출력 파일 형식<br>(Enum: `mp4`, `webm`, `gif`) |
| `duration` | number | true | 비디오 길이 \(ms\) |
| `width` | integer | true | 출력 너비 \(px\) |
| `height` | integer | true | 출력 높이 \(px\) |
| `fps` | integer | true | 초당 프레임 수 |
| `audio` | string | false | 오디오 정보가 담긴 JSON 파일 \(type이 'gif'가 아닌 경우에만 필요\)\. 각 오디오 트랙의 url, start, end, volume 정보를 포함함 |
| `paintProjectId` | integer | true | 프로젝트 ID |


**예시:**

```json
{
  "file": "example_value",
  "name": "example_value",
  "type": "mp4",
  "duration": 0.0,
  "width": 0,
  "height": 0,
  "fps": 0,
  "audio": "example_value",
  "paintProjectId": 0
}
```

#### 응답


**상태 코드**: `201`

**설명**: 인코딩 작업 생성 완료


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업 ID |
| `paintProjectId` | integer | true | 프로젝트 ID |
| `userId` | ['integer', 'null'] | true | 사용자 ID |
| `status` | integer | true | 인코딩 상태 \(예: \-1: 에러, 0: 완료, 1: 대기, 2: 진행중, 3: 취소\)<br>(Enum: `-1`, `0`, `1`, `2`, `3`) |
| `name` | string | true | 프로젝트 결과 목록에 표시될 이름 / 파일 이름 |
| `src` | ['string', 'null'] | false | 인코딩 파일 출력 경로 |
| `createdAt` | string | true | 생성 시간 |
| `updatedAt` | string | true | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "paintProjectId": 0,
  "userId": 0,
  "status": -1,
  "name": "example_value",
  "src": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='get-magic-paint-encodes'></h3>

### GET /magic-paint/encodes

**인코딩 작업 목록 조회**

No description provided

#### 요청 파라미터


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `paintProjectId` | integer | true | 특정 프로젝트 ID로 작업 필터링 |
| `cursorCreatedAt` | string | false | 커서 기반 페이징을 위한 기준 생성 시간 |
| `cursorId` | integer | false | 커서 기반 페이징을 위한 기준 ID |
| `limit` | integer | false | 한 번에 조회할 작업 수 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 인코딩 작업 목록 조회 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `items[]` | array&lt;object&gt; | true | \- |
| `items[].id` | integer | true | 작업 ID |
| `items[].paintProjectId` | integer | true | 프로젝트 ID |
| `items[].userId` | ['integer', 'null'] | true | 사용자 ID |
| `items[].status` | integer | true | 인코딩 상태 \(예: \-1: 에러, 0: 완료, 1: 대기, 2: 진행중, 3: 취소\)<br>(Enum: `-1`, `0`, `1`, `2`, `3`) |
| `items[].name` | string | true | 프로젝트 결과 목록에 표시될 이름 / 파일 이름 |
| `items[].src` | ['string', 'null'] | false | 인코딩 파일 출력 경로 |
| `items[].createdAt` | string | true | 생성 시간 |
| `items[].updatedAt` | string | true | 수정 시간 |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회용 커서 정보\. 더 이상 불러올 데이터가 없으면 null을 반환 |
| `cursor.cursorCreatedAt` | string | false | 다음 조회 시 생성 시간 조건에 사용 |
| `cursor.cursorId` | integer | false | 다음 조회 시 ID 조건에 사용 |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**Content Type**: application/json


**예시:**

```json
{
  "items": [
    {
      "id": 0,
      "paintProjectId": 0,
      "userId": 0,
      "status": -1,
      "name": "example_value",
      "src": "example_value",
      "createdAt": "2023-01-01T00:00:00Z",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ],
  "cursor": {
    "cursorCreatedAt": "example_value",
    "cursorId": 0
  },
  "hasMore": false
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='get-magic-paint-encodes-id-'></h3>

### GET /magic-paint/encodes/{id}

**특정 인코딩 작업 조회**

No description provided

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 조회할 인코딩 작업의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 인코딩 작업 조회 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업 ID |
| `paintProjectId` | integer | true | 프로젝트 ID |
| `userId` | ['integer', 'null'] | true | 사용자 ID |
| `status` | integer | true | 인코딩 상태 \(예: \-1: 에러, 0: 완료, 1: 대기, 2: 진행중, 3: 취소\)<br>(Enum: `-1`, `0`, `1`, `2`, `3`) |
| `name` | string | true | 프로젝트 결과 목록에 표시될 이름 / 파일 이름 |
| `src` | ['string', 'null'] | false | 인코딩 파일 출력 경로 |
| `createdAt` | string | true | 생성 시간 |
| `updatedAt` | string | true | 수정 시간 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "paintProjectId": 0,
  "userId": 0,
  "status": -1,
  "name": "example_value",
  "src": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

<h3 id='delete-magic-paint-encodes-id-'></h3>

### DELETE /magic-paint/encodes/{id}

**특정 인코딩 작업 삭제**

No description provided

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 삭제할 인코딩 작업의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `204`

**설명**: 인코딩 작업 삭제 성공 (No Content)


**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 파일이 없음


##### 응답 스키마

**타입**: string

**설명**: 파일을 찾을 수 없습니다.



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



---

## Auth

사용자 인증 관련 API

<h3 id='post-auth-key'></h3>

### POST /auth/key

**로그인 키 요청**

RSA 공개키를 발급받기 위한 엔드포인트입니다. 로그인 시 사용자 인증 데이터를 암호화하는데 사용합니다.

#### 요청


#### 응답


**상태 코드**: `201`

**설명**: 키 발급 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `resultCode` | integer | true | 작업 결과 코드 |
| `errorString` | string | false | 에러 메시지 |
| `result` | object | true | 결과 정보 |
| `result.key` | string | true | 생성된 RSA 공개키 \(2048 bits\) |
| `result.keyId` | integer | true | 생성된 RSA 키 페어의 ID |


**Content Type**: application/json


**예시:**

```json
{
  "resultCode": 0,
  "errorString": "example_value",
  "result": {
    "key": "example_value",
    "keyId": 0
  }
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `500`

**설명**: 서버 에러


---

<h3 id='post-auth-login'></h3>

### POST /auth/login

**사용자 로그인**

사용자 ID와 비밀번호를 암호화하여 전송하고 인증 토큰을 발급받습니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | 암호화된 로그인 데이터 \(ID:PW 문자열을 RSA로 암호화\) |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `captcha` | string | true | 암호화된 captcha 데이터 \(<captcha ID>:<captcha key> 문자열을 RSA로 암호화\) |


**예시:**

```json
{
  "captcha": "example_value"
}
```

#### 응답


**상태 코드**: `200`

**설명**: 로그인 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |
| `Set-Cookie` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `resultCode` | integer | true | 작업 결과 코드 |
| `accessToken` | string | true | JWT 형식의 액세스 토큰 |


**Content Type**: application/json


**예시:**

```json
{
  "resultCode": 0,
  "accessToken": "example_value"
}
```



**상태 코드**: `401`

**설명**: 인증 실패


##### 응답 스키마

**다음 중 하나의 스키마를 사용합니다:**

**옵션 1:**
| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `resultCode` | integer | true | \- |
| `errorString` | string | true | \- |
| `result` | object | false | \- |
| `result.loginTryCount` | integer | false | 로그인 시도 횟수 |
| `result.maxLoginTryCount` | integer | false | 최대 로그인 시도 횟수 |

**옵션 2:**
| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `resultCode` | integer | true | \- |
| `errorString` | string | true | \-<br>(Enum: `User is Locked`, `보안문자가 일치하지 않음`, `Failed to login`) |



**Content Type**: application/json


**예시 - wrongCredentials:**

```json
{
  "resultCode": 401,
  "errorString": "id, password 일치하지 않음",
  "result": {
    "loginTryCount": 3,
    "maxLoginTryCount": 5
  }
}
```

**예시 - lockedUser:**

```json
{
  "resultCode": 401,
  "errorString": "User is Locked"
}
```

**예시 - captchaError:**

```json
{
  "resultCode": 401,
  "errorString": "보안문자가 일치하지 않음"
}
```

**예시 - generalError:**

```json
{
  "resultCode": 401,
  "errorString": "Failed to login"
}
```



**상태 코드**: `500`

**설명**: 서버 에러


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `resultCode` | integer | true | \- |
| `errorString` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "resultCode": 0,
  "errorString": "example_value"
}
```



---

<h3 id='post-auth-logout'></h3>

### POST /auth/logout

**사용자 로그아웃**

현재 로그인된 사용자의 세션을 종료합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `204`

**설명**: 로그아웃 성공 (No Content)


**상태 코드**: `401`

**설명**: 인증 실패


---

<h3 id='post-auth-reissue'></h3>

### POST /auth/reissue

**토큰 재발급**

리프레시 토큰을 사용하여 새로운 액세스 토큰을 발급받습니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |


##### 쿠키 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Cookie` | string | true | 리프레시 토큰 쿠키 |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 토큰 재발급 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |
| `Set-Cookie` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `resultCode` | integer | true | \- |
| `errorString` | string | true | \- |
| `result` | object | true | \- |
| `result.accessToken` | string | true | \- |


**Content Type**: application/json


**예시:**

```json
{
  "resultCode": 0,
  "errorString": "example_value",
  "result": {
    "accessToken": "example_value"
  }
}
```



---

## Project

프로젝트 관리 관련 API

<h3 id='get-projects'></h3>

### GET /projects

**프로젝트 목록 조회**

사용자의 프로젝트 목록을 조회합니다.

#### 요청 파라미터


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `cursorCreatedAt` | string | false | 커서 기반 페이징을 위한 기준 생성 시간\. 이 시간보다 이전에 생성된 항목을 조회 |
| `cursorId` | integer | false | 동일 생성 시간 내에서 이 ID보다 작은 항목만 조회하기 위한 보조 커서 |
| `limit` | integer | false | 한 번에 가져올 개수 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 프로젝트 목록 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `items[]` | array&lt;object&gt; | true | \- |
| `items[].id` | integer | true | 프로젝트 고유 식별자 |
| `items[].userId` | string | true | 소유자 ID |
| `items[].name` | string | true | 프로젝트 이름 |
| `items[].description` | ['string', 'null'] | true | 프로젝트 설명 |
| `items[].type` | string | true | 프로젝트 타입 \(paint, generation 등\) |
| `items[].subProjectId` | number | true | 하위 프로젝트 ID \(paint\_project\.id 등\) |
| `items[].thumbnailPath` | string | true | 썸네일 이미지 경로 |
| `items[].isDeleted` | boolean | true | 삭제 여부 \(0: 정상, 1: 삭제됨\) |
| `items[].createdAt` | string | true | 생성 일시 |
| `items[].updatedAt` | string | true | 최종 수정 일시 |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회용 커서 정보\. 더 이상 불러올 데이터가 없으면 null을 반환 |
| `cursor.cursorCreatedAt` | string | false | 다음 조회 시 created\_at < 이 값 조건에 사용 |
| `cursor.cursorId` | integer | false | 다음 조회 시 \(created\_at = created\_at\_cursor AND id < 이 값\) 조건에 사용 |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**Content Type**: application/json


**예시:**

```json
{
  "items": [
    {
      "id": 0,
      "userId": "example_value",
      "name": "example_value",
      "description": "example_value",
      "type": "example_value",
      "subProjectId": 0.0,
      "thumbnailPath": "example_value",
      "isDeleted": false,
      "createdAt": "2023-01-01T00:00:00Z",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ],
  "cursor": {
    "cursorCreatedAt": "example_value",
    "cursorId": 0
  },
  "hasMore": false
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

## PaintProject

페인트 프로젝트 관리 관련 API

<h3 id='post-magic-paint-paint-projects'></h3>

### POST /magic-paint/paint-projects

**페인트 프로젝트 생성**

새로운 페인트 프로젝트를 생성합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `name` | string | true | 페인트 프로젝트 이름 |
| `description` | string | false | 페인트 프로젝트 설명 |
| `duration` | integer | false | 페인트 프로젝트 총 길이 \(밀리초\) |
| `framerate` | number | false | 프레임레이트 \(초당 프레임\) |


**예시:**

```json
{
  "name": "example_value",
  "description": "example_value",
  "duration": 0,
  "framerate": 0.0
}
```

#### 응답


**상태 코드**: `201`

**설명**: 페인트 프로젝트 생성 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 페인트 프로젝트 고유 식별자 |
| `userId` | string | true | 소유자 ID |
| `name` | string | true | 페인트 프로젝트 이름 |
| `description` | ['string', 'null'] | false | 페인트 프로젝트 설명 |
| `duration` | integer | true | 페인트 프로젝트 총 길이 \(밀리초\) |
| `framerate` | number | true | 프레임레이트 \(초당 프레임\) |
| `positionX` | number | true | 현재 편집 화면의 X 위치 |
| `positionY` | number | true | 현재 편집 화면의 Y 위치 |
| `zoomLevel` | number | true | 현재 편집 화면의 확대/축소 수준 |
| `currentTime` | integer | true | 현재 타임라인 위치 \(밀리초\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "userId": "example_value",
  "name": "example_value",
  "description": "example_value",
  "duration": 0,
  "framerate": 0.0,
  "positionX": 0.0,
  "positionY": 0.0,
  "zoomLevel": 0.0,
  "currentTime": 0,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='get-magic-paint-paint-projects-id-'></h3>

### GET /magic-paint/paint-projects/{id}

**페인트 프로젝트 상세 조회**

특정 ID의 페인트 프로젝트 정보를 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 조회할 페인트 프로젝트의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 페인트 프로젝트 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 페인트 프로젝트 고유 식별자 |
| `userId` | string | true | 소유자 ID |
| `name` | string | true | 페인트 프로젝트 이름 |
| `description` | ['string', 'null'] | false | 페인트 프로젝트 설명 |
| `duration` | integer | true | 페인트 프로젝트 총 길이 \(밀리초\) |
| `framerate` | number | true | 프레임레이트 \(초당 프레임\) |
| `positionX` | number | true | 현재 편집 화면의 X 위치 |
| `positionY` | number | true | 현재 편집 화면의 Y 위치 |
| `zoomLevel` | number | true | 현재 편집 화면의 확대/축소 수준 |
| `currentTime` | integer | true | 현재 타임라인 위치 \(밀리초\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "userId": "example_value",
  "name": "example_value",
  "description": "example_value",
  "duration": 0,
  "framerate": 0.0,
  "positionX": 0.0,
  "positionY": 0.0,
  "zoomLevel": 0.0,
  "currentTime": 0,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 페인트 프로젝트를 찾을 수 없음


---

<h3 id='put-magic-paint-paint-projects-id-'></h3>

### PUT /magic-paint/paint-projects/{id}

**페인트 프로젝트 수정**

특정 ID의 페인트 프로젝트 정보를 수정합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 수정할 페인트 프로젝트의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `name` | string | false | 페인트 프로젝트 이름 |
| `description` | string | false | 페인트 프로젝트 설명 |
| `duration` | integer | false | 페인트 프로젝트 총 길이 \(밀리초\) |
| `framerate` | number | false | 프레임레이트 \(초당 프레임\) |
| `positionX` | number | false | 현재 편집 화면의 X 위치 |
| `positionY` | number | false | 현재 편집 화면의 Y 위치 |
| `zoomLevel` | number | false | 현재 편집 화면의 확대/축소 수준 |
| `currentTime` | integer | false | 현재 타임라인 위치 \(밀리초\) |


**예시:**

```json
{
  "name": "example_value",
  "description": "example_value",
  "duration": 0,
  "framerate": 0.0,
  "positionX": 0.0,
  "positionY": 0.0,
  "zoomLevel": 0.0,
  "currentTime": 0
}
```

#### 응답


**상태 코드**: `200`

**설명**: 페인트프로젝트 수정 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 페인트 프로젝트 고유 식별자 |
| `userId` | string | true | 소유자 ID |
| `name` | string | true | 페인트 프로젝트 이름 |
| `description` | ['string', 'null'] | false | 페인트 프로젝트 설명 |
| `duration` | integer | true | 페인트 프로젝트 총 길이 \(밀리초\) |
| `framerate` | number | true | 프레임레이트 \(초당 프레임\) |
| `positionX` | number | true | 현재 편집 화면의 X 위치 |
| `positionY` | number | true | 현재 편집 화면의 Y 위치 |
| `zoomLevel` | number | true | 현재 편집 화면의 확대/축소 수준 |
| `currentTime` | integer | true | 현재 타임라인 위치 \(밀리초\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "userId": "example_value",
  "name": "example_value",
  "description": "example_value",
  "duration": 0,
  "framerate": 0.0,
  "positionX": 0.0,
  "positionY": 0.0,
  "zoomLevel": 0.0,
  "currentTime": 0,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 페인트 프로젝트를 찾을 수 없음


---

<h3 id='delete-magic-paint-paint-projects-id-'></h3>

### DELETE /magic-paint/paint-projects/{id}

**페인트 프로젝트 삭제**

특정 ID의 페인트 프로젝트를 삭제합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 삭제할 페인트 프로젝트의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `204`

**설명**: 페인트 프로젝트 삭제 성공 (No Content)


**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 페인트 프로젝트를 찾을 수 없음


---

## User

사용자 관련 API

<h3 id='get-tokens'></h3>

### GET /tokens

**사용자 토큰 정보 조회**

현재 사용자가 사용할 수 있는 토큰 정보를 조회합니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 토큰 정보 조회 성공


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `resultCode` | integer | true | 작업 결과 코드 |
| `errorString` | string | true | 에러 메시지 |
| `result` | object | true | 결과 정보 |
| `result.availableTokenAmount` | integer | true | 옵션을 만족하는 사용 가능한 토큰의 합 |
| `result.tokens[]` | array&lt;object&gt; | true | 토큰 목록 |
| `result.tokens[].tokenId` | integer | true | 토큰 ID |
| `result.tokens[].userId` | ['integer', 'null'] | false | 사용자 ID |
| `result.tokens[].groupId` | integer | true | 그룹 ID |
| `result.tokens[].planOrderId` | integer | true | 주문 ID |
| `result.tokens[].planId` | integer | true | 요금제 ID |
| `result.tokens[].remainingTokens` | integer | true | 잔여 토큰 |
| `result.tokens[].expirationDate` | string | true | 만료일 |


**Content Type**: application/json


**예시:**

```json
{
  "resultCode": 0,
  "errorString": "example_value",
  "result": {
    "availableTokenAmount": 0,
    "tokens": [
      {
        "tokenId": 0,
        "userId": 0,
        "groupId": 0,
        "planOrderId": 0,
        "planId": 0,
        "remainingTokens": 0,
        "expirationDate": "example_value"
      }
    ]
  }
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

## Static

정적 콘텐츠 제공 API

<h3 id='get-assets-year-month-day-assetid-filename-'></h3>

### GET /assets/{year}/{month}/{day}/{assetId}/{filename}

**정적 Asset 파일 서빙**

연도, 월, 일, Asset ID, 파일명을 기반으로 정적 파일을 서빙합니다. 예를 들어 `/assets/2025/5/1/3f42bac4-d1bb-4f04-afa6-fbb342d0fa79/thumb/0.png` 경로로 요청 시 파일을 반환합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `year` | string | true | Asset의 연도 \(예: '2025'\)\. |
| `month` | string | true | Asset의 월 \(예: '5'\)\. |
| `day` | string | true | Asset의 일 \(예: '1'\)\. |
| `assetId` | string | true | Asset의 고유 ID \(예: '3f42bac4\-d1bb\-4f04\-afa6\-fbb342d0fa79'\)\. |
| `filename` | string | true | 서빙할 파일의 이름 \(예: 'thumb/0\.png', '0\.png'\)\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 파일이 성공적으로 서빙되었습니다.


##### 응답 스키마

**타입**: string

**포맷**: binary



**Content Type**: application/octet-stream


**예시:**

```json
"example_value"
```



**상태 코드**: `404`

**설명**: 파일을 찾을 수 없습니다.


**상태 코드**: `500`

**설명**: 파일 서빙 중 서버 오류가 발생했습니다.


---

## Resources

외부 리소스 관련 API

<h3 id='get-resources-voices'></h3>

### GET /resources/voices

**음성 리소스 목록 조회**

Magic Platform으로부터 음성 리소스 목록을 가져옵니다.

#### 요청 파라미터


##### 쿼리 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `cursorTitle` | string | false | 마지막으로 조회한 음성의 제목 \(커서 기반 페이징용\) |
| `cursorId` | integer | false | 마지막으로 조회한 음성의 ID \(커서 기반 페이징용\) |
| `limit` | integer | false | 한 번에 조회할 음성 개수 |
| `searchKeyword` | string | false | 검색 키워드 \(음성 정보 또는 태그\) |
| `filterTags` | string | false | 쉼표\(,\)로 구분된 필터 태그 목록 |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 음성 리소스 목록 조회 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `data[]` | array&lt;object&gt; | false | 음성 리소스 목록 |
| `data[].id` | integer | false | 음성 리소스 ID |
| `data[].voiceTitle` | string | false | 음성 제목 |
| `data[].voiceInfo` | string | false | 음성 설명 정보 |
| `data[].voiceFilePath` | string | false | 음성 파일 경로 |
| `data[].voiceImageFile` | string | false | 음성 이미지 파일 경로 |
| `data[].voiceKey` | string | false | 음성 고유 키 |
| `data[].tags` | string | false | 음성에 연결된 태그 목록 \(쉼표로 구분\) |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회를 위한 커서 정보 |
| `cursor.cursorTitle` | string | false | 다음 조회 시작점의 음성 제목 |
| `cursor.cursorId` | integer | false | 다음 조회 시작점의 음성 ID |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**Content Type**: application/json


**예시:**

```json
{
  "data": [
    {
      "id": 0,
      "voiceTitle": "example_value",
      "voiceInfo": "example_value",
      "voiceFilePath": "example_value",
      "voiceImageFile": "example_value",
      "voiceKey": "example_value",
      "tags": "example_value"
    }
  ],
  "cursor": {
    "cursorTitle": "example_value",
    "cursorId": 0
  },
  "hasMore": false
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `500`

**설명**: 서버 오류


---

<h3 id='get-resources-voices-tags'></h3>

### GET /resources/voices/tags

**음성 리소스 태그 목록 조회**

Magic Platform으로부터 음성 리소스의 태그 목록을 가져옵니다.

#### 요청 파라미터


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 음성 리소스 태그 목록 조회 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `groupedTags` | object | false | 유형별로 그룹화된 태그 목록 |
| `groupedTags.button[]` | array&lt;object&gt; | false | 버튼 유형의 태그 목록 |
| `groupedTags.button[].id` | integer | false | 태그 ID |
| `groupedTags.button[].name` | string | false | 태그 이름 |
| `groupedTags.button[].type` | string | false | 태그 유형 \(button, lang, gen 등\) |
| `groupedTags.lang[]` | array&lt;object&gt; | false | 언어 유형의 태그 목록 |
| `groupedTags.lang[].id` | integer | false | 태그 ID |
| `groupedTags.lang[].name` | string | false | 태그 이름 |
| `groupedTags.lang[].type` | string | false | 태그 유형 \(button, lang, gen 등\) |
| `groupedTags.gen[]` | array&lt;object&gt; | false | 세대 유형의 태그 목록 |
| `groupedTags.gen[].id` | integer | false | 태그 ID |
| `groupedTags.gen[].name` | string | false | 태그 이름 |
| `groupedTags.gen[].type` | string | false | 태그 유형 \(button, lang, gen 등\) |
| `tags[]` | array&lt;object&gt; | false | 전체 태그 목록 |
| `tags[].id` | integer | false | 태그 ID |
| `tags[].name` | string | false | 태그 이름 |
| `tags[].type` | string | false | 태그 유형 \(button, lang, gen 등\) |


**Content Type**: application/json


**예시:**

```json
{
  "groupedTags": {
    "button": [
      {
        "id": 0,
        "name": "example_value",
        "type": "example_value"
      }
    ],
    "lang": [
      {
        "id": 0,
        "name": "example_value",
        "type": "example_value"
      }
    ],
    "gen": [
      {
        "id": 0,
        "name": "example_value",
        "type": "example_value"
      }
    ]
  },
  "tags": [
    {
      "id": 0,
      "name": "example_value",
      "type": "example_value"
    }
  ]
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `500`

**설명**: 서버 오류


---

## Cuts

컷 관리 관련 API

<h3 id='get-magic-paint-paint-projects-paint-project-id-paint-cuts'></h3>

### GET /magic-paint/paint-projects/{paint-project-id}/paint-cuts

**컷 목록 조회**

특정 캔버스에 속한 컷 목록을 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `paint-project-id` | integer | true | 조회할 컷의 프로젝트의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 컷 목록 조회 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `cuts[]` | array&lt;object&gt; | true | \- |
| `cuts[].id` | integer | true | 컷 고유 식별자 |
| `cuts[].canvasId` | integer | true | 속한 캔버스 ID |
| `cuts[].name` | string | true | 컷 이름 |
| `cuts[].startTime` | integer | true | 시작 시간 \(밀리초\) |
| `cuts[].endTime` | integer | true | 종료 시간 \(밀리초\) |
| `cuts[].duration` | integer | true | 컷 길이 \(밀리초\) |
| `cuts[].animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `cuts[].isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `cuts[].isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `cuts[].items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `cuts[].audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |
| `cuts[].createdAt` | string | true | 생성 일시 |
| `cuts[].updatedAt` | string | true | 최종 수정 일시 |


**Content Type**: application/json


**예시:**

```json
{
  "cuts": [
    {
      "id": 0,
      "canvasId": 0,
      "name": "example_value",
      "startTime": 0,
      "endTime": 0,
      "duration": 0,
      "animation": {
        "property1": "value1",
        "property2": "value2"
      },
      "isLocked": false,
      "isHidden": false,
      "items": {
        "property1": "value1",
        "property2": "value2"
      },
      "audioItems": {
        "property1": "value1",
        "property2": "value2"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ]
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 캔버스를 찾을 수 없음


---

<h3 id='post-magic-paint-paint-projects-paint-project-id-paint-cuts'></h3>

### POST /magic-paint/paint-projects/{paint-project-id}/paint-cuts

**컷 생성**

새로운 컷을 생성합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `paint-project-id` | integer | true | 생성할 컷의 프로젝트의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `canvasId` | integer | true | 속한 캔버스 ID |
| `name` | string | false | 컷 이름 |
| `startTime` | integer | false | 시작 시간 \(밀리초\) |
| `endTime` | integer | false | 종료 시간 \(밀리초\) |
| `duration` | integer | false | 컷 길이 \(밀리초\) |
| `animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |


**예시:**

```json
{
  "canvasId": 0,
  "name": "example_value",
  "startTime": 0,
  "endTime": 0,
  "duration": 0,
  "animation": {
    "property1": "value1",
    "property2": "value2"
  },
  "isLocked": false,
  "isHidden": false,
  "items": {
    "property1": "value1",
    "property2": "value2"
  },
  "audioItems": {
    "property1": "value1",
    "property2": "value2"
  }
}
```

#### 응답


**상태 코드**: `201`

**설명**: 컷 생성 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 컷 고유 식별자 |
| `canvasId` | integer | true | 속한 캔버스 ID |
| `name` | string | true | 컷 이름 |
| `startTime` | integer | true | 시작 시간 \(밀리초\) |
| `endTime` | integer | true | 종료 시간 \(밀리초\) |
| `duration` | integer | true | 컷 길이 \(밀리초\) |
| `animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "canvasId": 0,
  "name": "example_value",
  "startTime": 0,
  "endTime": 0,
  "duration": 0,
  "animation": {
    "property1": "value1",
    "property2": "value2"
  },
  "isLocked": false,
  "isHidden": false,
  "items": {
    "property1": "value1",
    "property2": "value2"
  },
  "audioItems": {
    "property1": "value1",
    "property2": "value2"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='put-magic-paint-paint-projects-paint-project-id-paint-cuts'></h3>

### PUT /magic-paint/paint-projects/{paint-project-id}/paint-cuts

**컷 목록 일괄 업데이트**

여러 컷을 한 번에 업데이트합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `paint-project-id` | integer | true | 업데이트 할 컷의 프로젝트의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `cuts[]` | array&lt;object&gt; | true | \- |
| `cuts[].id` | integer | false | 업데이트할 컷 ID \(PUT /cuts 요청 시 필수\) |
| `cuts[].canvasId` | integer | false | 속한 캔버스 ID |
| `cuts[].name` | string | false | 컷 이름 |
| `cuts[].startTime` | integer | false | 시작 시간 \(밀리초\) |
| `cuts[].endTime` | integer | false | 종료 시간 \(밀리초\) |
| `cuts[].duration` | integer | false | 컷 길이 \(밀리초\) |
| `cuts[].animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `cuts[].isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `cuts[].isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `cuts[].items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `cuts[].audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |


**예시:**

```json
{
  "cuts": [
    {
      "id": 0,
      "canvasId": 0,
      "name": "example_value",
      "startTime": 0,
      "endTime": 0,
      "duration": 0,
      "animation": {
        "property1": "value1",
        "property2": "value2"
      },
      "isLocked": false,
      "isHidden": false,
      "items": {
        "property1": "value1",
        "property2": "value2"
      },
      "audioItems": {
        "property1": "value1",
        "property2": "value2"
      }
    }
  ]
}
```

#### 응답


**상태 코드**: `200`

**설명**: 컷 목록 업데이트 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `cuts[]` | array&lt;object&gt; | true | \- |
| `cuts[].id` | integer | true | 컷 고유 식별자 |
| `cuts[].canvasId` | integer | true | 속한 캔버스 ID |
| `cuts[].name` | string | true | 컷 이름 |
| `cuts[].startTime` | integer | true | 시작 시간 \(밀리초\) |
| `cuts[].endTime` | integer | true | 종료 시간 \(밀리초\) |
| `cuts[].duration` | integer | true | 컷 길이 \(밀리초\) |
| `cuts[].animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `cuts[].isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `cuts[].isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `cuts[].items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `cuts[].audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |
| `cuts[].createdAt` | string | true | 생성 일시 |
| `cuts[].updatedAt` | string | true | 최종 수정 일시 |


**Content Type**: application/json


**예시:**

```json
{
  "cuts": [
    {
      "id": 0,
      "canvasId": 0,
      "name": "example_value",
      "startTime": 0,
      "endTime": 0,
      "duration": 0,
      "animation": {
        "property1": "value1",
        "property2": "value2"
      },
      "isLocked": false,
      "isHidden": false,
      "items": {
        "property1": "value1",
        "property2": "value2"
      },
      "audioItems": {
        "property1": "value1",
        "property2": "value2"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ]
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


---

<h3 id='get-magic-paint-paint-projects-paint-project-id-paint-cuts-paint-cut-id-'></h3>

### GET /magic-paint/paint-projects/{paint-project-id}/paint-cuts/{paint-cut-id}

**단일 컷 조회**

특정 ID의 컷 정보를 조회합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `paint-project-id` | integer | true | 조회할 컷의 프로젝트의 ID |
| `paint-cut-id` | integer | true | 조회할 컷의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `200`

**설명**: 컷 조회 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 컷 고유 식별자 |
| `canvasId` | integer | true | 속한 캔버스 ID |
| `name` | string | true | 컷 이름 |
| `startTime` | integer | true | 시작 시간 \(밀리초\) |
| `endTime` | integer | true | 종료 시간 \(밀리초\) |
| `duration` | integer | true | 컷 길이 \(밀리초\) |
| `animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "canvasId": 0,
  "name": "example_value",
  "startTime": 0,
  "endTime": 0,
  "duration": 0,
  "animation": {
    "property1": "value1",
    "property2": "value2"
  },
  "isLocked": false,
  "isHidden": false,
  "items": {
    "property1": "value1",
    "property2": "value2"
  },
  "audioItems": {
    "property1": "value1",
    "property2": "value2"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 컷을 찾을 수 없음


---

<h3 id='put-magic-paint-paint-projects-paint-project-id-paint-cuts-paint-cut-id-'></h3>

### PUT /magic-paint/paint-projects/{paint-project-id}/paint-cuts/{paint-cut-id}

**단일 컷 업데이트**

특정 ID의 컷 정보를 업데이트합니다. 요청된 필드만 업데이트됩니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `paint-project-id` | integer | true | 업데이트 할 컷의 프로젝트의 ID |
| `paint-cut-id` | integer | true | 업데이트 할 컷의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청 본문

**필수**: 예


**Content Type**: application/json

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 업데이트할 컷 ID \(PUT /cuts 요청 시 필수\) |
| `canvasId` | integer | false | 속한 캔버스 ID |
| `name` | string | false | 컷 이름 |
| `startTime` | integer | false | 시작 시간 \(밀리초\) |
| `endTime` | integer | false | 종료 시간 \(밀리초\) |
| `duration` | integer | false | 컷 길이 \(밀리초\) |
| `animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |


**예시:**

```json
{
  "id": 0,
  "canvasId": 0,
  "name": "example_value",
  "startTime": 0,
  "endTime": 0,
  "duration": 0,
  "animation": {
    "property1": "value1",
    "property2": "value2"
  },
  "isLocked": false,
  "isHidden": false,
  "items": {
    "property1": "value1",
    "property2": "value2"
  },
  "audioItems": {
    "property1": "value1",
    "property2": "value2"
  }
}
```

#### 응답


**상태 코드**: `200`

**설명**: 컷 업데이트 성공


##### 응답 스키마

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 컷 고유 식별자 |
| `canvasId` | integer | true | 속한 캔버스 ID |
| `name` | string | true | 컷 이름 |
| `startTime` | integer | true | 시작 시간 \(밀리초\) |
| `endTime` | integer | true | 종료 시간 \(밀리초\) |
| `duration` | integer | true | 컷 길이 \(밀리초\) |
| `animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**Content Type**: application/json


**예시:**

```json
{
  "id": 0,
  "canvasId": 0,
  "name": "example_value",
  "startTime": 0,
  "endTime": 0,
  "duration": 0,
  "animation": {
    "property1": "value1",
    "property2": "value2"
  },
  "isLocked": false,
  "isHidden": false,
  "items": {
    "property1": "value1",
    "property2": "value2"
  },
  "audioItems": {
    "property1": "value1",
    "property2": "value2"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```



**상태 코드**: `400`

**설명**: 잘못된 요청 데이터


##### 응답 헤더

| 이름 | 타입 | 설명 |
|------|------|------|
| `Content-Type` | string | \- |


##### 응답 스키마

**타입**: string

**설명**: 잘못된 요청 데이터 상세



**Content Type**: text/plain


**예시:**

```json
"example_value"
```



**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 컷을 찾을 수 없음


---

<h3 id='delete-magic-paint-paint-projects-paint-project-id-paint-cuts-paint-cut-id-'></h3>

### DELETE /magic-paint/paint-projects/{paint-project-id}/paint-cuts/{paint-cut-id}

**단일 컷 삭제**

특정 ID의 컷을 삭제합니다.

#### 요청 파라미터


##### 경로 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `paint-project-id` | integer | true | 삭제할 컷의 프로젝트의 ID |
| `paint-cut-id` | integer | true | 삭제할 컷의 ID |


##### 헤더 파라미터

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `Authorization` | string | true | Bearer token for authentication\. |

#### 요청


#### 응답


**상태 코드**: `204`

**설명**: 컷 삭제 성공 (No Content)


**상태 코드**: `401`

**설명**: 인증 실패


**상태 코드**: `403`

**설명**: 권한 없음


**상태 코드**: `404`

**설명**: 컷을 찾을 수 없음


---

## 스키마

API에서 사용되는 데이터 모델 스키마입니다.


### Asset

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | string | true | Asset 고유 식별자\(ID\) |
| `uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `name` | string | true | Asset 이름 |
| `src` | ['string', 'null'] | true | Asset 소스 URL |
| `size` | integer | true | Asset 파일 크기\(바이트\) |
| `width` | integer | true | Asset 너비\(픽셀\) |
| `height` | integer | true | Asset 높이\(픽셀\) |
| `duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `mimeType` | string | true | Asset의 MIME 타입 |
| `metadata` | object | false | 파일 메타데이터 정보 |
| `metadata.width` | integer | false | 원본 파일의 너비\(픽셀\) |
| `metadata.height` | integer | false | 원본 파일의 높이\(픽셀\) |
| `metadata.duration` | ['number', 'null'] | false | 원본 파일의 길이\(초\) |
| `metadata.mimeType` | string | false | 원본 파일의 MIME 타입 |
| `metadata.fps` | ['string', 'null'] | false | 비디오의 초당 프레임 수 \(분수 형태\) |
| `thumbnailSrc` | string | true | Asset 썸네일 URL |
| `isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `createdAt` | string | true | 생성 시간 |
| `updatedAt` | string | true | 수정 시간 |


**예시:**

```json
{
  "id": "example_value",
  "uiRequestId": 0,
  "type": "image",
  "name": "example_value",
  "src": "example_value",
  "size": 0,
  "width": 0,
  "height": 0,
  "duration": 0.0,
  "mimeType": "example_value",
  "metadata": {
    "width": 0,
    "height": 0,
    "duration": 0.0,
    "mimeType": "example_value",
    "fps": "example_value"
  },
  "thumbnailSrc": "example_value",
  "isFavorite": 0,
  "createdAt": "example_value",
  "updatedAt": "example_value"
}
```

### AssetResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `asset` | object | false | \- |
| `asset.id` | string | true | Asset 고유 식별자\(ID\) |
| `asset.uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `asset.type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `asset.name` | string | true | Asset 이름 |
| `asset.src` | ['string', 'null'] | true | Asset 소스 URL |
| `asset.size` | integer | true | Asset 파일 크기\(바이트\) |
| `asset.width` | integer | true | Asset 너비\(픽셀\) |
| `asset.height` | integer | true | Asset 높이\(픽셀\) |
| `asset.duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `asset.mimeType` | string | true | Asset의 MIME 타입 |
| `asset.metadata` | object | false | 파일 메타데이터 정보 |
| `asset.metadata.width` | integer | false | 원본 파일의 너비\(픽셀\) |
| `asset.metadata.height` | integer | false | 원본 파일의 높이\(픽셀\) |
| `asset.metadata.duration` | ['number', 'null'] | false | 원본 파일의 길이\(초\) |
| `asset.metadata.mimeType` | string | false | 원본 파일의 MIME 타입 |
| `asset.metadata.fps` | ['string', 'null'] | false | 비디오의 초당 프레임 수 \(분수 형태\) |
| `asset.thumbnailSrc` | string | true | Asset 썸네일 URL |
| `asset.isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `asset.createdAt` | string | true | 생성 시간 |
| `asset.updatedAt` | string | true | 수정 시간 |


**예시:**

```json
{
  "asset": {
    "id": "example_value",
    "uiRequestId": 0,
    "type": "image",
    "name": "example_value",
    "src": "example_value",
    "size": 0,
    "width": 0,
    "height": 0,
    "duration": 0.0,
    "mimeType": "example_value",
    "metadata": {
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "fps": "example_value"
    },
    "thumbnailSrc": "example_value",
    "isFavorite": 0,
    "createdAt": "example_value",
    "updatedAt": "example_value"
  }
}
```

### AssetListResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `total` | integer | true | 총 Asset 개수 |
| `assets[]` | array&lt;Asset&gt; | true | \- |
| `assets[].id` | string | true | Asset 고유 식별자\(ID\) |
| `assets[].uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `assets[].type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `assets[].name` | string | true | Asset 이름 |
| `assets[].src` | ['string', 'null'] | true | Asset 소스 URL |
| `assets[].size` | integer | true | Asset 파일 크기\(바이트\) |
| `assets[].width` | integer | true | Asset 너비\(픽셀\) |
| `assets[].height` | integer | true | Asset 높이\(픽셀\) |
| `assets[].duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `assets[].mimeType` | string | true | Asset의 MIME 타입 |
| `assets[].metadata` | object | false | 파일 메타데이터 정보 |
| `assets[].thumbnailSrc` | string | true | Asset 썸네일 URL |
| `assets[].isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `assets[].createdAt` | string | true | 생성 시간 |
| `assets[].updatedAt` | string | true | 수정 시간 |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회용 커서 정보\. 더 이상 불러올 데이터가 없으면 null을 반환 |
| `cursor.cursorCreatedAt` | string | false | 다음 조회 시 created\_at < 이 값 조건에 사용 |
| `cursor.cursorId` | string | false | 다음 조회 시 \(created\_at = created\_at\_cursor AND id < 이 값\) 조건에 사용 |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**예시:**

```json
{
  "total": 0,
  "assets": [
    {
      "id": "example_value",
      "uiRequestId": 0,
      "type": "image",
      "name": "example_value",
      "src": "example_value",
      "size": 0,
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "metadata": {
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "fps": "example_value"
      },
      "thumbnailSrc": "example_value",
      "isFavorite": 0,
      "createdAt": "example_value",
      "updatedAt": "example_value"
    }
  ],
  "cursor": {
    "cursorCreatedAt": "example_value",
    "cursorId": "example_value"
  },
  "hasMore": false
}
```

### ErrorResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `message` | string | false | 에러 메시지 |


**예시:**

```json
{
  "message": "example_value"
}
```

### TaskIdResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 작업아이디 |


**예시:**

```json
{
  "id": 0
}
```

### TaskStatusResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업아이디 |
| `status` | string | true | 작업상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `percent` | integer | false | 작업 진행도 |
| `result` | object | false | 작업 결과 데이터 \(completed 상태일 때만 존재\) 가능한 타입: ImageGeneration, ImageConstancy, VideoGenerationGen3, VideoGenerationKling, VoiceGenerationClova (discriminator: type) |
| `errorString` | string | false | 에러 메시지 \(failed 상태일 때만 존재\) |


**예시:**

```json
{
  "id": 0,
  "status": "pending",
  "percent": 0,
  "result": {
    "type": "ImageGeneration",
    "generatedImageList": [
      "example_value"
    ],
    "assets": [
      {
        "id": "example_value",
        "uiRequestId": 0,
        "type": "image",
        "name": "example_value",
        "src": "example_value",
        "size": 0,
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "metadata": {
          "width": 0,
          "height": 0,
          "duration": 0.0,
          "mimeType": "example_value",
          "fps": "example_value"
        },
        "thumbnailSrc": "example_value",
        "isFavorite": 0,
        "createdAt": "example_value",
        "updatedAt": "example_value"
      }
    ]
  },
  "errorString": "example_value"
}
```

### ImageGenerationResult

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | false | \-<br>(Enum: `ImageGeneration`) |
| `generatedImageList[]` | array&lt;string&gt; | true | 생성된 이미지 URL 목록 |
| `assets[]` | array&lt;Asset&gt; | false | \- |
| `assets[].id` | string | true | Asset 고유 식별자\(ID\) |
| `assets[].uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `assets[].type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `assets[].name` | string | true | Asset 이름 |
| `assets[].src` | ['string', 'null'] | true | Asset 소스 URL |
| `assets[].size` | integer | true | Asset 파일 크기\(바이트\) |
| `assets[].width` | integer | true | Asset 너비\(픽셀\) |
| `assets[].height` | integer | true | Asset 높이\(픽셀\) |
| `assets[].duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `assets[].mimeType` | string | true | Asset의 MIME 타입 |
| `assets[].metadata` | object | false | 파일 메타데이터 정보 |
| `assets[].thumbnailSrc` | string | true | Asset 썸네일 URL |
| `assets[].isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `assets[].createdAt` | string | true | 생성 시간 |
| `assets[].updatedAt` | string | true | 수정 시간 |


**예시:**

```json
{
  "type": "ImageGeneration",
  "generatedImageList": [
    "example_value"
  ],
  "assets": [
    {
      "id": "example_value",
      "uiRequestId": 0,
      "type": "image",
      "name": "example_value",
      "src": "example_value",
      "size": 0,
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "metadata": {
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "fps": "example_value"
      },
      "thumbnailSrc": "example_value",
      "isFavorite": 0,
      "createdAt": "example_value",
      "updatedAt": "example_value"
    }
  ]
}
```

### ImageConstancyResult

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | false | \-<br>(Enum: `ImageConstancy`) |
| `generatedImageList[]` | array&lt;string&gt; | true | 생성된 이미지 URL 목록 |
| `assets[]` | array&lt;Asset&gt; | false | \- |
| `assets[].id` | string | true | Asset 고유 식별자\(ID\) |
| `assets[].uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `assets[].type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `assets[].name` | string | true | Asset 이름 |
| `assets[].src` | ['string', 'null'] | true | Asset 소스 URL |
| `assets[].size` | integer | true | Asset 파일 크기\(바이트\) |
| `assets[].width` | integer | true | Asset 너비\(픽셀\) |
| `assets[].height` | integer | true | Asset 높이\(픽셀\) |
| `assets[].duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `assets[].mimeType` | string | true | Asset의 MIME 타입 |
| `assets[].metadata` | object | false | 파일 메타데이터 정보 |
| `assets[].thumbnailSrc` | string | true | Asset 썸네일 URL |
| `assets[].isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `assets[].createdAt` | string | true | 생성 시간 |
| `assets[].updatedAt` | string | true | 수정 시간 |


**예시:**

```json
{
  "type": "ImageConstancy",
  "generatedImageList": [
    "example_value"
  ],
  "assets": [
    {
      "id": "example_value",
      "uiRequestId": 0,
      "type": "image",
      "name": "example_value",
      "src": "example_value",
      "size": 0,
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "metadata": {
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "fps": "example_value"
      },
      "thumbnailSrc": "example_value",
      "isFavorite": 0,
      "createdAt": "example_value",
      "updatedAt": "example_value"
    }
  ]
}
```

### VideoGenerationGen3Result

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | false | \-<br>(Enum: `VideoGenerationGen3`) |
| `generatedVideoList[]` | array&lt;string&gt; | true | 생성된 비디오 URL 목록 |
| `assets[]` | array&lt;Asset&gt; | false | \- |
| `assets[].id` | string | true | Asset 고유 식별자\(ID\) |
| `assets[].uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `assets[].type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `assets[].name` | string | true | Asset 이름 |
| `assets[].src` | ['string', 'null'] | true | Asset 소스 URL |
| `assets[].size` | integer | true | Asset 파일 크기\(바이트\) |
| `assets[].width` | integer | true | Asset 너비\(픽셀\) |
| `assets[].height` | integer | true | Asset 높이\(픽셀\) |
| `assets[].duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `assets[].mimeType` | string | true | Asset의 MIME 타입 |
| `assets[].metadata` | object | false | 파일 메타데이터 정보 |
| `assets[].thumbnailSrc` | string | true | Asset 썸네일 URL |
| `assets[].isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `assets[].createdAt` | string | true | 생성 시간 |
| `assets[].updatedAt` | string | true | 수정 시간 |


**예시:**

```json
{
  "type": "VideoGenerationGen3",
  "generatedVideoList": [
    "example_value"
  ],
  "assets": [
    {
      "id": "example_value",
      "uiRequestId": 0,
      "type": "image",
      "name": "example_value",
      "src": "example_value",
      "size": 0,
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "metadata": {
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "fps": "example_value"
      },
      "thumbnailSrc": "example_value",
      "isFavorite": 0,
      "createdAt": "example_value",
      "updatedAt": "example_value"
    }
  ]
}
```

### VideoGenerationKlingResult

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | false | \-<br>(Enum: `VideoGenerationKling`) |
| `generatedVideoList[]` | array&lt;string&gt; | true | 생성된 비디오 URL 목록 |
| `assets[]` | array&lt;Asset&gt; | false | \- |
| `assets[].id` | string | true | Asset 고유 식별자\(ID\) |
| `assets[].uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `assets[].type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `assets[].name` | string | true | Asset 이름 |
| `assets[].src` | ['string', 'null'] | true | Asset 소스 URL |
| `assets[].size` | integer | true | Asset 파일 크기\(바이트\) |
| `assets[].width` | integer | true | Asset 너비\(픽셀\) |
| `assets[].height` | integer | true | Asset 높이\(픽셀\) |
| `assets[].duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `assets[].mimeType` | string | true | Asset의 MIME 타입 |
| `assets[].metadata` | object | false | 파일 메타데이터 정보 |
| `assets[].thumbnailSrc` | string | true | Asset 썸네일 URL |
| `assets[].isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `assets[].createdAt` | string | true | 생성 시간 |
| `assets[].updatedAt` | string | true | 수정 시간 |


**예시:**

```json
{
  "type": "VideoGenerationKling",
  "generatedVideoList": [
    "example_value"
  ],
  "assets": [
    {
      "id": "example_value",
      "uiRequestId": 0,
      "type": "image",
      "name": "example_value",
      "src": "example_value",
      "size": 0,
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "metadata": {
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "fps": "example_value"
      },
      "thumbnailSrc": "example_value",
      "isFavorite": 0,
      "createdAt": "example_value",
      "updatedAt": "example_value"
    }
  ]
}
```

### VoiceGenerationClovaResult

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | false | \-<br>(Enum: `VoiceGenerationClova`) |
| `generatedVoiceList[]` | array&lt;string&gt; | true | \- |
| `assets[]` | array&lt;Asset&gt; | false | \- |
| `assets[].id` | string | true | Asset 고유 식별자\(ID\) |
| `assets[].uiRequestId` | ['integer', 'null'] | false | UI 요청 ID |
| `assets[].type` | string | true | Asset 타입 \(이미지, 비디오, 오디오 등\)<br>(Enum: `image`, `video`, `audio`) |
| `assets[].name` | string | true | Asset 이름 |
| `assets[].src` | ['string', 'null'] | true | Asset 소스 URL |
| `assets[].size` | integer | true | Asset 파일 크기\(바이트\) |
| `assets[].width` | integer | true | Asset 너비\(픽셀\) |
| `assets[].height` | integer | true | Asset 높이\(픽셀\) |
| `assets[].duration` | ['number', 'null'] | false | 미디어 길이\(초\), video/audio 타입에서 사용 |
| `assets[].mimeType` | string | true | Asset의 MIME 타입 |
| `assets[].metadata` | object | false | 파일 메타데이터 정보 |
| `assets[].thumbnailSrc` | string | true | Asset 썸네일 URL |
| `assets[].isFavorite` | integer | false | 즐겨찾기 여부 \(0: 아님, 1: 즐겨찾기\)<br>(Enum: `0`, `1`) |
| `assets[].createdAt` | string | true | 생성 시간 |
| `assets[].updatedAt` | string | true | 수정 시간 |


**예시:**

```json
{
  "type": "VoiceGenerationClova",
  "generatedVoiceList": [
    "example_value"
  ],
  "assets": [
    {
      "id": "example_value",
      "uiRequestId": 0,
      "type": "image",
      "name": "example_value",
      "src": "example_value",
      "size": 0,
      "width": 0,
      "height": 0,
      "duration": 0.0,
      "mimeType": "example_value",
      "metadata": {
        "width": 0,
        "height": 0,
        "duration": 0.0,
        "mimeType": "example_value",
        "fps": "example_value"
      },
      "thumbnailSrc": "example_value",
      "isFavorite": 0,
      "createdAt": "example_value",
      "updatedAt": "example_value"
    }
  ]
}
```

### ImageConstancyParams

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `prompt` | string | true | 생성 프롬프트 |
| `styleIndex` | integer | false | 스타일 인덱스 |
| `matting` | boolean | false | 생성할 이미지 배경 투명 여부 |
| `width` | integer | true | 생성할 이미지 가로 픽셀 |
| `height` | integer | true | 생성할 이미지 세로 픽셀 |


**예시:**

```json
{
  "prompt": "seaside city",
  "styleIndex": 0,
  "matting": false,
  "width": 1152,
  "height": 768,
  "numImages": 2
}
```

### VideoGenerationGen3Params

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `promptText` | string | false | 생성 프롬프트 |
| `seed` | integer | false | 랜덤 시드 값 |
| `watermark` | boolean | false | 워터마크 여부 |
| `duration` | integer | false | 비디오 길이<br>(Enum: `5`, `10`) |
| `ratio` | string | false | 비디오 비율<br>(Enum: `1280:768`, `768:1280`) |


**예시:**

```json
{
  "promptText": "example_value",
  "seed": 0,
  "watermark": false,
  "duration": 5,
  "ratio": "1280:768"
}
```

### VideoGenerationKlingParams

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `modelName` | string | false | Kling 모델 이름 kling\-v1\-5 만 camera control 사용 가능<br>(Enum: `kling-v1`, `kling-v1-5`, `kling-v1-6`) |
| `prompt` | string | true | 비디오 생성 프롬프트 |
| `negativePrompt` | string | false | 제외할 내용 프롬프트 |
| `cfgScale` | number | false | 비디오 생성의 유연성 \(값이 높을수록 모델의 유연성이 낮고 사용자 프롬프트와의 관련성이 강해짐\) |
| `mode` | string | false | 비디오 생성 모드 pro만 camera control 사용 가능<br>(Enum: `std`, `pro`) |
| `dynamicMasks[]` | array&lt;object&gt; | false | 동적 브러시 설정 리스트 |
| `dynamicMasks[].trajectories` | array | false | 모션 궤적 좌표 리스트 \(5초 동영상을 위해 최대 77개\) |
| `cameraControl` | object | false | 카메라 움직임 제어 조건 |
| `cameraControl.type` | string | false | 사전 정의된 카메라 움직임 유형<br>(Enum: `simple`, `down_back`, `forward_up`, `right_turn_forward`, `left_turn_forward`) |
| `cameraControl.config` | object | false | 카메라 이동 설정 \(type이 simple일 경우만 사용\) |
| `cameraControl.config.horizontal` | number | false | 수평이동 \(음수 값은 왼쪽으로, 양수 값은 오른쪽으로 이동\) |
| `cameraControl.config.vertical` | number | false | 수직이동 \(음수 값은 하향 이동, 양수 값은 상향 이동\) |
| `cameraControl.config.pan` | number | false | 수평면에서의 카메라 회전 \(음수 값은 y축 왼쪽 회전, 양수 값은 y축 오른쪽 회전\) |
| `cameraControl.config.tilt` | number | false | 수직면 회전 \(음수 값은 x축 하향 회전, 양수 값은 x축 상향 회전\) |
| `cameraControl.config.roll` | number | false | 카메라 롤링 \(음수 값은 z축 반시계 방향, 양수 값은 z축 시계 방향\) |
| `cameraControl.config.zoom` | number | false | 줌 \(음수 값은 시야 좁아짐, 양수 값은 시야 넓어짐\) |
| `duration` | string | false | 비디오 길이 \(초\)<br>(Enum: `5`, `10`) |


**예시:**

```json
{
  "modelName": "kling-v1",
  "prompt": "example_value",
  "negativePrompt": "example_value",
  "cfgScale": 0.0,
  "mode": "std",
  "dynamicMasks": [
    {
      "trajectories": [
        {
          "x": 0,
          "y": 0
        }
      ]
    }
  ],
  "cameraControl": {
    "type": "simple",
    "config": {
      "horizontal": 0.0,
      "vertical": 0.0,
      "pan": 0.0,
      "tilt": 0.0,
      "roll": 0.0,
      "zoom": 0.0
    }
  },
  "duration": "5"
}
```

### ImageGenerationParams

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `prompt` | string | true | 프롬프트 |
| `negativePrompt` | string | false | 네거티브 프롬프트 |
| `guidanceScale` | number | false | Guidance Scale |
| `steps` | integer | false | Inference Steps |
| `refinerStrength` | number | false | Refiner Strength |
| `seed` | integer | false | Seed |
| `numImages` | integer | false | 생성할 이미지 수 |
| `width` | integer | false | 생성할 이미지 너비 \(width \* height 의 픽셀 수가 512\*512보다 커야하고 4096\*4096보다 작아야 함\) |
| `height` | integer | false | 생성할 이미지 높이 \(width \* height 의 픽셀 수가 512\*512보다 커야하고 4096\*4096보다 작아야 함\) |
| `mode` | integer | false | 모드 \(0: text2img, 1: img2img\)<br>(Enum: `0`, `1`) |
| `modelType` | integer | false | 모델 타입 \(0: SDXL, 1: Flux\.1 dev\)<br>(Enum: `0`, `1`) |
| `loraModel` | integer | false | LoRA 모델 타입 \(Flux\.1\-dev 모델용, \-1: None, 0~7: 각 모델\) 기본값 \-1: None 0: "Flux\.1 D Painting Style \- v1\.0" 1: "Pen drawing \+ watercolor style" 2: "FLUX \- Oil painting" 3: "Impressionist Landscape LoRA for Flux" 4: "35mm\-Photo" 5: "Eldritch Watercolor for Flux" 6: "Flux Dreamscape" 7: "painters\_sketchbook"<br>(Enum: `-1`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`) |
| `loraModelScale` | number | false | LoRA 모델 스케일 |
| `loraModelSub` | integer | false | Sub LoRA 모델 타입 \(loraModel과 동일한 범위\)<br>(Enum: `-1`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`) |
| `loraModelSubScale` | number | false | Sub LoRA 모델 스케일 |


**예시:**

```json
{
  "prompt": "example_value",
  "negativePrompt": "example_value",
  "guidanceScale": 0.0,
  "steps": 1,
  "refinerStrength": 0.0,
  "seed": 0,
  "numImages": 1,
  "width": 0,
  "height": 0,
  "mode": 0,
  "modelType": 0,
  "loraModel": -1,
  "loraModelScale": 0.0,
  "loraModelSub": -1,
  "loraModelSubScale": 0.0
}
```

### VoiceGenerationClovaParams

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `speaker` | string | true | 음성 합성 시 사용할 목소리 종류 |
| `text` | string | true | 음성으로 변환할 텍스트 \(UTF\-8 인코딩\)\. 언어별 최대 글자 수: 한국어, 일본어, 중국어, 대만어는 2,000자, 영어, 스페인어는 3,000자 |
| `volume` | integer | false | 음성 크기: \-5~5 \(기본값: 0\)\. \-5: 0\.5배 작게, 0: 정상 크기, 5: 1\.5배 크게 |
| `speed` | integer | false | 음성 속도: \-5~10 \(기본값: 0\)\. \-5: 2\.0배 속도 \(빠르게\), 0: 원음의 속도, 10: 0\.5배 속도 \(느리게\) |
| `pitch` | integer | false | 음성 높낮이: \-5~5 \(기본값: 0\)\. \-5: 1\.2배 높게, 0: 정상 높낮이, 5: 0\.8배 낮게 |
| `emotion` | integer | false | 음성 감정 정도 \(지원 목소리: nara, vara, vmikyung, vdain, vyuna, vgoeun, vdaeseong\): 0~3 \(기본값: 0\)\. 0: 중립, 1: 슬픔, 2: 기쁨, 3: 분노 \(nara 미지원\)<br>(Enum: `0`, `1`, `2`, `3`) |
| `emotionStrength` | integer | false | 음성 감정 강도 \(지원 목소리: vara, vmikyung, vdain, vyuna, vgoeun, vdaeseong\): 0~2 \(기본값: 1\)\. 0: 약함, 1: 보통, 2: 강함<br>(Enum: `0`, `1`, `2`) |
| `format` | string | false | 음성 파일 형식<br>(Enum: `mp3`, `wav`) |
| `samplingRate` | integer | false | 음성의 샘플링 레이트 \(wav 형식만 지원\)\. 예외적으로 mijin은 16000 레이트만 지원<br>(Enum: `8000`, `16000`, `24000`, `48000`) |
| `alpha` | integer | false | 음색: \-5~5 \(기본값: 0\)\. 0보다 클 경우: 높은 음색, 0보다 작을 경우: 낮은 음색 |
| `endPitch` | integer | false | 음성의 끝음 처리 \(지원 목소리: clara, matt, meimei, liangliang, chiahua, kuanlin, carmen, jose, d\-로 시작하는 모든 목소리\): \-5~5 \(기본값: 0\)\. 0보다 클 경우: 높은 끝음, 0보다 작을 경우: 낮은 끝음 |


**예시:**

```json
{
  "speaker": "example_value",
  "text": "example_value",
  "volume": 0,
  "speed": 0,
  "pitch": 0,
  "emotion": 0,
  "emotionStrength": 0,
  "format": "mp3",
  "samplingRate": 8000,
  "alpha": 0,
  "endPitch": 0
}
```

### ImageGenerationFormData

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `file` | string | false | 이미지 파일 \(img2img 모드일 때 필수\) |
| `param` | object | true | JSON 문자열로 param 값에 전달 |
| `param.prompt` | string | true | 프롬프트 |
| `param.negativePrompt` | string | true | 네거티브 프롬프트 |
| `param.guidanceScale` | number | true | Guidance Scale |
| `param.steps` | integer | true | Inference Steps |
| `param.refinerStrength` | number | true | Refiner Strength |
| `param.seed` | integer | true | Seed |
| `param.numImages` | integer | true | 생성할 이미지 수 |
| `param.width` | integer | true | 생성할 이미지 너비 \(width \* height 의 픽셀 수가 512\*512보다 커야하고 4096\*4096보다 작아야 함\) |
| `param.height` | integer | true | 생성할 이미지 높이 \(width \* height 의 픽셀 수가 512\*512보다 커야하고 4096\*4096보다 작아야 함\) |
| `param.mode` | integer | true | 모드 \(0: text2img, 1: img2img\)<br>(Enum: `0`, `1`) |
| `param.modelType` | integer | true | 모델 타입 \(0: SDXL, 1: Flux\.1 dev\)<br>(Enum: `0`, `1`) |
| `param.loraModel` | integer | true | LoRA 모델 타입 \(Flux\.1\-dev 모델용, \-1: None, 0~7: 각 모델\) 기본값 \-1: None 0: "Flux\.1 D Painting Style \- v1\.0" 1: "Pen drawing \+ watercolor style" 2: "FLUX \- Oil painting" 3: "Impressionist Landscape LoRA for Flux" 4: "35mm\-Photo" 5: "Eldritch Watercolor for Flux" 6: "Flux Dreamscape" 7: "painters\_sketchbook"<br>(Enum: `-1`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`) |
| `param.loraModelScale` | number | true | LoRA 모델 스케일 |
| `param.loraModelSub` | integer | true | Sub LoRA 모델 타입 \(loraModel과 동일한 범위\)<br>(Enum: `-1`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`) |
| `param.loraModelSubScale` | number | true | Sub LoRA 모델 스케일 |
| `paintProjectId` | string | true | 프로젝트 ID |


**예시:**

```json
{
  "file": "example_value",
  "param": {
    "prompt": "example_value",
    "negativePrompt": "example_value",
    "guidanceScale": 0.0,
    "steps": 1,
    "refinerStrength": 0.0,
    "seed": 0,
    "numImages": 1,
    "width": 0,
    "height": 0,
    "mode": 0,
    "modelType": 0,
    "loraModel": -1,
    "loraModelScale": 0.0,
    "loraModelSub": -1,
    "loraModelSubScale": 0.0
  },
  "paintProjectId": "example_value"
}
```

### ImageConstancyFormData

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `styleFiles[]` | array&lt;string&gt; | true | 참조할 스타일 파일<br>용량: 25MB<br>확장자: 'jpg', 'jpeg', 'png'<br>최대 해상도: 3840x2160 |
| `param` | object | true | JSON 문자열로 param 값에 전달 |
| `param.prompt` | string | true | 생성 프롬프트 |
| `param.styleIndex` | integer | true | 스타일 인덱스 |
| `param.matting` | boolean | true | 생성할 이미지 배경 투명 여부 |
| `param.width` | integer | true | 생성할 이미지 가로 픽셀 |
| `param.height` | integer | true | 생성할 이미지 세로 픽셀 |
| `paintProjectId` | string | true | 프로젝트 ID |
| `numImages` | integer | false | 생성할 이미지 개수 |


**예시:**

```json
{
  "styleFiles": [
    "example_value"
  ],
  "param": {
    "prompt": "example_value",
    "styleIndex": 0,
    "matting": false,
    "width": 0,
    "height": 0
  },
  "paintProjectId": "example_value",
  "numImages": 1
}
```

### VideoGenerationKlingFormData

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `imageInputFile` | string | false | 대상 이미지<br>용량: 10MB 이하<br>확장자: 'jpg', 'jpeg', 'png'<br>해상도: 300x300 이상<br>비율: 1:2\.5 ~ 2\.5:1<br>\*imageInputFile이나 imageTailInputFile 둘 중 하나는 있어야 함 |
| `imageTailInputFile` | string | false | 대상 이미지<br>용량: 10MB 이하<br>확장자: 'jpg', 'jpeg', 'png'<br>해상도: 300x300 이상<br>비율: 1:2\.5 ~ 2\.5:1<br>\*imageInputFile이나 imageTailInputFile 둘 중 하나는 있어야 함 |
| `staticMaskInputFile` | string | false | 사용자가 모션 브러시를 사용하여 만든 마스크 이미지<br>확장자: 'jpg', 'jpeg', 'png'<br>image와 비율이 같아야 함<br>dynamic\_mask와 해상도가 일치해야 함 |
| `dynamicMaskInputFiles[]` | array&lt;string&gt; | false | param\.dynamicMasks\[\]\.trajectories와 순서 일치 필요<br>확장자: 'jpg', 'jpeg', 'png'<br>image와 비율이 같아야 함<br>static\_mask와 해상도가 일치해야 함 |
| `param` | object | false | JSON 문자열로 param 값에 전달 |
| `param.modelName` | string | false | Kling 모델 이름 kling\-v1\-5 만 camera control 사용 가능<br>(Enum: `kling-v1`, `kling-v1-5`, `kling-v1-6`) |
| `param.prompt` | string | true | 비디오 생성 프롬프트 |
| `param.negativePrompt` | string | false | 제외할 내용 프롬프트 |
| `param.cfgScale` | number | false | 비디오 생성의 유연성 \(값이 높을수록 모델의 유연성이 낮고 사용자 프롬프트와의 관련성이 강해짐\) |
| `param.mode` | string | false | 비디오 생성 모드 pro만 camera control 사용 가능<br>(Enum: `std`, `pro`) |
| `param.dynamicMasks[]` | array&lt;object&gt; | false | 동적 브러시 설정 리스트 |
| `param.dynamicMasks[].trajectories` | array | false | 모션 궤적 좌표 리스트 \(5초 동영상을 위해 최대 77개\) |
| `param.cameraControl` | object | false | 카메라 움직임 제어 조건 |
| `param.cameraControl.type` | string | false | 사전 정의된 카메라 움직임 유형<br>(Enum: `simple`, `down_back`, `forward_up`, `right_turn_forward`, `left_turn_forward`) |
| `param.cameraControl.config` | object | false | 카메라 이동 설정 \(type이 simple일 경우만 사용\) |
| `param.cameraControl.config.horizontal` | number | false | 수평이동 \(음수 값은 왼쪽으로, 양수 값은 오른쪽으로 이동\) |
| `param.cameraControl.config.vertical` | number | false | 수직이동 \(음수 값은 하향 이동, 양수 값은 상향 이동\) |
| `param.cameraControl.config.pan` | number | false | 수평면에서의 카메라 회전 \(음수 값은 y축 왼쪽 회전, 양수 값은 y축 오른쪽 회전\) |
| `param.cameraControl.config.tilt` | number | false | 수직면 회전 \(음수 값은 x축 하향 회전, 양수 값은 x축 상향 회전\) |
| `param.cameraControl.config.roll` | number | false | 카메라 롤링 \(음수 값은 z축 반시계 방향, 양수 값은 z축 시계 방향\) |
| `param.cameraControl.config.zoom` | number | false | 줌 \(음수 값은 시야 좁아짐, 양수 값은 시야 넓어짐\) |
| `param.duration` | string | false | 비디오 길이 \(초\)<br>(Enum: `5`, `10`) |
| `paintProjectId` | string | true | 프로젝트 ID |


**예시:**

```json
{
  "imageInputFile": "example_value",
  "imageTailInputFile": "example_value",
  "staticMaskInputFile": "example_value",
  "dynamicMaskInputFiles": [
    "example_value"
  ],
  "param": {
    "modelName": "kling-v1",
    "prompt": "example_value",
    "negativePrompt": "example_value",
    "cfgScale": 0.0,
    "mode": "std",
    "dynamicMasks": [
      {
        "trajectories": [
          {
            "x": 0,
            "y": 0
          }
        ]
      }
    ],
    "cameraControl": {
      "type": "simple",
      "config": {
        "horizontal": 0.0,
        "vertical": 0.0,
        "pan": 0.0,
        "tilt": 0.0,
        "roll": 0.0,
        "zoom": 0.0
      }
    },
    "duration": "5"
  },
  "paintProjectId": "example_value"
}
```

### VideoGenerationGen3FormData

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `file` | string | true | 참조 이미지 \(첫 프레임\) |
| `param` | object | false | JSON 문자열로 param 값에 전달 |
| `param.promptText` | string | false | 생성 프롬프트 |
| `param.seed` | integer | false | 랜덤 시드 값 |
| `param.watermark` | boolean | false | 워터마크 여부 |
| `param.duration` | integer | false | 비디오 길이<br>(Enum: `5`, `10`) |
| `param.ratio` | string | false | 비디오 비율<br>(Enum: `1280:768`, `768:1280`) |
| `paintProjectId` | string | true | 프로젝트 ID |
| `numVideos` | integer | false | 생성할 비디오 개수 |


**예시:**

```json
{
  "file": "example_value",
  "param": {
    "promptText": "example_value",
    "seed": 0,
    "watermark": false,
    "duration": 5,
    "ratio": "1280:768"
  },
  "paintProjectId": "example_value",
  "numVideos": 1
}
```

### VoiceGenerationClovaFormData

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `param` | object | true | JSON 문자열로 param 값에 전달 |
| `param.speaker` | string | true | 음성 합성 시 사용할 목소리 종류 |
| `param.text` | string | true | 음성으로 변환할 텍스트 \(UTF\-8 인코딩\)\. 언어별 최대 글자 수: 한국어, 일본어, 중국어, 대만어는 2,000자, 영어, 스페인어는 3,000자 |
| `param.volume` | integer | true | 음성 크기: \-5~5 \(기본값: 0\)\. \-5: 0\.5배 작게, 0: 정상 크기, 5: 1\.5배 크게 |
| `param.speed` | integer | true | 음성 속도: \-5~10 \(기본값: 0\)\. \-5: 2\.0배 속도 \(빠르게\), 0: 원음의 속도, 10: 0\.5배 속도 \(느리게\) |
| `param.pitch` | integer | true | 음성 높낮이: \-5~5 \(기본값: 0\)\. \-5: 1\.2배 높게, 0: 정상 높낮이, 5: 0\.8배 낮게 |
| `param.emotion` | integer | true | 음성 감정 정도 \(지원 목소리: nara, vara, vmikyung, vdain, vyuna, vgoeun, vdaeseong\): 0~3 \(기본값: 0\)\. 0: 중립, 1: 슬픔, 2: 기쁨, 3: 분노 \(nara 미지원\)<br>(Enum: `0`, `1`, `2`, `3`) |
| `param.emotionStrength` | integer | true | 음성 감정 강도 \(지원 목소리: vara, vmikyung, vdain, vyuna, vgoeun, vdaeseong\): 0~2 \(기본값: 1\)\. 0: 약함, 1: 보통, 2: 강함<br>(Enum: `0`, `1`, `2`) |
| `param.format` | string | true | 음성 파일 형식<br>(Enum: `mp3`, `wav`) |
| `param.samplingRate` | integer | true | 음성의 샘플링 레이트 \(wav 형식만 지원\)\. 예외적으로 mijin은 16000 레이트만 지원<br>(Enum: `8000`, `16000`, `24000`, `48000`) |
| `param.alpha` | integer | true | 음색: \-5~5 \(기본값: 0\)\. 0보다 클 경우: 높은 음색, 0보다 작을 경우: 낮은 음색 |
| `param.endPitch` | integer | true | 음성의 끝음 처리 \(지원 목소리: clara, matt, meimei, liangliang, chiahua, kuanlin, carmen, jose, d\-로 시작하는 모든 목소리\): \-5~5 \(기본값: 0\)\. 0보다 클 경우: 높은 끝음, 0보다 작을 경우: 낮은 끝음 |
| `paintProjectId` | string | true | 프로젝트 ID |


**예시:**

```json
{
  "param": {
    "speaker": "example_value",
    "text": "example_value",
    "volume": 0,
    "speed": 0,
    "pitch": 0,
    "emotion": 0,
    "emotionStrength": 0,
    "format": "mp3",
    "samplingRate": 8000,
    "alpha": 0,
    "endPitch": 0
  },
  "paintProjectId": "example_value"
}
```

### AssetFileFormData

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `file` | string | true | 업로드할 파일 |
| `type` | string | true | Asset 타입<br>(Enum: `image`, `video`, `audio`) |
| `name` | string | false | Asset 이름 \(미사용시 파일명에서 추출\) |


**예시:**

```json
{
  "file": "example_value",
  "type": "image",
  "name": "example_value"
}
```

### EncodeFormData

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `file` | string | true | 인코딩할 파일 \(비디오/이미지\) |
| `name` | string | true | 출력 파일의 이름 |
| `type` | string | true | 출력 파일 형식<br>(Enum: `mp4`, `webm`, `gif`) |
| `duration` | number | true | 비디오 길이 \(ms\) |
| `width` | integer | true | 출력 너비 \(px\) |
| `height` | integer | true | 출력 높이 \(px\) |
| `fps` | integer | true | 초당 프레임 수 |
| `audio` | string | false | 오디오 정보가 담긴 JSON 파일 \(type이 'gif'가 아닌 경우에만 필요\)\. 각 오디오 트랙의 url, start, end, volume 정보를 포함함 |
| `paintProjectId` | integer | true | 프로젝트 ID |


**예시:**

```json
{
  "file": "example_value",
  "name": "example_value",
  "type": "mp4",
  "duration": 0.0,
  "width": 0,
  "height": 0,
  "fps": 0,
  "audio": "example_value",
  "paintProjectId": 0
}
```

### AiRequestHistoryItem

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | AI 요청 고유 ID |
| `paintProjectId` | integer | false | 프로젝트 ID |
| `requestType` | string | true | 생성 종류 \(API 별\) |
| `requestData` | string | true | 요청 데이터 |
| `responseData` | string | false | 응답 데이터 |
| `status` | string | true | 요청 상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `errorMessage` | ['string', 'null'] | false | 오류 메시지 \(실패한 경우에만 값 포함\) |
| `createdAt` | string | true | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**예시:**


**pending:**

```json
{
  "id": 1235,
  "paintProjectId": 42,
  "requestType": "IMAGE_GENERATION",
  "requestData": "{\"param\":{\"prompt\":\"A beautiful mountain landscape\",\"width\":1024,\"height\":768,\"numImages\":1}}",
  "responseData": "{\"jobId\":\"01JDV831F240NAXYM33K8FQF3X\",\"jobStatus\":\"Pending\",\"percent\":10}",
  "status": "pending",
  "createdAt": "2024-06-15T09:12:34.567Z",
  "updatedAt": "2024-06-15T09:12:35.123Z"
}
```

**downloading:**

```json
{
  "id": 1236,
  "paintProjectId": 42,
  "requestType": "IMAGE_GENERATION",
  "requestData": "{\"param\":{\"prompt\":\"A futuristic cityscape\",\"width\":1024,\"height\":768,\"numImages\":1}}",
  "responseData": "{\"jobId\":\"01JDV831F240NAXYM33K8FQF3X\",\"jobStatus\":\"Downloading\",\"percent\":100}",
  "status": "downloading",
  "createdAt": "2024-06-15T10:15:34.567Z",
  "updatedAt": "2024-06-15T10:16:35.123Z"
}
```

**completed:**

```json
{
  "id": 1237,
  "paintProjectId": 42,
  "requestType": "IMAGE_GENERATION",
  "requestData": "{\"param\":{\"prompt\":\"A portrait of a woman\",\"width\":1024,\"height\":768,\"numImages\":1}}",
  "responseData": "{\"jobId\":\"01JDV831F240NAXYM33K8FQF3X\",\"jobStatus\":\"Completed\",\"percent\":100,\"result\":{\"generatedImageList\":[\"/assets/2024/6/15/01JDV831F240NAXYM33K8FQF3X/1.png\"]}}",
  "status": "completed",
  "createdAt": "2024-06-15T11:20:34.567Z",
  "updatedAt": "2024-06-15T11:21:35.123Z"
}
```

**failed:**

```json
{
  "id": 1238,
  "paintProjectId": 42,
  "requestType": "IMAGE_CONSTANCY",
  "requestData": "{\"styleFiles\":[{\"readableStream\":{\"fd\":null,\"path\":\"C:\\\\Users\\\\tioh1\\\\Documents\\\\.magictool\\\\uploads\\\\9229fa947d8ddb4d55bb57476192b163\",\"flags\":\"r\",\"mode\":438,\"end\":null,\"bytesRead\":2086236,\"_events\":{},\"_readableState\":{\"highWaterMark\":65536,\"buffer\":[],\"bufferIndex\":0,\"length\":0,\"pipes\":[],\"awaitDrainWriters\":null},\"_eventsCount\":2},\"filename\":\"style.png\"}],\"param\":{\"prompt\":\"steak\",\"width\":1920,\"height\":1080,\"numImages\":1}}",
  "responseData": "{\"jobId\":\"01JQ407CN8JFXASG9DF2APPZH6\",\"jobStatus\":\"Fail\",\"percent\":0,\"errorString\":\"connect ETIMEDOUT 121.134.39.157:8080\"}",
  "status": "failed",
  "errorMessage": "connect ETIMEDOUT 121.134.39.157:8080",
  "createdAt": "2024-06-15T12:30:34.567Z",
  "updatedAt": "2024-06-15T12:31:35.123Z"
}
```

### AiRequestHistoryResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `items[]` | array&lt;AiRequestHistoryItem&gt; | true | AI 요청 이력 목록 |
| `items[].id` | integer | true | AI 요청 고유 ID |
| `items[].paintProjectId` | integer | false | 프로젝트 ID |
| `items[].requestType` | string | true | 생성 종류 \(API 별\) |
| `items[].requestData` | string | true | 요청 데이터 |
| `items[].responseData` | string | false | 응답 데이터 |
| `items[].status` | string | true | 요청 상태<br>(Enum: `pending`, `downloading`, `completed`, `failed`) |
| `items[].errorMessage` | ['string', 'null'] | false | 오류 메시지 \(실패한 경우에만 값 포함\) |
| `items[].createdAt` | string | true | 생성 시간 |
| `items[].updatedAt` | string | false | 수정 시간 |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회를 위한 커서 정보 |
| `cursor.cursorCreatedAt` | string | false | 다음 조회 시 생성 시간 조건에 사용 |
| `cursor.cursorId` | integer | false | 다음 조회 시 ID 조건에 사용 |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**예시:**

```json
{
  "items": [
    {
      "id": 0,
      "paintProjectId": 0,
      "requestType": "example_value",
      "requestData": "example_value",
      "responseData": "example_value",
      "status": "pending",
      "errorMessage": "example_value",
      "createdAt": "2023-01-01T00:00:00Z",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ],
  "cursor": {
    "cursorCreatedAt": "example_value",
    "cursorId": 0
  },
  "hasMore": false
}
```

### GenerationTemplate

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 템플릿 ID |
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | ['string', 'null'] | true | 템플릿 설정 JSON 데이터  \{ prompt, prompt\_en \} |
| `createdAt` | string | false | 생성 시간 |
| `updatedAt` | string | false | 수정 시간 |


**예시:**

```json
{
  "id": 0,
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

### GenerationTemplateInput

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `type` | string | true | 생성 타입 \(code\)<br>(Enum: `VIDEO_GENERATION_GEN3`, `VIDEO_GENERATION_KLING`) |
| `data` | string | true | 템플릿 설정 JSON 데이터 |


**예시:**

```json
{
  "type": "VIDEO_GENERATION_GEN3",
  "data": "example_value"
}
```

### Encode

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 작업 ID |
| `paintProjectId` | integer | true | 프로젝트 ID |
| `userId` | ['integer', 'null'] | true | 사용자 ID |
| `status` | integer | true | 인코딩 상태 \(예: \-1: 에러, 0: 완료, 1: 대기, 2: 진행중, 3: 취소\)<br>(Enum: `-1`, `0`, `1`, `2`, `3`) |
| `name` | string | true | 프로젝트 결과 목록에 표시될 이름 / 파일 이름 |
| `src` | ['string', 'null'] | false | 인코딩 파일 출력 경로 |
| `createdAt` | string | true | 생성 시간 |
| `updatedAt` | string | true | 수정 시간 |


**예시:**

```json
{
  "id": 0,
  "paintProjectId": 0,
  "userId": 0,
  "status": -1,
  "name": "example_value",
  "src": "example_value",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

### EncodeListResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `items[]` | array&lt;Encode&gt; | true | \- |
| `items[].id` | integer | true | 작업 ID |
| `items[].paintProjectId` | integer | true | 프로젝트 ID |
| `items[].userId` | ['integer', 'null'] | true | 사용자 ID |
| `items[].status` | integer | true | 인코딩 상태 \(예: \-1: 에러, 0: 완료, 1: 대기, 2: 진행중, 3: 취소\)<br>(Enum: `-1`, `0`, `1`, `2`, `3`) |
| `items[].name` | string | true | 프로젝트 결과 목록에 표시될 이름 / 파일 이름 |
| `items[].src` | ['string', 'null'] | false | 인코딩 파일 출력 경로 |
| `items[].createdAt` | string | true | 생성 시간 |
| `items[].updatedAt` | string | true | 수정 시간 |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회용 커서 정보\. 더 이상 불러올 데이터가 없으면 null을 반환 |
| `cursor.cursorCreatedAt` | string | false | 다음 조회 시 생성 시간 조건에 사용 |
| `cursor.cursorId` | integer | false | 다음 조회 시 ID 조건에 사용 |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**예시:**

```json
{
  "items": [
    {
      "id": 0,
      "paintProjectId": 0,
      "userId": 0,
      "status": -1,
      "name": "example_value",
      "src": "example_value",
      "createdAt": "2023-01-01T00:00:00Z",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ],
  "cursor": {
    "cursorCreatedAt": "example_value",
    "cursorId": 0
  },
  "hasMore": false
}
```

### VoiceListResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `data[]` | array&lt;Voice&gt; | false | 음성 리소스 목록 |
| `data[].id` | integer | false | 음성 리소스 ID |
| `data[].voiceTitle` | string | false | 음성 제목 |
| `data[].voiceInfo` | string | false | 음성 설명 정보 |
| `data[].voiceFilePath` | string | false | 음성 파일 경로 |
| `data[].voiceImageFile` | string | false | 음성 이미지 파일 경로 |
| `data[].voiceKey` | string | false | 음성 고유 키 |
| `data[].tags` | string | false | 음성에 연결된 태그 목록 \(쉼표로 구분\) |
| `cursor` | ['object', 'null'] | false | 다음 페이지 조회를 위한 커서 정보 |
| `cursor.cursorTitle` | string | false | 다음 조회 시작점의 음성 제목 |
| `cursor.cursorId` | integer | false | 다음 조회 시작점의 음성 ID |
| `hasMore` | boolean | false | 조회할 데이터가 더 있는지 여부 |


**예시:**

```json
{
  "data": [
    {
      "id": 0,
      "voiceTitle": "example_value",
      "voiceInfo": "example_value",
      "voiceFilePath": "example_value",
      "voiceImageFile": "example_value",
      "voiceKey": "example_value",
      "tags": "example_value"
    }
  ],
  "cursor": {
    "cursorTitle": "example_value",
    "cursorId": 0
  },
  "hasMore": false
}
```

### Voice

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 음성 리소스 ID |
| `voiceTitle` | string | false | 음성 제목 |
| `voiceInfo` | string | false | 음성 설명 정보 |
| `voiceFilePath` | string | false | 음성 파일 경로 |
| `voiceImageFile` | string | false | 음성 이미지 파일 경로 |
| `voiceKey` | string | false | 음성 고유 키 |
| `tags` | string | false | 음성에 연결된 태그 목록 \(쉼표로 구분\) |


**예시:**

```json
{
  "id": 0,
  "voiceTitle": "example_value",
  "voiceInfo": "example_value",
  "voiceFilePath": "example_value",
  "voiceImageFile": "example_value",
  "voiceKey": "example_value",
  "tags": "example_value"
}
```

### VoiceTagListResponse

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `groupedTags` | object | false | 유형별로 그룹화된 태그 목록 |
| `groupedTags.button[]` | array&lt;VoiceTag&gt; | false | 버튼 유형의 태그 목록 |
| `groupedTags.button[].id` | integer | false | 태그 ID |
| `groupedTags.button[].name` | string | false | 태그 이름 |
| `groupedTags.button[].type` | string | false | 태그 유형 \(button, lang, gen 등\) |
| `groupedTags.lang[]` | array&lt;VoiceTag&gt; | false | 언어 유형의 태그 목록 |
| `groupedTags.lang[].id` | integer | false | 태그 ID |
| `groupedTags.lang[].name` | string | false | 태그 이름 |
| `groupedTags.lang[].type` | string | false | 태그 유형 \(button, lang, gen 등\) |
| `groupedTags.gen[]` | array&lt;VoiceTag&gt; | false | 세대 유형의 태그 목록 |
| `groupedTags.gen[].id` | integer | false | 태그 ID |
| `groupedTags.gen[].name` | string | false | 태그 이름 |
| `groupedTags.gen[].type` | string | false | 태그 유형 \(button, lang, gen 등\) |
| `tags[]` | array&lt;VoiceTag&gt; | false | 전체 태그 목록 |
| `tags[].id` | integer | false | 태그 ID |
| `tags[].name` | string | false | 태그 이름 |
| `tags[].type` | string | false | 태그 유형 \(button, lang, gen 등\) |


**예시:**

```json
{
  "groupedTags": {
    "button": [
      {
        "id": 0,
        "name": "example_value",
        "type": "example_value"
      }
    ],
    "lang": [
      {
        "id": 0,
        "name": "example_value",
        "type": "example_value"
      }
    ],
    "gen": [
      {
        "id": 0,
        "name": "example_value",
        "type": "example_value"
      }
    ]
  },
  "tags": [
    {
      "id": 0,
      "name": "example_value",
      "type": "example_value"
    }
  ]
}
```

### VoiceTag

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 태그 ID |
| `name` | string | false | 태그 이름 |
| `type` | string | false | 태그 유형 \(button, lang, gen 등\) |


**예시:**

```json
{
  "id": 0,
  "name": "example_value",
  "type": "example_value"
}
```

### Project

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 프로젝트 고유 식별자 |
| `userId` | string | true | 소유자 ID |
| `name` | string | true | 프로젝트 이름 |
| `description` | ['string', 'null'] | true | 프로젝트 설명 |
| `type` | string | true | 프로젝트 타입 \(paint, generation 등\) |
| `subProjectId` | number | true | 하위 프로젝트 ID \(paint\_project\.id 등\) |
| `thumbnailPath` | string | true | 썸네일 이미지 경로 |
| `isDeleted` | boolean | true | 삭제 여부 \(0: 정상, 1: 삭제됨\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**예시:**

```json
{
  "id": 0,
  "userId": "example_value",
  "name": "example_value",
  "description": "example_value",
  "type": "example_value",
  "subProjectId": 0.0,
  "thumbnailPath": "example_value",
  "isDeleted": false,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

### PaintProject

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 페인트 프로젝트 고유 식별자 |
| `userId` | string | true | 소유자 ID |
| `name` | string | true | 페인트 프로젝트 이름 |
| `description` | ['string', 'null'] | false | 페인트 프로젝트 설명 |
| `duration` | integer | true | 페인트 프로젝트 총 길이 \(밀리초\) |
| `framerate` | number | true | 프레임레이트 \(초당 프레임\) |
| `positionX` | number | true | 현재 편집 화면의 X 위치 |
| `positionY` | number | true | 현재 편집 화면의 Y 위치 |
| `zoomLevel` | number | true | 현재 편집 화면의 확대/축소 수준 |
| `currentTime` | integer | true | 현재 타임라인 위치 \(밀리초\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**예시:**

```json
{
  "id": 0,
  "userId": "example_value",
  "name": "example_value",
  "description": "example_value",
  "duration": 0,
  "framerate": 0.0,
  "positionX": 0.0,
  "positionY": 0.0,
  "zoomLevel": 0.0,
  "currentTime": 0,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

### PaintProjectCreate

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `name` | string | true | 페인트 프로젝트 이름 |
| `description` | string | false | 페인트 프로젝트 설명 |
| `duration` | integer | false | 페인트 프로젝트 총 길이 \(밀리초\) |
| `framerate` | number | false | 프레임레이트 \(초당 프레임\) |


**예시:**

```json
{
  "name": "example_value",
  "description": "example_value",
  "duration": 0,
  "framerate": 0.0
}
```

### PaintProjectUpdate

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `name` | string | false | 페인트 프로젝트 이름 |
| `description` | string | false | 페인트 프로젝트 설명 |
| `duration` | integer | false | 페인트 프로젝트 총 길이 \(밀리초\) |
| `framerate` | number | false | 프레임레이트 \(초당 프레임\) |
| `positionX` | number | false | 현재 편집 화면의 X 위치 |
| `positionY` | number | false | 현재 편집 화면의 Y 위치 |
| `zoomLevel` | number | false | 현재 편집 화면의 확대/축소 수준 |
| `currentTime` | integer | false | 현재 타임라인 위치 \(밀리초\) |


**예시:**

```json
{
  "name": "example_value",
  "description": "example_value",
  "duration": 0,
  "framerate": 0.0,
  "positionX": 0.0,
  "positionY": 0.0,
  "zoomLevel": 0.0,
  "currentTime": 0
}
```

### Cut

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | true | 컷 고유 식별자 |
| `canvasId` | integer | true | 속한 캔버스 ID |
| `name` | string | true | 컷 이름 |
| `startTime` | integer | true | 시작 시간 \(밀리초\) |
| `endTime` | integer | true | 종료 시간 \(밀리초\) |
| `duration` | integer | true | 컷 길이 \(밀리초\) |
| `animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |
| `createdAt` | string | true | 생성 일시 |
| `updatedAt` | string | true | 최종 수정 일시 |


**예시:**

```json
{
  "id": 0,
  "canvasId": 0,
  "name": "example_value",
  "startTime": 0,
  "endTime": 0,
  "duration": 0,
  "animation": {
    "property1": "value1",
    "property2": "value2"
  },
  "isLocked": false,
  "isHidden": false,
  "items": {
    "property1": "value1",
    "property2": "value2"
  },
  "audioItems": {
    "property1": "value1",
    "property2": "value2"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

### CutCreate

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `canvasId` | integer | true | 속한 캔버스 ID |
| `name` | string | false | 컷 이름 |
| `startTime` | integer | false | 시작 시간 \(밀리초\) |
| `endTime` | integer | false | 종료 시간 \(밀리초\) |
| `duration` | integer | false | 컷 길이 \(밀리초\) |
| `animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |


**예시:**

```json
{
  "canvasId": 0,
  "name": "example_value",
  "startTime": 0,
  "endTime": 0,
  "duration": 0,
  "animation": {
    "property1": "value1",
    "property2": "value2"
  },
  "isLocked": false,
  "isHidden": false,
  "items": {
    "property1": "value1",
    "property2": "value2"
  },
  "audioItems": {
    "property1": "value1",
    "property2": "value2"
  }
}
```

### CutUpdate

| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|:--------:|------|
| `id` | integer | false | 업데이트할 컷 ID \(PUT /cuts 요청 시 필수\) |
| `canvasId` | integer | false | 속한 캔버스 ID |
| `name` | string | false | 컷 이름 |
| `startTime` | integer | false | 시작 시간 \(밀리초\) |
| `endTime` | integer | false | 종료 시간 \(밀리초\) |
| `duration` | integer | false | 컷 길이 \(밀리초\) |
| `animation` | ['object', 'null'] | false | 전환 효과 데이터 \(JSON 형식\) |
| `isLocked` | boolean | false | 잠금 여부 \(false: 편집 가능, true: 잠김\) |
| `isHidden` | boolean | false | 숨김 여부 \(false: 표시, true: 숨김\) |
| `items` | ['object', 'null'] | false | 컷에 포함된 요소 목록 \(JSON 형식\) |
| `audioItems` | ['object', 'null'] | false | 컷에 포함된 오디오 목록 \(JSON 형식\) |


**예시:**

```json
{
  "id": 0,
  "canvasId": 0,
  "name": "example_value",
  "startTime": 0,
  "endTime": 0,
  "duration": 0,
  "animation": {
    "property1": "value1",
    "property2": "value2"
  },
  "isLocked": false,
  "isHidden": false,
  "items": {
    "property1": "value1",
    "property2": "value2"
  },
  "audioItems": {
    "property1": "value1",
    "property2": "value2"
  }
}
```