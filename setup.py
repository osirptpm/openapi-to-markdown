#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="openapi-to-markdown",
    version="0.1.0",
    description="OpenAPI 스펙 문서를 마크다운 형식으로 변환하는 도구",
    author="OpenAPI to Markdown Team",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=5.1",
    ],
    entry_points={
        "console_scripts": [
            "openapi-to-markdown=openapi_to_markdown.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
