---
layout: post
title:  "관리 계층"
date:   2023-12-14 15:33:00 +0900
categories: Group&nbsp;:&nbsp;Others DevOn&nbsp;NCD
---

### 구조

- Application
    - Business Service
        - Group
            - Component
                - Service
    - Business Rule
        - Group
            - Component
                - Service
    - Data Access
        - Group
            - Component
                - Service
    - Service Access
        - Group
            - Component
                - Service

### 역할

- 서비스 : 기능을 수행 하는 단위 (소유권 보유자만 수정/삭제 가능)
- 컴포넌트 : 서비스의 집합체 (소유권 보유자만 수정/삭제 가능)
- 그룹 : 컴포넌트의 집합체 (소유권 개념 X, 공용)