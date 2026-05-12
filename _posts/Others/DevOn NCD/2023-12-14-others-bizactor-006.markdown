---
layout: post
title:  "Data Access Layer"
date:   2023-12-14 15:50:00 +0900
categories:  DevOn&nbsp;NCD
---

### 정의

- Database 관련 작업 수행을 담당하는 Layer

### Data Access Component 종류

- One Table/View Component
- AdHoc/Stored Procedure Component

### One Table/View Component

- 역할
    - 하나의 Table/View에 관련된 SQL 을 수행하는 Service 관리 Table/View의 스키마 정보를 가지고 있는 컴포넌트
- 서비스 생성 방법
    - Wizard 방식
        - SQL문의 형식(Select/Insert/Update/Delete)을 선택하면 SQL문을 자동으로 생성
        - Input/Output Parameter가 자동으로 생성되며 편집 불가
        - Join이 없는 단순 Select 문장과 Insert/Update/Delete 문장에 주로 사용
    - Script 방식
        - Wizard 방식으로 작성된 SQL 문장을 일부 수정할 필요가 있을 때 사용
        - 함수 호출 등이 필요한 경우 사용
        - 자동으로 생성된 Input / Output Parameter 편집 가능

### One Table/View Service 생성

- 공통
    1. One Table/View Component 생성
        1. Data Access의 Group 선택 및 우클릭
        2. Add Component 클릭
        3. 항목 입력
        4. <span style="color: red;">One Table/View Management(CRUD)</span> 항목을 <span style="color: blue;">체크 필요</span>
        5. From Database 클릭
        6. 해당 Table 선택 및 OK 클릭
        7. Apply 클릭
    2. 서비스 생성
        1. 해당 컴포넌트 우클릭
        2. Add Service 클릭
        3. 항목 입력 및 SQL 유형 선택
        4. Next 클릭
- Wizard 방식
    1. 하단의 탭에서 Wizar 탭 영역 활성화
    2. 조회할 Column 체크
    3. Condition 선택 (Value 옵션 선택시 상수값 입력 가능)
    4. Apply & Test를 클릭하여 조회된 값 확인
- Script 방식
1. 하단의 탭에서 Script 탭 영역 활성화
    2. 우측 Data Info 영역에서 Input Data의 RQSTDT에서 우클릭
    3. Add DataColumn 클릭 및 필요한 파라미터 추가
    4. SQL 직접 작성
    5. Input Data의 RQSTDT에 선언한 파라미터를 WHERE 절에서 사용 ("@변수명"으로 사용 가능)
    6. 하단 Test 탭의 Input(& Test Case)탭에 파라미터 값 입력
    7. Apply&Test 클릭하여 조회된 값 확인

### AdHoc/Stored Procedure Component

- 역할
    - 여러 개의 Table/View에 관련된 복잡한 SQL 문을 수행하는 Service 관리
    - Stored Procedure 호출하는 Service 관리
    - Table/View 정보를 관리하지 않음
- 서비스 생성 방법
    - AdHoc 방식
        - SQL 문을 사용자가 직접 작성
        - Input / Output Parameter 를 사용자가 직접 생성
    - Stored Procedure 방식
        - 호출하고자 하는 Stored Procedure 이름을 입력
        - Stored Procedure는 DevOn NCD에서 정의한 형식으로 작성되어야 한다.
        - Input / Output Parameter 수동으로 설정

### AdHoc/Stored Procedure Service 생성

- 공통
    1. AdHoc/Stored Procedure Component 생성
        1. Data Access의 Group 선택 및 우클릭
        2. Add Component 클릭
        3. 항목 입력
        4. <span style="color: red;">One Table/View Management(CRUD)</span> 항목을 <span style="color: blue;">체크 해제</span>
        5. From Database 클릭
        6. 해당 Table 선택 및 OK 클릭
        7. Apply 클릭
    2. 서비스 생성
        1. 해당 컴포넌트 우클릭
        2. Add Service 클릭
        3. 항목 입력 및 서비스 유형 선택
        4. Next 클릭
- AdHoc 방식
    1. 우측 Data Info 영역에서 Input/Output Data의 RQSTDT에 파라미터 추가
    2. Script 빈 칸을 더블 클릭
    3. From절까지 SQL 직접 작성
    4. OK 클릭
    5. Optional Condition Query (선택적 조회 조건) 작성하기
        1. Script 아래의 빈 영역 우클릭
        2. Add 클릭 및 Script Editor 영역 활성화
        3. 상단의 All DataColumns 영역에서 필요한 것을 선택해서 Optional Condition DataColumns에 추가  
        (Input Data의 RQSTD에 추가한 파라미터의 목록이 출력된다.)
        4. Script 영역에서 해당 파라미터에 대한 조건절 입력 및 OK 클릭 (예시 : NAME LIKE CONCAT('%',@NAME,'%'))
    6. 필수적 조회 조건 작성하기
        1. Script 아래의 빈 영역 우클릭
        2. Add 클릭 및 Script Editor 영역 활성화
        3. Optional Condition DataColumns을 입력하지 않고 Script 영역에서 SQL 작성 및 OK 클릭
    7. Test 탭에 파라미터 값을 입력하고 Apply&Test 클릭
- Stored Procedure 방식
    1. 호출하고자 하는 Stored Procedure 이름을 입력한다.
    2. 우측의 DataInfo의 Input/Output Parameter를 설정한다.
    3. Apply&Test 클릭하여 조회된 값 확인

>※ AdHoc 방식에서 Optional Condition Query는
>조건절에 사용된 Input Parameter 값이 Null일 경우 해당 조건을 무시하고 수행한다.
>예시) 파라미터 [A, B, C] => 입력한 항목 [A, C] => 검색되는 조건 [A, C]
>
>※ AdHoc 방식에서 Optional Condition Query를 사용할 때
>무조건 NAME LIKE CONCAT('%',@NAME,'%')처럼 단문으로 쓰는게 아니라
>NAME LIKE CONCAT('%',@NAME,'%') AND MEMBER_TYPE IN (1, 2, 3)처럼 복합적으로 사용해도 된다.
>
>※ AdHoc 방식에서 Optional Condition Query를 사용할 때
>${칼럼명} LIKE CONCAT('%',@칼럼값,'%')처럼 사용해서 쿼리를 좀 더 동적으로 사용할 수도 있다.