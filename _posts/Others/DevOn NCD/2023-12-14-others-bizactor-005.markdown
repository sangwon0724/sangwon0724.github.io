---
layout: post
title:  "Business Rule Layer"
date:   2023-12-14 15:42:00 +0900
categories:  DevOn&nbsp;NCD
---

### 정의 및 역할

- 복잡한 비즈니스 로직 수행을 담당하는 Layer
- BR/DA/SA Service를 호출하는 기능
- 제어 로직을 수행하는 기능
- Step과 선으로 연결된 다이어그램으로 비즈니스 로직을 구현

### Data Info

- Internal Data : BR Service 내에서 사용할 변수 DataTable
- Index : LOOP Step 에서 사용할 Index 변수 (※ Type : Integer)
- System
    - RsltNum : CALL Step으로 DA Service 실행 시 데이터 Fetch 건수
    - RsltMsg : CALL Step에서 Ignore 선택한 후, 해당 Step 이 Exception 발생하면 Error Message 가 저장되는 변수
- 추가 정보
- 매핑하지 않으면 에러 표시 및 "XXX DataTable is not assigned"이라는 메시지가 출력된다.
- 해당 Step을 선택했을 시 하단에 나오는 Step 영역에서  
Assigned DataTable에 Data Info에 있는 테이블을 드래그 & 드랍하면  
테이블이 매핑되고 오류 메시지가 사라진다.

### Step 종류

- Call
    - 역할 : 호출할 서비스(DA/BR/SA Service)를 선택하고 Input/Output Parameter를 매핑
    - 모양 : 파란색 사각형
- IF 
    - 역할 : 조건문의 True/False에 따라 분기 수행
    - 모양 : 연분홍색 마름모
- Switch
    - 역할 : 변수 조건에 따라 분기 수행
    - 모양 : 하늘색 마름모
- Loop
    - 역할 : Index 변수의 증감과 조건을 지정하여 True인동안 반복 수행
    - 모양 : 연두색 마름모
- Script
    - 역할 : 코드를 직접 실행
    - 모양 : 녹색 사각형
- Substitution
    - 역할 : Input/Output/Internal DataTable에 저장된 데이터를 가공
    - 모양 : 분홍색 사각형
- Error
    - 역할 : 사용자 정의 Exception 발생 (Error Dictopnary로 별도 관리)
    - 모양 : 빨간 테두리의 흰색 사각형
- Group
    - 역할 : Step들의 범위를 설정하여 해당 그룹을 표시
    - 모양 : 45쪽이 약간 잘린 주황색 사각형
- Point
    - 역할 : Flow Chart 선 정리용 (Logic 구조적 설계용 또는 주석용)
    - 모양 : 회색 원

### Step 생성하기

- Call
    1. 왼쪽 트리에서 호출하고 싶은 BR/DA를 선택하여 Start와 End 사이에 Drag&Drop
    2. 호출할 BR/DA 선택시 좌측 하단에 나오는 INPUT/OUTPUT 파라미터 정보를 해당 서비스의 DataInfo 쪽에 Drag&Drop  
    (매핑하지 않으면 에러 표시 및 "XXX DataTable is not assigned"이라는 메시지가 출력된다.)
    3. Apply 클릭
- IF 
    1. Start와 End 사이의 구간에서 IF 로직이 필요한 곳을 우클릭
    2. Add IF Step 클릭
    3. Condition에 분기 조건 입력
    4. true/false 화살표를  각각의 로직에 알맞는 다른 Step에 연결
    5. Apply 클릭
- Switch
    1. Start와 End 사이의 구간에서 Switch 로직이 필요한 곳을 우클릭
    2. Add Switch Step 클릭
    3. Variable에 비교할 변수 입력 (DataTable에서 Drag 가능)
    4. 분기 추가시 추가할 분기 다음이 되는 값에 우클릭
    5. Insert 클릭
    6. 값 입력
    7. OK (※ 반드시 Default가 항상 맨 밑에 존재)
    8. 각 분기의 화살표를 각각의 로직에 알맞는 다른 Step에 연결
    9. Apply 클릭
- Loop
    1. Start와 End 사이의 구간에서 Loop 로직이 필요한 곳을 우클릭
    2. Add Loop Step 클릭
    3. Data Info의 Index 우클릭
    4. Add Index 클릭
    5. 사용할 인덱스명 입력
    6. OK 클릭
    7. Condition에 반복 조건 입력
    8. 하단의 Index Definition에서 3단계에서 생성한 인덱스 선택 → 초기값 및 증감값 입력
    9. true 화살표의 끝에 반복할 로직 Step 추가 (Call, Script 등등)
    10. 추가한 Step의 화살표를 Loop Step으로 연결
    11. false 화살표의 끝을 로직에 알맞는 다른 Step에 연결
    12. Apply 클릭
- Script
    1. Start와 End 사이의 구간에서 Script 로직이 필요한 곳을 우클릭
    2. Add Script Step 클릭
    3. 하단 Step 영역의 우측 중앙에 있는 물음표 아이콘 클릭
    4. HelpBook.html 오픈
    5. HelpBook.html을 참고하여 스크립트 작성하여 하단 Step 영역의 Script란에 추가
    6. Apply&Test 클릭
- Substitution
    1. Start와 End 사이의 구간에서 Substitution 로직에 우측 DataInfo에서 알맞는 DataTable을 선택하여 Drag&Drop
    2. 하단 Step 영역에서 가공 방식을 설정 (Wizard 방식 / Script 방식)
- Error
    1. 우측 상단의 DataInfo/Dictionary(Error) 탭 영역에서 Dictionary(Error) 탭 선택
    2. Dictionary(Error) 영역의 빈 화면으로 마우스 이동 후 우클릭
    3. Add 클릭
    4. 항목 입력
    5. OK 클릭
    6. Dictionary(Error) 영역의 Error Step 목록에서 필요한 Error Step을 에러를 발생시킬 위치에 Drag&Drop
- Group
    1. Group으로 관리할 Step을 Ctrl+클릭으로 모두 선택 후 (또는 드래그로 영역 지정 후) 우클릭
    2. Group 클릭
    >Group 클릭시 Group 속에서 진행되는 Flow를 별개의 화면으로 확인 가능
- Point
    1. Start와 End 사이의 구간에서 Point가 필요한 곳을 우클릭
    2. Add Point Step 클릭
    3. 아래의 Step 영역에서 Comment 입력 후 차트 영역 클릭
    >연결하기 애매한 구간에 Point Step을 추가해 보기 편하게 선을 연결할수도 있다.

### Call Step의 옵션

- 트랜잭션 분리
    1. 트랜잭션을 분리하고자 하는 Call Step 클릭
    2. 하단 영역에 있는 체크박스 중에서 <span style="color: red;">Txn</span> 체크
    3. Commit 또는 Rollback 을 하고 싶은 곳에 Script Step 을 추가
    4. 해당 Script Step에 상황에 맞는 메소드 호출 코드 작성
        - Commit 호출 : BatchCommit();
        - Rollback 호출 : BatchRollback();

- USE REFERENCE
    1. Data Reference로 전달하려는 Step 을 선택
    2. 하단 영역에 있는 체크박스 중에서 <span style="color: red;">Ref</span> 체크
        - 기능 : 호출되는 Call Step 내부로 DataSet 을 Reference 형태로 전달
        - 주의점
            - 하나의 테이블 / 동일한 컬럼명을 가진 경우에만 사용 가능
            - Multi 테이블 Mapping / 다른 컬럼 Mapping / 행 단위 사용 불가
            - 호출하는 Business Rule 의 컬럼 중 일부가 호출당하는 BR 에서 누락되어 있는 경우는 허용

- 오류 무시
    1. 오류가 발생하더라도 해당 오류를 무시하고 Main Flow를 진행시키게 하려는 Call Step 선택
    2. 하단 영역에 있는 체크박스 중에서 <span style="color: red;">Ignore</span> 체크
    3. 해당 Call Step을 처리한 직후 Data Info의 System의 RsltNUm이 -1인 경우 사용자 오류 처리 로직 수행
    4. Data Info의 System의 RsltMsg에 저장된 Exception 내용 확인 (DebugPrint(RsltMsg);)

- 페이징
    1. 페이징 기능을 사용하고자 하는 Call Step 클릭
    2. 하단 영역에 있는 체크박스 중에서 <span style="color: red;">Page</span> 체크

- ASSIGN ONLY THE FIRST ROW
    1. ASSIGN ONLY THE FIRST ROW 기능을 사용하고자 하는 Call Step 클릭
    2. 하단 영역에 있는 체크박스 중에서 <span style="color: red;">First</span> 체크
        - 기능 : Call Step 에서 Input Data 를 맵핑할 때, DataTable 의 첫번째 Row 데이터만 Assign 시키기

- QUERY TIMEOUT
    1. Query Timeout 을 설정하고자 하는 Call Step 클릭
    2. 하단 영역에 있는 Query Timeout 시간을 초 단위로 설정 (0으로 입력시  Query Timeout 미사용)
        - 주의점
            - Call Step 에서 DataAccess Service 를 호출하는 경우 설정 가능

### Point Step을 통하여 로직 구조 설계하기

1. Point Step으로 로직 구조를 설계
2. 해당 Point Step을 우클릭
3. Replace with XXX Step을 클릭하여 실제 사용할 Step으로 대체

### Step에 대한 추가 사용법

- Call Step을 우클릭하고 "Copy With Data"를 선택하면 매핑되있는 Data Table까지 복사할 수 있다.
- Call Step을 활성/비활성 처리 하고 싶을 때는 해당 Step을 우클릭하고 "Enable/Disable"을 선택하면 된다.
- 각 Step은 우클릭 후 "Replace With XXX Step" 메뉴를 통해서 다른 Step으로 교체할 수 있다.
- 각 Step을 연결하는 연결선을 우클릭하고 "Fix/Unfix Start/End Point" 메뉴를 통해서  
각각의 Step의 연결되있는 시작/종료 지점에 대해서 고정하는 기능을 활성화/비활성화 시킬수 있다.  
(해당 기능 활성화 시 연결되있는 Step의 위치를 변경해도 Point의 위치는 변경되지 않는다.)

### Save & Load

- 서비스를 파일로 저장하기
    1. Flow 영역 밑의 Others를 클릭
    2. "Save Temp"를 클릭
    3. 저장 위치와 파일명을 지정한 후 저장 (저장 형식은 xml 고정)

- 파일로 저장된 서비스를 불러오기
    1. Flow 영역 밑의 Others를 클릭
    2. "Load Temp"를 클릭
    3. 작업 영역에 불러올 서비스 파일을 선택
    4. 정상적으로 불러와지면 "Apply&Test" 버튼과 "Apply" 버튼이 빨간색으로 바뀐다.
>※ 동일한 서비스만 불러올수 있다.
>※ 서비스 정보가 다를 경우에는 오류가 발생한다.

### 순서도의 흐름 오류 검사하기

1. Flow 영역 밑의 Others를 클릭
2. Check를 선택
3. 순서도에 문제 존재시 팝업 발생 (Type ID 또는 Step ID를 알려준다.)

### SQL 체크하기

1. 순서도에 있는 Call Step 중에서 SQL을 확인하고 싶은 DA를 선택
2. 해당 DA를 우클릭
3. View SQL 클릭