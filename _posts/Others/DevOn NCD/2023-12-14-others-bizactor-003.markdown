---
layout: post
title:  "서비스"
date:   2023-12-14 15:35:00 +0900
categories: Group&nbsp;:&nbsp;Others DevOn&nbsp;NCD
---

### 서비스 종류

- 구분
    - Business Rule Service (= BR Service) : 조건/반복/루프/스위치 등의 제어 Logic을 수행하는 Service
    - Data Access Service (= DA Service) : DB와 관련된 기능을 수행하는 Service, SQL을 수행
    - Service Access Service (= SA Service) : 외부 시스템과의 연계를 담당하는 Service

- 추가 정보
    - BR Service에서는 DA/SA/BR Service를 호출한다.
    - 복잡한 비즈니스 Logic은 대부분 BR Service로 구현한다.
    - SA Service 사용시 DevOn NCD에서 정의한 형태의 Adapter 작성이 필요하다.

### 서비스의 상태 - 정의

- <span style="color: red;">C*</span>
    - 서비스가 최초로 생성된 상태
    - 아무런 제약 없이 수정 가능
    - 다른 BR Service에서 호출 불가
    - <b>서비스는 C* 상태에서만 삭제할 수 있다.</b>
- <span style="color: blue;">A</span>
    - 서비스를 모듈화 시킨 상태
    - 다른 BR Service에서 호출 가능
    - 다른 서비스에서 호출되고 있는 경우 Deactivate 불가
- <span style="color: blue;">M*</span>
    - 모듈화된 서비스를 수정 중인 상태
    - 원본이 아닌 사본을 수정 후 원본에 적용시키는 형태
    - 원본은 계속 서비스되고 있는 상태를 가진다.
- <span class="">S</span>
    - 서비스를 외부에 제공할 수 있는 상태
    - BR Service에서는 호출 불가
    - Business Service에서는 호출 가능
- <span class="">M*</span>
    - 외부 제공용 서비스를 수정 중인 상태
    - 원본이 아닌 사본을 수정 후 원본에 적용시키는 형태
    - 원본은 계속 서비스되고 있는 상태를 가진다.

### 서비스의 상태 - 변경 방법
- <span style="color: red;">C*</span> ←→  <span style="color: blue;">A</span>
    - <span style="color: red;">C*</span> → [Activate] → <span style="color: blue;">A</span>
    - <span style="color: red;">C*</span> ← [Deactivate] ← <span style="color: blue;">A</span>
- <span style="color: blue;">A</span> ←→ <span style="color: blue;">M*</span>
    - <span style="color: blue;">A</span> → [Apply] → <span style="color: blue;">M*</span>
    - <span style="color: blue;">A</span> ← [Reactivate/Cancle] ← <span style="color: blue;">M*</span>
- <span style="color: blue;">A</span> ←→ <span class="">S</span>
    - <span style="color: blue;">A</span> → [Expose Service] → <span class="">S</span>
    - <span style="color: blue;">A</span> ← [Hide Service] ← <span class="">S</span>
- <span class="">S</span> ←→ <span class="">M*</span>
    - <span class="">S</span> → [Apply] → <span class="">M*</span>
    - <span class="">S</span> ← [Reactivate/Cancle] ← <span class="">M*</span>

### 서비스의 소유권

- 자신이 서비스 및 컴포넌트는 자신만 수정/삭제 가능
- 다른 사용자의 서비스는 VIew/Text만 가능
- 다른 사용자의 소유권을 가져올수는 있으나, 소유권을 다른 사용자에게 전달할 수는 없다.
- 운영자가 소유권 정책을 서비스/컴포넌트 단위로 설정할 수 있다. (설정한 단위별로 소유권 이동 가능)
- 운영자가 소유권 정책을 컴포넌트 단위로 설정시, 서비스 소유권은 컴포넌트 소유권에 종속된다.

### 서비스 생성 방법

1. 그룹 생성 : Business Rule 우클릭 → Add Group → OK
2. 컴포넌트 생성 : 컴포넌트를 생성할 그룹 우클릭 → Add Component → 항목 입력 → Apply
3. 서비스 생성 : 서비스를 생성할 컴포넌트 우클릭 → Add Service → 항목 입력 → Next → Apply

### 히스토리 관리

1. 서비스를 선택
2. 하단 영역의 History 탭을 클릭하여 영역 활성화
3. History 영역에서 기록 확인
4. 버전 비교
>4-1. 특정 버전의 작성 기록을 확인하고 싶을 때 : 해당 버전을 선택 → 우클릭 → View를 선택하면 된다.  
>4-2. 특정 버전의 기록을 현재 상태와 비교 하고 싶을 때 : 해당 버전을 선택 → 우클릭 → Compare를 선택하면 된다.  
>4-3. 특정 버전의 상태로 서비스를 되돌리고 싶을 때에는 해당 버전을 선택한 후 오른쪽 위의 "Rollback"을 클릭한다.  
>※ 서비스 상태나 서비스 관련 값들도 해당 버전으로 롤백됨으로 주의가 필요하다.