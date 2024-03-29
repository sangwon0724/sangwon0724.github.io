---
layout: post
title:  "자료구조에 대하여"
date:   2024-02-10 17:24:00 +0900
categories: 이론&nbsp;-&nbsp;자료&nbsp;구조
---

### 자료구조란?

- 자료를 효율적으로 표현하고 저장하고 처리할 수 잇도록 정리하는 것

```mermaid
flowchart TD
    top[자료구조] --> a[이론적 측면]
    top[자료구조] --> b[실제적 측면]

    a --> a_a[그래프 이론]
    a --> a_b[집합 이론]
    a --> a_c[조합적 분석]
    a --> a_d[확률 이론]

    b --> b_a[문자열]
    b --> b_b[리스트]
    b --> b_c[트리]
    b --> b_d[그래프]
    b --> b_e[파일]

    a_a --> a_f[이산 수학]
    a_b --> a_f
    a_c --> a_f

    a_f --> a_g[알고리즘의 분석]
    a_d --> a_g

    b_a --> b_f[알고리즘의 구현]
    b_b --> b_f
    b_c --> b_f
    b_d --> b_f
    b_e --> b_f

    a_g --> a_h[검색]
    a_g --> a_i[정렬]
    a_g --> a_j[효율 분석]

    a_j --> a_k[공간 복잡도]
    a_j --> a_l[시간 복잡도]

    b_f --> b_g[응용]

    b_g --> b_h[응용]

    b_h --> b_i[프로그래밍]
    b_h --> b_j[파일 작성]
    b_h --> b_k[메모리 관리]
    b_h --> b_l[운영체제]
```

### 자료구조의 분류

```mermaid
flowchart LR
    top[자료구조] --> a[단순 구조]
    top[자료구조] --> b[선형 구조]
    top[자료구조] --> c[비선형 구조]
    top[자료구조] --> d[파일 구조]

    a --> a_1[정수]
    a --> a_2[실수]
    a --> a_3[문자]
    a --> a_4[문자열]

    b --> b_1[순차 리스트]
    b --> b_2[연결 리스트]
        b_2 --> b_2_1[단순 연결 리스트]
        b_2 --> b_2_2[이중 연결 리스트]
        b_2 --> b_2_3[원형 연결 리스트]
    b --> b_3[스택]
    b --> b_4[큐]
    b --> b_5[데크]

    c --> c_1[트리]
        c_1 --> c_1_1[일반 트리]
        c_1 --> c_1_2[이진 트리]
    c --> c_2[그래프]
        c_2 --> c_2_1[방향 그래프]
        c_2 --> c_2_2[무방향 그래프]

    d --> d_1[순차 파일]
    d --> d_2[색인 파일]
    d --> d_3[직접 파일]
```

### 자료의 표현

```mermaid
flowchart LR
    top[자료의 표현] --> a[수치 자료]
    top --> b[문자 자료]
    top --> c[논리 자료]
    top --> d[포인터 자료]
    top --> e[문자열 자료]

    a --> a_1[10진수]
        a_1 --> a_1_1[존 형식]
        a_1 --> a_1_2[팩 형식]
    a --> a_2[2진수]
        a_2 --> a_2_1[정수]
            a_2_1 --> a_2_1_1[부호 절댓값]
            a_2_1 --> a_2_1_2[1의 보수]
            a_2_1 --> a_2_1_3[2의 보수]
        a_2 --> a_2_2[실수]
            a_2_2 --> a_2_2_1[고정소수점]
            a_2_2 --> a_2_2_2[부동소수점]

    b --> b_1[BCD 코드]
    b --> b_2[EBCDIC 코드]
    b --> b_3[ASCII 코드]
    b --> b_4[유니코드]
```

#### 10진수의 표현

##### 존 형식

- 10진수 한 자리를 존(Zone) 형식으로 표현하기 위해 1바이트(8비트)를 단위로 사용한다.
- 8비트는 상위 비트 존 영역과 하위 4비트 수치 영여긍로 구성된다.
- 기본적으로 존 영역에는 항상 1111을 표시한다. (16진수로 변환하여 F로 표기한다.)
- 최하위 8비트의 존 영역은 양수/음수를 표시하기 위해 다른 값을 저장한다.
    - 양수면 C가 저장된다.
    - 음수면 D가 저장된다.
- 예시
    - \+ 213
        - F2F1C3
    - \- 213
        - F2F1D3

##### 팩 형식

- 존 형식은 항상 1111(F)을 저장해야 하므로 기억 공간이 낭비되고 처리가 지연된다.
- 존 형식의 문제를 해결하기 위해 팩(Pack) 형식은 1바이트에 2개의 10진수를 저장한ㄷ.
- 최하위 4비트는 존 형식과 동일하게 양수/음수를 표시하기 위해 다른 값을 저장한다.
    - 양수면 C가 저장된다.
    - 음수면 D가 저장된다.
- 예시
    - \+ 213
        - 213C
    - \- 213
        - 213D

#### 2진수의 정수 표현

- 2진수는 일정한 길이의 n비트로 표현한다.

##### 부호 절댓값

- 최상위 비트(SB : Most Significant Bit)인 첫번째 비트는 부호를 표시하기 위해 사용한다.
    - 양수면 0이 저장된다.
    - 음수면 1이 저장된다.

##### 1의 보수

- 양수는 부호 절댓값 형식과 같은 방법으로 표현한다.
- 음수는 1의 보수(1's Complement)로 변환하여 표현한다.
- 1의 보수로 음수를 구할 때는 그 값을 양의 2진수로 표현한 후 각 자리의 1과 0을 서로 바꾸면 된다.
- 예시
    - 전제 : - 21을 구하려고 한다.
    - 21의 2진수 표현 방법 : 00010101
    - 21의 1의 보수 : 11101010

##### 2의 보수

- 양수는 부호 절댓값 형식과 같은 방법으로 표현한다.
- 음수는 2의 보수(2's Complement)로 변환하여 표현한다.
- 2의 보수로 음수를 구할 때는 1의 보수를 구한 뒤에 그 값에 1을 더하면 된다.

#### 2진수의 실수 표현

##### 고정소수점

- 소수점이 항상 최상위 비트의 왼쪽 밖에 고정되있거나 최하위 비트의 오른쪽 밖에 고정되있다고 취급한다.
- 예시
    - 소수점이 최상위 비트의 왼쪽 밖에 고정되있다고 가정했을 때 00010101은 0.00010101을 나타낸다.
    - 소수점이 최하위 비트의 오른쪽 밖에 고정되있다고 가정했을 때 00010101은 00010101.0을 나타낸다.

##### 부동소수점

- 과학적 표기 방식의 실수를 사용한다.
- 고정소수점 방식에 비해서 아주 작은 값이다 아주 큰 값을 표현할 수가 있다.
- 예시
    - 213 = 0.213 * 10<sup>3</sup>
    - 0.213에 해당하는 부분을 소수부라고 부른다.
    - 10에 해당하는 부분을 밑수라고 부른다.
    - 3에 해당하는 부분을 지수라고 부른다.
- 부동 소수점의 표현 범위에 따라서 부동소수점 표현 방식도 표현 방법이 달라진다.
    - 단정도 부동소수점 (Single Precision)
        - 4바이트를 사용한다.
        - 부호, 지수부, 가수부를 각각 1비트, 8비트, 23비트를 사용한다.
    - 배정도 부동소수점 (Double Precision)
        - 8바이트를 사용한다.
        - 부호, 지수부, 가수부를 각각 1비트, 11비트, 52비트를 사용한다.
- 부동소수점으로 표현하는 과정 (IEE 754 표준)
    1. 정규화
        - 정수부가 1이 되도록 소수점을 이동하여 과학적 표기로 변환한다.
    2. 부호
        - 양수는 0, 음수는 1을 저장한다.
    3. 가수부
        - 정규화하면 정수는 항상 1이 되므로, 정수부를 생략하고 소수부만 저장한다.
        - 남는 자리는 0으로 채운다.
    4. 지수부
        - 정규화해서 구한 지수와 바이어스를 더한 값을 저장한다.
        - 바이어스
            - 지수의 부호를 표현하기 위해 사용하는 값
            - 단정도 부동소수점 방식에서는 127을 사용한다.
            - 배정도 부동소수점 방식에서는 1023을 사용한다.
- 예시
    - 전제
        - \+ 100010.101을 변환
    - 수행
        1. 정규화
            - 1.00010101 x 2<sup>5</sup>
            - 소수부는 0.00010101이 된다.
            - 지수는 5가 된다.
        2. 부호
            - 양수니까 0이 된다.
        3. 가수부
            - 1.00010101에서 정수를 제외한 0.00010101이 저장된다.
        4. 지수부
            - 지수는 5다.
            - 단정도 부동소수점 방식일 경우에는 5 + 127인 132를 2진수로 변환한 값을 저장한다.
            - 배정도 부동소수점 방식일 경우에는 5 + 1023인 1028를 2진수로 변환한 값을 저장한다.

#### 문자 자료의 표현

- 컴퓨터 내부에서는 문자 자료도 1과 0의 2진수 조합으로 표현한다.

##### BCD 코드 (Binary-Coded Decimal Code)

- BCD 코드는 6비트를 사용한다.
- 상위 2비트의 존 비트와 하위 4비트의 숫자 비트로 구성된다.
- 존 비트와 숫자 비트의 조합에 따라서 문자가 구성된다.
- 10진수 숫자 0 ~ 9와 대문자 A ~ Z까지 표현할 수 있다.

##### EBCDIC 코드 (Extended Binary-Coded Decimal Interchange Code)

- EBCDIC 코드는 8비트를 사용한다.
- 상위 4비트의 존 비트와 하위 4비트의 숫자 비트로 구성된다.
- 존 비트와 숫자 비트의 조합에 따라서 문자가 구성된다.
- 기존 BCD 코드에서 표현할 수 있는 문자에 추가로 소문자와 특수문자를 표현할 수 있다.

##### ASCII 코드 (American Standard Code for Information Interchange)

- ASCII 코드는 7비트를 사용한다.
- 상위 3비트의 존 비트와 하위 4비트의 숫자 비트로 구성된다.
- 존 비트와 숫자 비트의 조합에 따라서 문자가 구성된다.
- 10진수 숫자 0 ~ 9와 대/소문자 A ~ Z에 특수문자까지 표현할 수 있다.
- ASCII 코드를 데이터 통신용으로 사용할 때는 최상위 비트에 패리티 비트를 추가하여 8비트 형식으로 사용하기도 한다.

##### 유니코드

- BCD 코드, EBCDIC 코드, ASCII 코드 모두 문자 코드 표에 정의되어 있지 않은 문자를 표현하는 건 불가능하다.
- 위의 문제를 해결하기 위해 세계 여러 나라의 언어를 통일된 방법으로 표현할 수 있도록  
정의된 국제 표준 코드(ISO/IEC 10646)가 유니코드다.

#### 논리 자료의 표현

- 논리 자료
    - 논리값을 표현하기 위한 자료 형식
- 논리값
    - 참(True)과 거짓(False) 중 하나를 표시한 값
- 1비트로도 표현할 수도 있긴 하지만 일반적으로 컴퓨터 내부에서는 1바이트나 1워드를 논리값을 표현하는 단위로 사용한다.
- 1바이트를 사용하여 논리 자료를 표현하는 방법
    - 방법 1
        - 참
            - 00000001
        - 거짓
            - 00000000
    - 방법 2
        - 참
            - 11111111
        - 거짓
            - 00000000
    - 방법 3
        - 참
            - 하나 이상의 비트를 1로 표시
        - 거짓
            - 00000000

#### 포인터 자료의 표현

- 포인터(Pointer) 자료
    - 메모리 주소를 표현하기 위한 자료 형식
- 자료를 저장하고 있는 변수나 특정 위치의 메모리 주소를 저장한다.
- 주소 연산을 할 떄 사용한다.
- 포인터 자료를 사용하면 복잡한 자료구조 연산을 메모리에서의 주소 연산만으로 처리할 수 있다.

#### 문자열 자료의 표현

- 문자열(String) 자료
    - 여러 글자로 이루어진 문자 그룹을 하나의 자료로 취급하여 메모리에 연속적으로 저장하는 자료 형식
    - 문자 자료는 한 글자만 표현할 수 있다.
- 부분 문자열을 포함하는 문자열 자료를 메모리에 저장하는 방법
    - 부분 문자열 사이에 구분자를 사용하여 저장
        - 메모리 이용률
            - 문자열 길이 + 구분자 길이 → 효율적
        - 부분 문자열 탐색 시간
            - 문자 비교 연산 시간 + 구분자 구별 시간 → 비효율적
    - 가장 긴 문자열의 길이에 맞춰서 고정 길이로 저장
        - 메모리 이용률
            - 가장 긴 부분 문자열 길이 * 부분 문자열의 개수 → 비효율적
        - 부분 문자열 탐색 시간
            - 문자 비교 연산 시간 → 효율적
    - 부분 문자열을 연속하여 저장하고 각 부분 문자열에 대한 포인터를 사용한다.
        - 메모리 이용률
            - 문자열 길이 + 포인터 저장 공간 → 효율적
        - 부분 문자열 탐색 시간
            - 문자 비교 연산 시간 + 포인터 주소 연산 시간 → 효율적

### 자료의 추상화

- 추상화 (Abstraction)
    - 자세하고 복잡한 것 대신 필수적이고 중요한 특징만 골라서 단순화시키는 작업
- 크고 복잡한 문제를 해결하기 위해 문제에 추상화를 적용하여 문제를 단순화시킨다.
- 자료 추상화(Data Abstraction)는 이미 알고 있는 잘 정의된 기본 개념을 이용하여 표현한다.
    - 자료
        - 프로그램의 처리 대상이 되는 모든 것
        - 어떤 값 자체를 의미하기도 한다.
    - 연산
        - 어떤 일을 처리하는 과정
        - 연산자를 이용하여 수행된다.
    - 자료형
        - 처리할 잘의 집합과 자료에 대해 수행할 수 있는 연산자의 집합
        - 자료형을 정의할 때는 자료형에 속하는 값과 이를 처리하기 위해 사용할 수 있는 연산자를 정의한다.
- 추상 자료형 (ADT, Abstaract Data Type)
    - 추상화하여 정의한 자료형

### 알고리즘의 이해

- 알고리즘 (Algorithm)
    - 주어진 문제를 해결하는 방법을 추상화하여 일련의 단계적 절차를 논리적으로 기술해 놓은 명세서
- 효과적인 알고리즘이 되기 위해서는 아래의 조건을 만족해야 한다.
    - 입력 (input)
        - 알고리즘을 수행하는 데 필요한 자료가 외부에서 입력되어야 한다.
    - 출력 (Output)
        - 알고리즘을 수행하고 나면 결과를 하나 이상 출력해야 한다.
    - 명확성 (Definiteness)
        - 수행할 작업의 내용과 순서를 나타내는 알고리즘의 명령어는 명확하게 명세되어야 한다.
    - 유한성 (Finiteness)
        - 알고리즘을 모두 수행하고 나면 반드시 종료되어야 한다.
    - 효과성 (Effectiveness)
        - 알고리즘의 모든 명령어는 기본적이며 실행할 수 있어야 한다.

### 알고리즘의 표현 방법

#### 자연어를 이용한 서술적 표현

- 알고리즘을 사연이 쓰는 자연어(언어)로 표현하는 방법
- 자연어는 서술적일 뿐만 아니라 쓰는 사람에 따라 일관성이나 명확성을 유지하기 어렵다.
- 누구라도 쉽게 이해하고 쓸 수 있어야 하는 알고리즘을 표현하는 데는 한계가 있다.

#### 순서도를 이용한 도식화

- 알고리즘을 순서도를 작성하는 규칙에 따라 도식화하는 방법
- 순서도를 이용하면 명령의 흐름을 쉽게 파악할 수 있다.
- 복잡한 알고리즘을 표현하기에는 한계가 있다.

#### 프로그래밍 언어를 이용한 구체화

- 알고리즘을 프로그래밍 언어를 사용하여 표현하는 방법
- 알고리즘 자체가 구체화되므로 추가로 구체화 작업을 할 필요가 없다.
- 작성한 프로그래밍 언어를 모르면 이해하기 어렵다.
- 다른 프로그래밍 언어로 프로그램을 개발하면 알고리즘을 번역하고 다른 프로그래밍 언어로 변환해야 하므로 비효율적이다.

#### 가상 코드를 이용한 추상화

- 알고리즘을 프로그래밍 언어로 표현했을 때 생기는 단점을 보완한 방법
- 프로그래밍 언어의 형태를 갖춘 가상 코드를 사용하여 알고리즘을 표현한다.
    - 실제 프로그래밍 언어가 아니라서 직접 실행할 수는 없다.
    - 형태가 일반적인 프로그래밍 언어와 유사하기 때문에 다른 프로그래밍 언어로 변환하기가 쉽다.
    - 가상 코드는 의사 코드(Pseudo code) 또는 알고리즘 기술 언어(ADL, Algorithm Description Language)라고도 부른다.

### 알고리즘의 성능 분석

#### 알고리즘의 성능 분석 기준

- 정확성
    - 올바른 자료가 입력되었을 때 유한한 시간 내에 올바른 결과가 출력되는 정도
- 명확성
    - 알고리즘의 이해하기 쉽고 명확하게 작성된 정도
- 수행량
    - 알고리즘의 주요 연산이 반복되는 양
- 메모리 사용량
    - 알고리즘이 문제를 해결하기 위해 사용하는 메모리 공간의 크기
- 최적성
    - 내가 선택한 알고리즘이 현재 마주한 문제를 해결하기 위한 최적의 알고리즘인지에 대한 정도
    - 가장 중요한 기준이다.

#### 알고리즘 성능 분석 방법

##### 공간 복잡도 (Spacce Complexity)

- 알고리즘을 프로그램으로 실행하여 완료하는 데까지 필요한 총 저장 공간
- 팔요한 고정 공간과 가변 공간을 합하여 구한다.
- 고정 공간
    - 프로그램의 크기나 입출력 횟수와는 상관없이 고정적으로 필요한 저장 공간
    - 프로그램 저장 공간과 변수 및 상수를 저장하는 공간
- 가변 공간
    - 실행 과정에서 사용하는 자료와 변수를 저장하는 공간과 함수를 실행하는 데 관련 있는 저장하는 공간

##### 시간 복잡도 (Time Complexity)

- 알고리즘을 프로그램으로 실행하여 완료하는 데까지 걸리는 시간
- 시간 복잡도는 프로그램의 컴파일 시간과 실행 시간을 더해 구한다.
- 컴파일 시간
    - 프로그램의 특성과 큰 관련이 없으므로 고정된 같은 시간으로 가정한다.
    - 일단 컴파일이 되면 프로그램을 수정하지 않는 한 추가로 컴파일 작업을 하지 않으므로  
    시간 복잡도에서는 컴파일 시간을 의미있는 시간으로 취급하지 않는다.
- 실행 시간
    - 실행 시간은 같은 프로그램이라도 실행되는 컴퓨터의 성능에 따라 달라질 수 있기 떄문에  
    실제 실행 시간을 측정하기보다는 명령문의 실행 빈도수를 계산하여 추정한다.

#### 알고리즘 성능 분석 표기법

- 알고리즘 성능을 비교하는 방법
    - 메모리 사용 공간을 분석하는 공간 복잡도
    - 실행 시간을 분석하는 시간 복잡도
- 일반적으로 알고리즘의 주요 성능 차이는 실행 시간 차이에서 발생한다.
- 따라서 알고리즘을 분석하기 위한 성능 분석 표기는 시간 복잡도 표기를 의미한다.
- 시간 복잡도는 실행 빈도 함수에서 입력 크기 n에 대한 실행 시간의 증가율만 분석하는 점근적 분석(Asymptotic Analysis)이다.
    - 따라서 시간 복잡도는 실행 빈도 함수의 상수항과 계수는 무시하고  
    n의 증가에 따라 증가율이 가장 큰 하나에 대해서 차수 표기법(Order otation)으로 표기한다.

>실행 함수는 상수 → logn → n → nlogn → n<sup>2</sup> → n<sup>3</sup> → 2<sup>n</sup> 순으로 느려진다.
>실행 함수가 상수일 경우에는 O(1)처럼 내부에 1로 표시한다.

##### 빅-오 표기법 (Big-Oh Notation)

- 주로 많이 사용하는 표기법
- `O(f(n))`처럼 표기한다.
    - 만약 시간 복잡도가 n<sup>2라면</sup> 시간 복잡도는 O(n<sup>2</sup>)가 된다.
- 함수의 상한을 나타내기 위한 표기법이다.
- 실행 빈도 수에서 가장 영향이 큰 항을 계수를 생략하고 괄호 안에 표시한다.
    - 만약 실행 빈도 수가 `4n + 2`라면 빅오-표기법으로는 `O(n)`이 된다.

##### 빅-오메가 표기법 (Big-Omega Notation)

- `Ω(f(n))`처럼 표기한다.
- 함수의 하한을 나타내기 위한 표기법이다.


##### 빅-세타 표기법 (Big-Theta Notation)

- `θ(f(n))`처럼 표기한다.
- 상한과 하한이 같은 정확한 차수를 표기하기 위한 표기법