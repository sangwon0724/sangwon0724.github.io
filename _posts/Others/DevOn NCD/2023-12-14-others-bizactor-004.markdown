---
layout: post
title:  "데이터"
date:   2023-12-14 15:37:00 +0900
categories: Group&nbsp;:&nbsp;Others DevOn&nbsp;NCD
---

### DevOn NCD 에서 사용하는 데이터 단위

- DataSet : DataTable의 집합체
- DataTable : DataColumn 및 실제 값들로 이루어진 테이블
- DataColumn : 각 데이터에 대한 항목

### Service Parameter

- Input Parameter : 입력받는 데이터
    - Argument
    - UI 화면 입력 항목
    - SELECT 조건 Column
    - INSERT 대상 Column
    - UPDATE 대상 및 조건 Column
    - Delete 조건 Column
- Output Parameter : 출력되는 데이터
    - Return
    - UI 화면 출력 항목
    - SELECT 대상 Column
- 추가 정보
    - 모든 Service는 Input Parameter와 Output Parameter를 가진다.
    - Parameter는 DataSet을 이용해 전달한다.
    - 진행 방식
        1. 업무화면/BR Service
        2. [Input Parameter]
        3. BR/DA/SA Service
        4. [Output Parameter]
        5. 업무화면/BR Service

### DataTable 추가하기

1. DataTable를 추가할 서비스 선택
2. 우측의 DataInfo 패널로 이동
3. DataTable를 추가할 항목 우클릭 (Input/Output/Internal Data)
4. Add DataTable 패널 활성화
5. 해당 DataTable의 Name 입력
6. DataColumn 영역을 우클릭
7. Add DataColumn 선택
8. 항목 입력 (반복)
9. Add DataTable 패널의 OK 클릭
>DataTable 생성시 최소 1개의 DataColumn이 필요하다.

### DataTable에 클립보드로 Column 추가하기

1. 메모장에서 Name/Type/Default/Description를 탭으로 구분해서 작성
2. 전체 복사
3. DataColumn을 추가할 DataTable 우클릭 (Input/Output/Internal Data)
4. Paste DataColumn From Clipboard
>엑셀도 가능

### 클립보드로 DataTable 추가하기

1. 메모장에서 Name/Type/Default/Description를 탭으로 구분해서 작성
2. 전체 복사
3. DataTable를 추가할 항목 우클릭 (Input/Output/Internal Data)
4. Paste DataColumn From Clipboard
5. DataTabl의 Name 입력
6. OK 클릭
>엑셀도 가능

### Drag & Drop으로 DataTable/DataColumn 추가하기


1. DataTable을 가져올 다른 BR이나 DA의 Service를 클릭
2. 좌측 하단에 DataTable 정보 확인
3. 필요한 DataTable/DataColumn 선택
4. 필요한 위치에 드래그

>좌측 하단의 영역에서 드래그 대신에  
>복사 대상에 우클릭해서 Copy DataTable한 후에  
>추가 대상에 우클릭해서 Paste DataTable을 하는 방법도 있다.