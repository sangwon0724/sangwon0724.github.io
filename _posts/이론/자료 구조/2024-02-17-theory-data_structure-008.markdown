---
layout: post
title:  "정렬 (Sort)"
date:   2024-02-17 20:58:00 +0900
categories: 이론&nbsp;-&nbsp;자료&nbsp;구조
tags: [정렬]
---

### 정렬이란?

- 순서 없이 배열된 자료를 정해진 순서에 맞게 재배열하는 것
- 키 (Key)
    - 자료를 정렬하는데 사용이 되는 기준

#### 정렬 방향

- 오름차순 (Asecending)
    - 작은 것부터 큰 것 순서로 재배열한다.
- 내림차순 (Descending)
    - 큰 것부터 작은 것 순서로 재배열한다.

#### 정렬 방식의 분류

- 실행 방법
    - 비교식 정렬 (Comparative Sort)
        - 비교할 각 키값을 한 번에 두 개씩 비교하여 교환하는 방식
    - 분배식 정렬 (Distribute Sort)
        - 키값을 기준으로 자료를 여러 개의 부분집합으로 분해하고,  
        각 부분집합을 정렬함으로써 전체를 정렬하는 방식
- 정렬 장소
    - 내부 정렬 (Internal Sort)
        - 컴퓨터 메모리 내부에서 정렬하는 방식
    - 외부 정렬 (External Sort)
        - 메모리의 외부인 보조 기억 장치에서 정렬하는 방식

##### 내부 정렬

- 정렬할 자료를 메인 메모리에 올려서 정렬하는 방식
- 정렬 속도는 빠르지만, 정렬할 자료의 양이 메인 메모리의 용량에 따라 제한된다.
- 종류
    - 비교식
        - 교환 방식
            - 키를 비교하고 교환하여 정렬하는 방식
            - 선택 정렬, 버블 정렬, 퀵 정렬
        - 삽입 방식
            - 키를 비교하고 삽입하여 정렬하는 방식
            - 삽입 정렬, 셸 정렬
        - 병합 방식
            - 키를 비교하고 병합하여 정렬하는 방식
            - 2-way 병합, n-way 병합
        - 선택 방식
            - 이진 트리를 사용하여 정렬하는 방식
            - 힙 정렬, 트리 정렬
    - 분배식
        - 분배 방식
            - 키를 구성하는 값을 여러 개의 부분집합에 분배하여 정렬하는 방식
            - 기수 정렬

##### 외부 정렬

- 정렬할 자료를 보조 기억 장치에 올려서 정렬하는 방식
- 내부 정렬보다 비교적 속도는 떨어지지만,  
보조 기억 장치를 대용량으로 쓸 수 있어 내부 정렬로 처리할 수 없는 대용량 자료를 정렬할 수 있다.
- 외부 정렬은 파일을 부분 파일로 분리하여 각각을 내부 정렬 방법으로 정렬하여 병합하는 방식이다.
- 2-way 병합, n-way 병합이 해당한다.

### 선택 정렬 (Selection Sort)

- 전체 원소 중에서 기준 위치에 맞는 원소를 자리를 교환하여 정렬하는 방식
- 정렬 방법
    - 전체 원소 중에서 가장 작은 원소를 찾은 다음, 첫째 원소와 자리를 교환한다.
    - 그 다음 둘째로 작은 원소를 찾고, 둘째 원소와 자리를 교환한다.
    - 그 다음 셋째로 작은 원소를 찾고, 셋째 원소와 자리를 교환한다.
    - 이 과정을 반복하면서 정렬을 완성한다.
- 공간 복잡도
    - n
    - 메모리를 n개 사용하기 때문이다.
- 시간 복잡도
    - O(n<sup>2</sup>)
    - 어떤 경우에서나 비교 횟수가 같다.
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    1. 첫번째 선택 정렬 수행
        - 첫째 자리를 기준으로 잡고 가장 작은 원소를 찾아서 자리를 교환한다.
        - 기준은 69가 된다.
        - 가장 작은 원소는 2가 되니 2와 자리를 교환한다.
        - 비교 : [<span style="color: red;">69</span>, 10, 30, <span style='color: red;'>2</span>, 16, 8, 31, 22]
        - 결과 : [<span style="color: blue;">2</span>, 10, 30, <span style='color: red;'>69</span>, 16, 8, 31, 22]
    2. 두번째 선택 정렬 수행
        - 두번째 자리를 기준으로 잡고 두번째로 작은 원소를 찾아서 자리를 교환한다.
        - 기준은 10이 된다.
        - 두번째로 작은 원소는 8이 되니 8과 자리를 교환한다.
        - 비교 : [<span style='color: blue;'>2</span>, <span style='color: red;'>10</span>, 30, 69, 16, <span style='color: red;'>8</span>, 31, 22]
        - 결과 : [<span style='color: blue;'>2, 8</span>, 30, 69, 16, <span style='color: red;'>10</span>, 31, 22]
    3. 세번째 선택 정렬 수행
        - 세번째 자리를 기준으로 잡고 세번째로 작은 원소를 찾아서 자리를 교환한다.
        - 기준은 30이 된다.
        - 세번째로 작은 원소는 10이 되니 10과 자리를 교환한다.
        - 비교 : [<span style='color: blue;'>2, 8</span>, <span style='color: red;'>30</span>, 69, 16, <span style='color: red;'>10</span>, 31, 22]
        - 결과 : [<span style='color: blue;'>2, 8, 10</span>, 69, 16, <span style='color: red;'>30</span>, 31, 22]
    4. 네번째 선택 정렬 수행
        - 네번째 자리를 기준으로 잡고 네번째로 작은 원소를 찾아서 자리를 교환한다.
        - 기준은 69가 된다.
        - 네번째로 작은 원소는 16이 되니 16과 자리를 교환한다.
        - 비교 : [<span style='color: blue;'>2, 8, 10</span>, <span style='color: red;'>69</span>, <span style='color: red;'>16</span>, 30, 31, 22]
        - 결과 : [<span style='color: blue;'>2, 8, 10, 16</span>, <span style='color: red;'>69</span>, 30, 31, 22]
    5. 다섯번째 선택 정렬 수행
        - 다섯번째 자리를 기준으로 잡고 다섯번째로 작은 원소를 찾아서 자리를 교환한다.
        - 기준은 69가 된다.
        - 다섯번째로 작은 원소는 22가 되니 22와 자리를 교환한다.
        - 비교 : [<span style='color: blue;'>2, 8, 10, 16</span>, <span style='color: red;'>69</span>, 30, 31, <span style='color: red;'>22</span>]
        - 결과 : [<span style='color: blue;'>2, 8, 10, 16, 22</span>, 30, 31, <span style='color: red;'>69</span>]
    6. 여섯번째 선택 정렬 수행
        - 여섯번째 자리를 기준으로 잡고 여섯번째로 작은 원소를 찾아서 자리를 교환한다.
        - 기준은 30이 된다.
        - 30보다 작은 원소는 없으니 다음 단계로 넘어간다.
        - 비교 : [<span style='color: blue;'>2, 8, 10, 16, 22</span>, <span style='color: red;'>30</span>, 31, 69]
        - 결과 : [<span style='color: blue;'>2, 8, 10, 16, 22, 30</span>, 31, 69]
    7. 일곱번째 선택 정렬 수행
        - 일곱번째 자리를 기준으로 잡고 일곱번째로 작은 원소를 찾아서 자리를 교환한다.
        - 기준은 31이 된다.
        - 31보다 작은 원소는 없으니 다음 단계로 넘어간다.
        - 비교 : [<span style='color: blue;'>2, 8, 10, 16, 22, 30</span>, <span style='color: red;'>31</span>, 69]
        - 결과 : [<span style='color: blue;'>2, 8, 10, 16, 22, 30, 31</span>, 69]
    8. 여덟첫번째 선택 정렬 수행
        - 원소가 마지막 하나만 남았으니 해당 원소가 가장 큰 값이며,  
        마지막 자리에 존재하기 때문에 이미 정렬된 상태로 인지하여 실행을 종료한다.
        - 비교 : [<span style='color: blue;'>2, 8, 10, 16, 22, 30, 31</span>, <span style='color: red;'>69</span>]
        - 결과 : [<span style='color: blue;'>2, 8, 10, 16, 22, 30, 31,  69</span>]

### 버블 정렬 (Bubble Sort)

- 인접한 원소를 두 개씩 비교하여 자리를 교환하는 방식을 반복하여 정렬하는 방식
- 가장 크거나 가장 작은 값을 맨 뒤로 보내는 방식
- n번째 차례일때 정렬된 원소의 개수가 n개가 될 때까지 정렬을 수행한다.
- 시간 복잡도
    - O(n<sup>2</sup>)
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    1. 첫번째 버블 정렬 수행
        - [<span style='color: red;'>69</span>, <span style='color: red;'>10</span>, 30, 2, 16, 8, 31, 22] => 69와 10 비교
        - [10, <span style='color: red;'>69</span>, <span style='color: red;'>30</span>, 2, 16, 8, 31, 22] => 69와 30 비교
        - [10, 30, <span style='color: red;'>69</span>, <span style='color: red;'>2</span>, 16, 8, 31, 22] => 69와 2 비교
        - [10, 30, 2, <span style='color: red;'>69</span>, <span style='color: red;'>16</span>, 8, 31, 22] => 69와 16 비교
        - [10, 30, 2, 16, <span style='color: red;'>69</span>, <span style='color: red;'>8</span>, 31, 22] => 69와 8 비교
        - [10, 30, 2, 16, 8, <span style='color: red;'>69</span>, <span style='color: red;'>31</span>, 22] => 69와 31 비교
        - [10, 30, 2, 16, 8, 31, <span style='color: red;'>69</span>, <span style='color: red;'>22</span>] => 69와 22 비교
        - [10, 30, 2, 16, 8, 31, <span style='color: red;'>22</span>, <span style='color: blue;'>69</span>] => 1단계 종료 (정렬된 원소 1개)
    2. 두번째 버블 정렬 수행
        - [<span style='color: red;'>10</span>, <span style='color: red;'>30</span>, 2, 16, 8, 31, 22, <span style='color: blue;'>69</span>] => 10과 30 비교
        - [10, <span style='color: red;'>30</span>, <span style='color: red;'>2</span>, 16, 8, 31, 22, <span style='color: blue;'>69</span>] => 30과 2 비교
        - [10, 2, <span style='color: red;'>30</span>, <span style='color: red;'>16</span>, 8, 31, 22, <span style='color: blue;'>69</span>] => 30과 16 비교
        - [10, 2, 16, <span style='color: red;'>30</span>, <span style='color: red;'>8</span>, 31, 22, <span style='color: blue;'>69</span>] => 30과 8 비교
        - [10, 2, 16, 8, <span style='color: red;'>30</span>, <span style='color: red;'>31</span>, 22, <span style='color: blue;'>69</span>] => 30과 31 비교
        - [10, 2, 16, 8, 30, <span style='color: red;'>31</span>, <span style='color: red;'>22</span>, <span style='color: blue;'>69</span>] => 31과 22 비교
        - [10, 2, 16, 8, 30, <span style='color: red;'>22</span>, <span style='color: blue;'>31, 69</span>] => 2단계 종료 (정렬된 원소 2개)
    3. 세번째 버블 정렬 수행
        - [<span style='color: red;'>10</span>, <span style='color: red;'>2</span>, 16, 8, 30, 22, <span style='color: blue;'>31, 69</span>] => 10과 2 비교
        - [2, <span style='color: red;'>10</span>, <span style='color: red;'>16</span>, 8, 30, 22, <span style='color: blue;'>31, 69</span>] => 10과 16 비교
        - [2, 10, <span style='color: red;'>16</span>, <span style='color: red;'>8</span>, 30, 22, <span style='color: blue;'>31, 69</span>] => 16과 8 비교
        - [2, 10, 8, <span style='color: red;'>16</span>, <span style='color: red;'>30</span>, 22, <span style='color: blue;'>31, 69</span>] => 16과 30 비교
        - [2, 10, 8, 16, <span style='color: red;'>30</span>, <span style='color: red;'>22</span>, <span style='color: blue;'>31, 69</span>] => 30과 22 비교
        - [2, 10, 8, 16, <span style='color: red;'>22</span>, <span style='color: blue;'>30, 31, 69</span>] => 3단계 종료 (정렬된 원소 3개)
    4. 네번째 버블 정렬 수행
        - [<span style='color: red;'>2</span>, <span style='color: red;'>10</span>, 8, 16, 22, <span style='color: blue;'>30, 31, 69</span>] => 2와 10 비교
        - [2, <span style='color: red;'>10</span>, <span style='color: red;'>8</span>, 16, 22, <span style='color: blue;'>30, 31, 69</span>] => 10와 8 비교
        - [2, 8, <span style='color: red;'>10</span>, <span style='color: red;'>16</span>, 22, <span style='color: blue;'>30, 31, 69</span>] => 10와 16 비교
        - [2, 8, 10, <span style='color: red;'>16</span>, <span style='color: red;'>22</span>, <span style='color: blue;'>30, 31, 69</span>] => 16와 22 비교
        - [2, 8, 10, <span style='color: red;'>16</span>, <span style='color: blue;'>22, 30, 31, 69</span>] => 4단계 종료 (정렬된 원소 4개)
    5. 다섯번째 버블 정렬 수행
        - [<span style='color: red;'>2</span>, <span style='color: red;'>8</span>, 10, 16, <span style='color: blue;'>22, 30, 31, 69</span>] => 2와 8 비교
        - [2, <span style='color: red;'>8</span>, <span style='color: red;'>10</span>, 16, <span style='color: blue;'>22, 30, 31, 69</span>] => 8와 10 비교
        - [2, 8, <span style='color: red;'>10</span>, <span style='color: red;'>16</span>, <span style='color: blue;'>22, 30, 31, 69</span>] => 10와 16 비교
        - [2, 8, <span style='color: red;'>10</span>, <span style='color: blue;'>16, 22, 30, 31, 69</span>] => 5단계 종료 (정렬된 원소 5개)
    6. 여섯번째 버블 정렬 수행
        - [<span style='color: red;'>2</span>, <span style='color: red;'>8</span>, 10, <span style='color: red;'>10</span>, <span style='color: blue;'>16, 22, 30, 31, 69</span>] => 2와 8 비교
        - [2, <span style='color: red;'>8</span>, <span style='color: red;'>10</span>, <span style='color: red;'>10</span>, <span style='color: blue;'>16, 22, 30, 31, 69</span>] => 8와 10 비교
        - [2, <span style='color: red;'>8</span>, <span style='color: blue;'>10, 16, 22, 30, 31, 69</span>] => 6단계 종료 (정렬된 원소 6개)
    7. 일곱번째 버블 정렬 수행
        - [<span style='color: red;'>2</span>, <span style='color: red;'>8</span>, <span style='color: blue;'>10, 16, 22, 30, 31, 69</span>] => 2와 8 비교
        - [<span style='color: red;'>2</span>, <span style='color: blue;'>8, 10, 16, 22, 30, 31, 69</span>] => 7단계 종료 (정렬된 원소 7개)
    8. 여덟번째 버블 정렬 수행
        - 원소가 마지막 하나만 남았으니 해당 원소가 가장 작은 값이며,  
        마지막 자리에 존재하기 때문에 이미 정렬된 상태로 인지하여 실행을 종료한다.
        - [<span style='color: blue;'>2, 8, 10, 16, 22, 30, 31, 69</span>] => 8단계 종료 (정렬된 원소 8개)

### 퀵 정렬 (Quick Sort)

- 정렬할 전체 원소에 대해 정렬을 수행하지 않고 기준값을 중심으로  
왼쪽 부분집합과 오른쪽 부분집합으로 분할한다.
    - 왼쪽 부분집합에는 기준값보다 작거나 같은 원소들을 이동시킨다.
    - 오른쪽 부분집합에는 기준값보다 크거나 같은 원소들을 이동시킨다.
- 피봇 (Pivot)
    - 2개의 부분집합으로 분할 시 사용되는 기준 값
    - 선택되는 기준은 다양하다.
        - 전체 원소 중 가운데에 위치한 원소
            - 원소의 개수가 짝수일 경우 가운데 2개 중 왼쪽의 값을 사용한다.
        - 전체 원소 중 첫째 원소
        - 전체 원소 중 마지막 원소
        - 별도의 수식을 사용하기도 한다.
- 동작 규칙
    1. 왼쪽 끝에서 오른쪽으로 움직이면서 크기를 비교하여 피봇보다 크거나 같은 원소를 찾아 L로 표시한다.
        - 단 L은 R과 만나면 더 이상 오른쪽으로 이동하지 못하고 멈춘다.
    2. 오른쪽 끝에서 왼쪽으로 움직이면서 크기를 비교하여 피봇보다 작거나 같은 원소를 찾아 R로 표시한다.
        - 단 R은 L과 만나면 더 이상 왼쪽으로 이동하지 못하고 멈춘다.
    3. 비교 작업을 수행한다.
        - L과 R이 각각 존재하는 경우, 서료 교환하고 L과 R의 현재 위치에서 다시 L과 R을 찾는다.
        - L과 R이 같은 원소를 가리키는 경우, 해당 원소는 피봇과 교환한다.
            - 교환한 자리를 피봇 위치로 지정하고 해당 단계의 퀵 정렬을 끝낸다.
    4. 피봇의 확정된 위치를 기준으로 만들어진 새로운 왼쪽/오른쪽 부분집합에 대해서 1단계 ~ 3단계까지의 과정을 반복한다.
        - 왼쪽/오른쪽 부분집합의 크기가 모두 1이 되면 전체 퀵 정렬을 종료한다.
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    1. 첫번째 퀵 정렬 수행
        - 가운데 원소인 2를 피봇으로 선택한다.
            - [69, 10, 30, <span style='background: lightgray;'>2</span>, 16, 8, 31, 22]
        - 왼쪽에서 2보다 크거나 같은 값을 찾을 때 69가 해당하여 69가 L이 된다.
        - 오른쪽에서 2보다 작거나 같은 값을 찾을 때 해당하는 값이 없어서 69가 R이 된다.
        - L과 R이 같으니 해당하는 원소인 69를 피봇인 2와 위치를 교환한다.
            - 비교 : [<span style='color: red;'>69</span>, 10, 30, <span style='background: lightgray;'><span style='color: red;'>2</span></span>, 16, 8, 31, 22]
            - 결과 : [<span style='background: lightgray;'><span style='color: blue;'>2</span></span>, 10, 30, <span style='color: red;'>69</span>, 16, 8, 31, 22]
    2. 두번째 퀵 정렬 수행
        - 피봇인 2를 기준으로 왼쪽 부분집합은 원소가 존재하지 않으므로 퀵 정렬을 수행하지 않고,  
        오른쪽 부분집합에 대해서 퀵정렬을 수행한다.
        - 가운데 원소인 16을 피봇으로 선택한다.
            - 결과 : [<span style='color: blue;'>2</span>, 10, 30, 69, <span style='background: lightgray;'>16</span>, 8, 31, 22]
        - 왼쪽에서 16보다 크거나 같은 값을 찾을 때 30이 해당하여 30이 L이 된다.
        - 오른쪽에서 16보다 작거나 같은 값을 찾을 때 8이 해당하여 8이 R이 된다.
        - L과 R을 찾았으니 두 원소의 위치를 교환한다.
            - 비교 : [<span style='color: blue;'>2</span>, 10, <span style='color: red;'>30</span>, 69, <span style='background: lightgray;'>16</span>, <span style='color: red;'>8</span>, 31, 22]
            - 결과 : [<span style='color: blue;'>2</span>, 10, <span style='color: red;'>8</span>, 69, <span style='background: lightgray;'>16</span>, <span style='color: red;'>30</span>, 31, 22]
        - 왼쪽에서 16보다 크거나 같은 값을 찾을 때 69가 해당하여 69가 L이 된다.
        - 오른쪽에서 2보다 작거나 같은 값을 찾을 때 해당하는 값이 없어서 69가 R이 된다.
        - L과 R이 같으니 해당하는 원소인 69를 피봇인 16와 위치를 교환한다.
            - 비교 : [<span style='color: blue;'>2</span>, 10, 8, <span style='color: red;'>69</span>, <span style='background: lightgray;'><span style='color: red;'>16</span></span>, 30, 31, 22]
            - 결과 : [<span style='color: blue;'>2</span>, 10, 8, <span style='background: lightgray;'><span style='color: blue;'>16</span></span>, <span style='color: red;'>69</span>, 30, 31, 22]
    3. 세번째 퀵 정렬 수행
        - 피봇인 16을 기준으로 원소가 2개 이상인 부분집합이 왼쪽에 생겼으니 해당 부분집합에 퀵 정렬을 수행한다.
        - 가운데 원소인 10을 피봇으로 선택한다.
            - [<span style='color: blue;'>2</span>, <span style='background: lightgray;'>10</span>, 8, <span style='color: blue;'>16</span>, 69, 30, 31, 22]
        - 왼쪽에서 10보다 크거나 같은 값을 찾을 때 10이 해당하여 10이 L이 된다.
        - 오른쪽에서 10보다 작거나 같은 값을 찾을 때 8이 해당하여 8이 R이 된다.
        - L과 R을 찾았으니 두 원소의 위치를 교환한다.
            - 비교 : [<span style='color: blue;'>2</span>, <span style='background: lightgray;'><span style='color: red;'>10</span></span>, <span style='color: red;'>8</span>, <span style='color: blue;'>16</span>, 69, 30, 31, 22]
            - 결과 : [<span style='color: blue;'>2</span>, <span style='color: red;'>8</span>, <span style='background: lightgray;'><span style='color: red;'>10</span></span>, <span style='color: blue;'>16</span>, 69, 30, 31, 22]
        - 왼쪽에서 10보다 크거나 같은 값을 찾을 때 해당하는 값이 없어서 10이 L이 된다.
        - 오른쪽에서 10보다 작거나 같은 값을 찾을 때 10이 해당하여 10이 R이 된다.
        - L과 R이 같으니 해당하는 원소인 10을 피봇인 10과 위치를 교환한다.
            - 해당하는 원소와 피봇의 위치가 같았으므로 자리를 교환하기 전과 후의 상태가 같다.
            - 비교 : [<span style='color: blue;'>2</span>, 8, <span style='background: lightgray;'><span style='color: red;'>10</span></span>, <span style='color: blue;'>16</span>, 69, 30, 31, 22]
            - 결과 : [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'><span style='background: lightgray;'>10</span>, 16</span>, 69, 30, 31, 22]
    4. 네번째 퀵 정렬 수행
        - 피봇인 10을 기준으로 왼쪽 부분집합은 원소가 1개인 부분집합이기 떄문에 퀵 정렬을 수행하지 않고,  
        오른쪽 부분집합에 대하여 퀵 정렬을 수행한다.
        - 가운데 원소인 30을 피봇으로 선택한다.
            - [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, 69, <span style='background: lightgray;'>30</span>, 31, 22]
        - 왼쪽에서 30보다 크거나 같은 값을 찾을 때 69가 해당하여 69가 L이 된다.
        - 오른쪽에서 30보다 작거나 같은 값을 찾을 때 22가 해당하여 22가 R이 된다.
        - L과 R을 찾았으니 두 원소의 위치를 교환한다.
            - 비교 : [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, <span style='color: red;'>69</span>, <span style='background: lightgray;'>30</span>, 31, <span style='color: red;'>22</span>]
            - 결과 : [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, <span style='color: red;'>22</span>, <span style='background: lightgray;'>30</span>, 31, <span style='color: red;'>69</span>]
        - 왼쪽에서 30보다 크거나 같은 값을 찾을 때 해당하는 값이 없어서 30이 L이 된다.
        - 오른쪽에서 30보다 작거나 같은 값을 찾을 때 해당하는 값이 없어서 30이 R이 된다.
        - L과 R이 같으니 해당하는 원소인 30을 피봇인 30과 위치를 교환한다.
            - 해당하는 원소와 피봇의 위치가 같았으므로 자리를 교환하기 전과 후의 상태가 같다.
            - 비교 : [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, 22, <span style='background: lightgray;'><span style='color: red;'>30</span></span>, 31, 69]
            - 결과 : [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, 22, <span style='background: lightgray;'><span style='color: blue;'>30</span></span>, 31, 69]
    5. 다섯번째 퀵 정렬 수행
        - 피봇인 30을 기준으로 왼쪽 부분집합은 원소가 1개인 부분집합이기 떄문에 퀵 정렬을 수행하지 않고,  
        오른쪽 부분집합에 대하여 퀵 정렬을 수행한다.
        - 가운데 원소인 31을 피봇으로 선택한다.
            - [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, 22, <span style='color: blue;'>30</span>, <span style='background: lightgray;'>31</span>, 69]
        - 왼쪽에서 31보다 크거나 같은 값을 찾을 때 해당하는 값이 없어서 31이 L이 된다.
        - 오른쪽에서 31보다 작거나 같은 값을 찾을 때 해당하는 값이 없어서 31이 R이 된다.
        - L과 R이 같으니 해당하는 원소인 30을 피봇인 31과 위치를 교환한다.
            - 해당하는 원소와 피봇의 위치가 같았으므로 자리를 교환하기 전과 후의 상태가 같다.
            - 비교 : [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, 22, <span style='color: blue;'>30</span>, <span style='background: lightgray;'><span style='color: red;'>31</span></span>, 69]
            - 결과 : [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, 22, <span style='color: blue;'>30</span>, <span style='background: lightgray;'><span style='color: blue;'>31</span></span>, 69]
    6. 여섯번째 퀵 정렬 수행
        - 피봇인 30을 기준으로 왼쪽 부분집합은 원소가 0개인 부분집합이기 떄문에 퀵 정렬을 수행하지 않고,  
        또한 오른쪽 부분집합도 원소가 1개인 부분집합이기 떄문에 퀵 정렬을 수행하지 않는다.
        - 모든 부분집합의 원소가 1개 이하이기 때문에 전체 퀵 정렬을 종료한다. 
            - 비교 : [<span style='color: blue;'>2</span>, 8, <span style='color: blue;'>10, 16</span>, 22, <span style='color: blue;'>30</span>, <span style='color: blue;'>31</span>, 69]
            - 결과 : [<span style='color: blue;'>2, 8, 10, 16, 22, 30, 31, 69</span>]
- 시간 복잡도
    - O(log<sub>2</sub>n)

### 삽입 정렬 (Insert Sort)

- 정렬되어 있는 부분집합에 정렬할 새로운 원소의 위치를 찾아 삽입하는 방식
- 삽입 정렬에서는 정렬할 자료가 두 개의 부분집합으로 나뉘어 있다고 가정한다.
    - S (Sorted Subset)
    - U (Unsorted Subset)
- 시간 복잡도
    - O(n<sup>2</sup>)
- 동작 규칙
    1. 앞 부분 원소부터 정렬을 수행한다.
    2. 정렬된 앞 부분의 원소는 부분집합 S가 되고,  
    아직 정렬되지 않은 나머지 원소는 부분집합 U가 된다.
    3. 정렬하지 않은 부분집합 U의 원소를 하나씩 꺼내서  
    이미 정렬한 부분집합 S의 마지막 원소부터 비교하면서 위치를 찾아 삽입한다.
    4. 삽입 정렬을 수행할 때마다 부분집합의 S의 원소는 하나씩 늘어나고,  
    부분집합 U의 원소는 하나씩 줄어든다.
    5. 부분집합 U가 원소가 0개인 공집합이 되면 삽입 정렬을 종료한다.
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    0. 초기 상태
        - 첫번째 요소인 69를 정렬되어 있는 부분 집합 S로 취급한다.
        - 69를 제외한 나머지 원소 전부를 정렬되어 있지 않은 부분 집합 U로 취급한다.
        - S = {69}, U = {10, 30, 2, 16, 8, 31, 22}
        - [<span style='color: blue;'>69</span>, 10, 30, 2, 16, 8, 31, 22]
    1. 첫번째 삽입 정렬 수행
        - U의 첫번째 요소인 10을 S와 비교하여 알맞는 위치에 삽입한다.
        - S = {10, 69}, U = {30, 2, 16, 8, 31, 22}
        - 비교 : [<span style='color: blue;'>69</span>, <span style='color: red;'>10</span>, 30, 2, 16, 8, 31, 22]
        - 결과 : [<span style='color: blue;'><span style='color: red;'>10</span>, 69</span>, 30, 2, 16, 8, 31, 22]
    2. 두번째 삽입 정렬 수행
        - U의 첫번째 요소인 30을 S와 비교하여 알맞는 위치에 삽입한다.
        - S = {10, 30, 69}, U = {2, 16, 8, 31, 22}
        - 비교 : [<span style='color: blue;'>10, 69</span>, <span style='color: red;'>30</span>, 2, 16, 8, 31, 22]
        - 결과 : [<span style='color: blue;'>10, <span style='color: red;'>30</span>, 69</span>, 2, 16, 8, 31, 22]
    3. 세번째 삽입 정렬 수행
        - U의 첫번째 요소인 2를 S와 비교하여 알맞는 위치에 삽입한다.
        - S = {2, 10, 30, 69}, U = {16, 8, 31, 22}
        - 비교 : [<span style='color: blue;'>10, 30, 69</span>, <span style='color: red;'>2</span>, 16, 8, 31,22]
        - 결과 : [<span style='color: blue;'><span style='color: red;'>2</span>, 10, 30, 69</span>, 16, 8, 31, 22]
    4. 네번째 삽입 정렬 수행
        - U의 첫번째 요소인 16을 S와 비교하여 알맞는 위치에 삽입한다.
        - S = {2, 10, 16, 30, 69}, U = {8, 31, 22}
        - 비교 : [<span style='color: blue;'>2, 10, 30, 69</span>, <span style='color: red;'>16</span>, 8, 31, 22]
        - 결과 : [<span style='color: blue;'>2, 10, <span style='color: red;'>16</span>, 30, 69</span>, 8, 31, 22]
    5. 다섯번째 삽입 정렬 수행
        - U의 첫번째 요소인 8을 S와 비교하여 알맞는 위치에 삽입한다.
        - S = {2, 8, 10, 16, 30, 69}, U = {31, 22}
        - 비교 : [<span style='color: blue;'>2, 10, 16, 30, 69</span>, <span style='color: red;'>8</span>, 31, 22]
        - 결과 : [<span style='color: blue;'>2, <span style='color: red;'>8</span>, 10, 16, 30, 69</span>, 31, 22]
    6. 여섯번째 삽입 정렬 수행
        - U의 첫번째 요소인 31을 S와 비교하여 알맞는 위치에 삽입한다.
        - S = {2, 8, 10, 16, 30, 31, 69}, U = {22}
        - 비교 : [<span style='color: blue;'>2, 8, 10, 16, 30, 69</span>, <span style='color: red;'>31</span>, 22]
        - 결과 : [<span style='color: blue;'>2, 8, 10, 16, 30, <span style='color: red;'>31</span>, 69</span>, 22]
    7. 일곱번째 삽입 정렬 수행
        - U의 첫번째 요소인 22를 S와 비교하여 알맞는 위치에 삽입한다.
        - S = {2, 8, 10, 16, 22, 30, 31, 69}, U = {}
        - 비교 : [<span style='color: blue;'>2, 8, 10, 16, 30, 31, 69</span>, <span style='color: red;'>22</span>]
        - 결과 : [<span style='color: blue;'>2, 8, 10, 16, <span style='color: red;'>22</span>, 30, 31, 69</span>]
    8. 여덟번째 삽입 정렬 수행
        - U가 공집합이 됬으므로 삽입 정렬을 종료한다.
        - 결과 : [<span style='color: blue;'>2, 8, 10, 16, 22, 30, 31, 69</span>]

### 셸 정렬 (Shell Sort)

- 일정한 간격으로 떨어져 있는 자료들끼리 부분집합을 구성하고,  
각 부분집합에 있는 원소에 대해 삽입 정렬을 수행하는 작업을 반복하여 전체 원소를 정렬하는 방식
- 전체 원소에 대해 삽입 원소를 수행하는 것보다 부분집합으로 나누어 삽입 정렬하면  
비교 연산과 자리 이동 연산의 횟수를 줄일 수 있다.
- 시간 복잡도
    - O(n<sup>1.25</sup>)
- 동작 규칙
    1. 부분집합을 만드는 기준인 간격을 매개변수 h에 저장한다.
    2. 한 단계 수행될 때마다 h의 값을 감소시키고 셸 정렬을 순환 호출한다.
    3. h가 1이 되면 정렬을 완성한다.
- 셸 정렬의 성능은 매개변수 h의 값에 따라 달라진다.
    - 일반적으로는 원소 개수의 1/2를 사용하고, 한 단계 수행할 때마다 다시 그 값을 1/2를 사용한다.
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    0. 매개변수 h는 원소 개수의 1/2인 4가 된다.
    1. 첫번째 셸 정렬 수행
        - 4칸 떨어진 원소들을 같은 부분집합으로 묶는다.
            - {69, 16}, {10, 8}, {30, 31}, {2, 22}
        - 첫번째 부분집합인 {69, 16}에 대해서 삽입 정렬을 수행한다.
            - 삽입 정렬 수행 시 {16, 69}가 된다.
            - 이를 전체집합에 적용한다.
            - 비교 : [<span style='color: red;'>69</span>, 10, 30, 2, <span style='color: red;'>16</span>, 8, 31, 22]
            - 결과 : [<span style='color: red;'>16</span>, 10, 30, 2, <span style='color: red;'>69</span>, 8, 31, 22]
        - 두번째 부분집합인 {10, 8}에 대해서 삽입 정렬을 수행한다.
            - 삽입 정렬 수행 시 {8, 10}이 된다.
            - 이를 전체집합에 적용한다.
            - 비교 : [16, <span style='color: red;'>10</span>, 30, 2, 69, <span style='color: red;'>8</span>, 31, 22]
            - 결과 : [16, <span style='color: red;'>8</span>, 30, 2, 69, <span style='color: red;'>10</span>, 31, 22]
        - 세번째 부분집합인 {30, 31}에 대해서 삽입 정렬을 수행한다.
            - 삽입 정렬 수행 시 {30, 31}이 된다.
            - 이를 전체집합에 적용한다.
            - 연산 전/후가 동일하기 때문에 자리의 교환은 일어나지 않는다.
            - 비교 : [16, 8, <span style='color: red;'>30</span>, 2, 69, 10, <span style='color: red;'>31</span>, 22]
            - 결과 : [16, 8, <span style='color: red;'>30</span>, 2, 69, 10, <span style='color: red;'>31</span>, 22]
        - 네번째 부분집합인 {2, 22}에 대해서 삽입 정렬을 수행한다.
            - 2는 22보다 작기때문에 자리를 교환하지 않는다.
            - 삽입 정렬 수행 시 {2, 22}가 된다.
            - 연산 전/후가 동일하기 때문에 자리의 교환은 일어나지 않는다.
            - 비교 : [16, 8, 30, <span style='color: red;'>2</span>, 69, 10, 31, <span style='color: red;'>22</span>]
            - 결과 : [16, 8, 30, <span style='color: red;'>2</span>, 69, 10, 31, <span style='color: red;'>22</span>]
    2. 두번째 셸 정렬 수행
        - 매개변수 h는 기존 h의 1/2인 2가 된다.
        - 2칸 떨어진 원소들을 같은 부분 집합으로 묶는다.
            - {16, 30, 69, 31}, {8, 2, 10, 22}
        - 첫번째 부분집합인 {16, 30, 69, 31}에 대해서 삽입 정렬을 수행한다.
            - 삽입 정렬 수행 시 {16, 30, 31, 69}이 된다.
            - 이를 전체집합에 적용한다.
            - 비교 : [<span style='color: red;'>16</span>, 8, <span style='color: red;'>30</span>, 2, <span style='color: red;'>69</span>, 10, <span style='color: red;'>31</span>, 22]
            - 결과 : [<span style='color: red;'>16</span>, 8, <span style='color: red;'>30</span>, 2, <span style='color: red;'>31</span>, 10, <span style='color: red;'>69</span>, 22]
        - 두번째 부분집합인 {8, 2, 10, 22}에 대해서 삽입 정렬을 수행한다.
            - 삽입 정렬 수행 시 {2, 8, 10, 22}가 된다.
            - 이를 전체집합에 적용한다.
            - 비교 : [16, <span style='color: red;'>8</span>, 30, <span style='color: red;'>2</span>, 31, <span style='color: red;'>10</span>, 69, <span style='color: red;'>22</span>]
            - 결과 : [16, <span style='color: red;'>2</span>, 30, <span style='color: red;'>8</span>, 31, <span style='color: red;'>10</span>, 69, <span style='color: red;'>22</span>]
    3. 세번째 셸 정렬 수행
        - 매개변수 h는 기존 h의 1/2인 1이 된다.
        - 1칸 떨어진 원소들을 같은 부분 집합으로 묶는다.
            - {16, 2, 30, 8, 31, 10, 69, 22}
        - 매개변수가 1이 됬으므로 전체 원소에 대해서 삽입 정렬을 수행한다.
            - 비교 : [<span style='color: red;'>16, 2, 30, 8, 31, 10, 69, 22</span>]
            - 결과 : [<span style='color: blue;'>2, 8, 10, 16, 22, 30, 31, 69</span>]

### 병합 정렬 (Merge Sort)

- 여러 개의 정렬된 자료 집합을 병합하여 하나의 정렬된 집합으로 만드는 방식
- 병합 정렬은 분할 정복(Devide and Conquer) 기법을 사용한다.
    - 병합 정렬의 동작 규칙 같은 기법을 의미한다.
- 시간 복잡도
    - O(nlog<sub>2</sub>n)
- 동작 규칙
    0. 전체 원소에 대해 정렬을 수행하지 않는다.
    1. 부분집합으로 분할(Devide)한다.
    2. 각 부분집합에 대해서 정렬 작업을 정복(Conquer)한다.
        - 각 부분집합에 대해서 정렬 작업을 완성한다는 것을 의미한다.
    3. 정렬된 부분집합들을 다시 결합(Combine)한다.
- 종류
    - 2-way 병합
        - 정렬된 자료 집합 2개를 결합하여 하나의 집합으로 만드는 병합 방법
    - n-way 병합
        - 정렬된 자료 집합 n개를 결합하여 하나의 집합으로 만드는 병합 방법
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    1. 첫번째 병합 정렬 수행
        - 최소 원소의 부분집합이 될 때까지 분할 작업을 반복한다.
        - 즉, 1개의 원소를 가진 부분집합 여덟 개를 만든다.
        - {69}, {10}, {30}, {2}, {16}, {8}, {31}, {22}
    2. 두번째 병합 정렬 수행
        - 부분집합을 2개씩 정렬하여 하나로 결합한다.
            - 전체 원소가 하나의 집합이 되고 해당 집합에 정렬이 완료될 때까지 수행한다.
        - 수행 과정
            - {69}, {10}, {30}, {2}, {16}, {8}, {31}, {22}
            - {69, 10}, {30, 2}, {16, 8}, {31, 22} => 결합
            - {10, 69}, {2, 30}, {8, 16}, {22, 31} => 정렬
            - {10, 69, 2, 30}, {8, 16, 22, 31} => 결합
            - {2, 10, 30, 69}, {8, 16, 22, 31} => 정렬
            - {2, 10, 30, 69, 8, 16, 22, 31} => 결합
            - {2, 8, 10, 16, 22, 30, 31, 69} => 정렬
        - 결과 : [2, 8, 10, 16, 22, 30, 31, 69]

### 기수 정렬 (Radix Sort)

- 분배 방식의 정렬 방법
- 정렬할 원소의 키값에 해당하는 버킷에 원소를 분배하였다가 버킷의 순서대로 원소를 꺼내는 방법을 반복한다.
- 버킷에 원소들이 들어간 순서대로 꺼내야 하므로 선입선출 구조의 큐를 사용하여 버킷을 만든다.
- 시간 복잡도
    - O(d(n+r))
    - n
        - 정렬할 원소의 수
    - d
        - 키값의 자릿수
    - r
        - 버킷을 결정하는 기수
- 동작 규칙
    0. 10진수로 표현된 키값을 가진 원소들을 정렬할 때는 0부터 9까지 버킷을 총 10개 사용한다.
    1. 키값의 1의 자리에 대해 기수 정렬을 수행한다.
    2. 키값의 10의 자리에 대해 기수 정렬을 수행한다.
    3. 키값의 100의 자리에 대해 기수 정렬을 수행한다.
    4. 한 단계가 끝날 때마다 버킷에 분배된 원소들을 차례대로 꺼내서 다음 단계의 기수 정렬을 수행한다.
    5. 모든 원소의 정렬이 끝나면 기수 정렬을 종료한다.
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    1. 첫번째 기수 정렬 수행
        - 키값의 1의 자리에 대해서 기수 정렬을 수행한다.
        - 정렬할 원소의 키값의 1의 자리에 맞춰 버킷에 분배한다.
            - (10, 30) / (31), (2,22), (), (), () ,(16), (), (8), (69)
        - 버킷에 분배한 원소를 차례대로 꺼낸다.
            - 결과 : [10, 30, 31, 2, 22, 16, 8, 69]
    2. 두번째 기수 정렬 수행
        - 키값의 10의 자리에 대해서 기수 정렬을 수행한다.
        - 정렬할 원소의 키값의 10의 자리에 맞춰 버킷에 분배한다.
            - (2, 8), (10, 16), (22), (30, 31), (), (), (69), (), (), ()
        - 버킷에 분배한 원소를 차례대로 꺼낸다.
            - 결과 : [2, 8, 10, 16, 22, 30, 31, 69]
        - 키값의 최대 자릿수가 두 자리이므로 두번째 기수 정렬 후 전체 정렬을 종료한다.

### 힙 정렬 (Heap Sort)

- 힙 자료구조를 이용하여 정렬하는 방식
- 힙에는 항상 가장 큰 원소가 루트가 되고, 삭제 연산을 수행하면 항상 루트 노드의 원소를 삭제하여 반환하는 특징이 있다.
- 정렬 방향에 대한 연산 방법
    - 내림차순
        - 최대 힙에 대해서 원소 개수만큼 삭제 연산을 수행한다.
    - 오름차순
        - 최소 힙에 대해서 원소 개수만큼 삭제 연산을 수행한다.
- 시간 복잡도
    - O(nlog<sub>2</sub>n)
- 동작 규칙
    - 힙 정렬을 정렬할 원소들을 하나씩 힙에 삽입하여 정렬할 n개의 원소를 가진 최대 힙을 구성한다.
    - 힙에 삭제 연산을 하여 얻은 루트 원소를 저장하고, 힙을 다시 최대 힙이 되도록 재구성하는 작업을 원소의 개수만큼 반복한다.
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    0. 정렬할 원소에 대해 삽입 연산을 이용해 최대 힙을 구성한다.
        ```mermaid
        flowchart TD
            69 --- 22
            69 --- 31
            22 --- 16
            22 --- 10
            16 --- 2
            31 --- 8
            31 --- 30
        ```
    1. 첫번째 힙 정렬 수행
        - 삭제 연산을 수행하여 루트 노드의 원소 69를 구한 후 배열의 비어있는 마지막 자리에 저장한다.
        - 나머지 힙을 최대 힙으로 재구성한다.
        - 결과 : [69]
        ```mermaid
        flowchart TD
            31 --- 22
            31 --- 30
            22 --- 16
            22 --- 10
            30 --- 8
            30 --- 2
        ```
    2. 두번째 힙 정렬 수행
        - 삭제 연산을 수행하여 루트 노드의 원소 31을 구한 후 배열의 비어있는 마지막 자리에 저장한다.
        - 나머지 힙을 최대 힙으로 재구성한다.
        - 결과 : [31, 69]
        ```mermaid
        flowchart TD
            30 --- 22
            30 --- 8
            22 --- 16
            22 --- 10
            8 --- 2
        ```
    3. 세번째 힙 정렬 수행
        - 삭제 연산을 수행하여 루트 노드의 원소 30을 구한 후 배열의 비어있는 마지막 자리에 저장한다.
        - 나머지 힙을 최대 힙으로 재구성한다.
        - 결과 : [30, 31, 69]
        ```mermaid
        flowchart TD
            22 --- A[16]
            22 --- B[8]
            A --- 2
            A --- 10
        ```
    4. 네번째 힙 정렬 수행
        - 삭제 연산을 수행하여 루트 노드의 원소 22를 구한 후 배열의 비어있는 마지막 자리에 저장한다.
        - 나머지 힙을 최대 힙으로 재구성한다.
        - 결과 : [22, 30, 31, 69]
        ```mermaid
        flowchart TD
            16 --- A[10]
            16 --- B[8]
            A --- 2
        ```
    5. 다섯번째 힙 정렬 수행
        - 삭제 연산을 수행하여 루트 노드의 원소 16을 구한 후 배열의 비어있는 마지막 자리에 저장한다.
        - 나머지 힙을 최대 힙으로 재구성한다.
        - 결과 : [16, 22, 30, 31, 69]
        ```mermaid
        flowchart TD
            10 --- 2
            10 --- 8
        ```
    6. 여섯번째 힙 정렬 수행
        - 삭제 연산을 수행하여 루트 노드의 원소 10을 구한 후 배열의 비어있는 마지막 자리에 저장한다.
        - 나머지 힙을 최대 힙으로 재구성한다.
        - 결과 : [10, 16, 22, 30, 31, 69]
        ```mermaid
        flowchart TD
            8 --- 2
        ```
    7. 일곱번째 힙 정렬 수행
        - 삭제 연산을 수행하여 루트 노드의 원소 8을 구한 후 배열의 비어있는 마지막 자리에 저장한다.
        - 나머지 힙을 최대 힙으로 재구성한다.
        - 결과 : [8, 10, 16, 22, 30, 31, 69]
        ```mermaid
        flowchart TD
            2
        ```
    8. 여덟번째 힙 정렬 수행
        - 삭제 연산을 수행하여 루트 노드의 원소 2를 구한 후 배열의 비어있는 마지막 자리에 저장한다.
        - 나머지 힙으로 최대 힙으로 재구성해야 하는데 공백 힙이 됬으니 힙 정렬을 종료한다.
        - 결과 : [2, 8, 10, 16, 22, 30, 31, 69]
        ```mermaid
        flowchart TD
            A[ ]
        ```

### 트리 정렬 (Tree Sort)

- 이진 탐색 트리를 이용하여 정렬하는 방법
- 정렬할 원소들을 이진 탐색 트리로 구성하고, 중위 우선 순회 방법을 사용하여 이진 탐색트리의 순회하는 경로가 오름차순 정렬이 된다.
- 시간 복잡도
    - O(nlog<sub>2</sub>n)
- 동작 규칙
- 예시 (정렬할 자료 : [69, 10, 30, 2, 16, 8, 31, 22], 오름차순)
    1. 정렬할 원소를 차례대로 삽입하여 이진 탐색 트리를 구성한다.
        ```mermaid
        flowchart TD
            69 --- 10
            10  --- 2
            10 --- 30
            2 --- 8
            30 --- 16
            30 --- 31
            16 --- 22
        ```
    2. 이진 탐색 트리를 중위 순회 방법으로 순회하면서 원소를 저장한다.
        - 결과 : [2, 8, 10, 16, 22, 30, 31, 69]