---
layout: post
title:  "Service Access Layer"
date:   2023-12-14 15:55:00 +0900
categories:  DevOn&nbsp;NCD
---

### 정의 및 역할

● 외부 시스템과의 연계를 담당하는 Layer
● 연계를 위한 Adapter를 작성하고 DevOn NCD에 등록하여 외부 시스템과의 연계를 수행한다.
● Adapter는 DevOn NCD에서 정의한 형식대로 작성되어야 한다.

### 컴포넌트 생성

1. Service Access에 그룹 생성
2. 그룹 우클릭 후 Add Component 클릭
3. General 영역에서 항목 입력
4. Legacy 영역에서 항목 선택

>※ Legacy System에 등록된 DevOn NCD Server의 Service를 원격호출 하는 기능을 한다.
>※ 등록된 DevOn NCD Server는 외부 시스템이나 자기 자신도 가능하다.

### 서비스 생성

1. 서비스를 생성할 컴포넌트 우클릭
2. Service ID 입력 (※ 입력 방식 : "EXT." + 호출할 Service ID)
3. 호출할 Service의 Input / Output Data 를 동일하게 설정