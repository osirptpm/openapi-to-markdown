import yaml
from openapi_to_markdown import convert_refs, generate_markdown, save_markdown

# 간단한 테스트 OpenAPI 스펙 정의
test_spec = {
    "openapi": "3.0.0",
    "info": {
        "title": "테스트 API",
        "version": "1.0.0",
        "description": "예시 테스트 API"
    },
    "paths": {
        "/test": {
            "get": {
                "summary": "테스트 API 엔드포인트",
                "description": "테스트 API 설명",
                "responses": {
                    "200": {
                        "description": "성공적인 응답",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "example": {
                                    "id": 1,
                                    "name": "테스트 이름"
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "테스트 데이터 생성",
                "description": "테스트 데이터 생성 API",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    }
                                }
                            },
                            "example": {
                                "name": "새 테스트 이름"
                            }
                        },
                        "application/xml": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    }
                                }
                            },
                            "example": "<test><name>XML 테스트 이름</name></test>"
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "생성됨",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "examples": {
                                    "성공 예시": {
                                        "value": {
                                            "id": 100,
                                            "name": "생성된 테스트"
                                        }
                                    },
                                    "다른 예시": {
                                        "value": {
                                            "id": 101,
                                            "name": "또 다른 테스트"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# 테스트 스펙으로 마크다운 생성
resolved_spec = convert_refs(test_spec)
markdown_content = generate_markdown(resolved_spec)
save_markdown("test_markdown.md", markdown_content)

print("테스트 마크다운이 생성되었습니다: test_markdown.md")
