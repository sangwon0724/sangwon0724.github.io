---
layout: post
title:  "Redis 사용법 (기초편)"
date:   2025-02-25 16:19:00 +0900
categories:  Redis
---

### 다양한 자료구조

레디스에서는 String, Lists, Sets 등 다양한 자료구조를 제공한다.  
전부 다 습득하기에는 오래 걸리니까 가장 기본이 되는 자료구조인 String을 통해  
레디스에 대한 기본기를 습득하자.

참고로 레디스는 자료구조마다 사용되는 명령어가 다른데,  
자료구조마다 명령어가 다를 뿐 각 명령어가 수행하는 역할군은  
SQL의 DML처럼 CRUD로 정해져있다.

### 데이터 저장하기

데이터를 저장할 때는 `set [키 이름] [값]`을 실행하면 된다.  
`SET` 명령어 자체가 `Strings` 자료구조에 대한 명령어이기 때문에  
별도로 문자열임을 표시하기 위해 쌍따옴표를 붙일 필요는 없다.
하지만 값을 설정할 때 띄워쓰기가 들어간다면 쌍따옴표로 묶어줘야 한다.

#### 쌍따옴표를 붙이는 이유

예를 들어 취미가 게임이라는 데이터를 저장하기 위해 `set hobby game`이라고 저장해보자.  
이 때는 문제없이 저장될 것이다.  
`SET` 명령어 자체가 `Strings` 자료구조에 대한 명령어이기 때문에  
"game"이라는 값은 자동으로 문자열로 저장되기 때문이다.

하지만 만약에 취미를 게임하기라고 구체적으로 적기 위해 "play game"이라고 저장하려고 하면 어떻게 될까?  
실제로 `set hobby play game`을 실행해보면  
`(error) ERR syntax error`라는 오류 메시지를 반환하면서 명령어 실행에 실패할 것이다.

사실 어찌보면 당연한건데 레디스만 그런게 아니라 SQL에서도 동일하게  
명령어를 조합해서 명령문을 만드는 것인데  
띄워쓰기로 구분해버리면 레디스 입장에서는 당연히 명령어인 줄 알고 실행할 것이다.

그래서 정확하게 데이터의 범위를 지정하기 위해  
쌍따옴표로 묶는 것이다.  
아까의 예시의 경우에는 `set hobby "play game"`처럼 명령문을 작성하면 된다.

#### 데이터 만료시간 설정하기

데이터를 영구적으로 저장하는 일반적인 RDBMS와 다르게  
레디스에서는 데이터를 특정 시간동안만 저장하게 할 수 있다.  
이 때의 특정 시간을 `만료시간(TTL, Time To Live)`이라고 부른다.

만료시간을 포함해 데이터를 저장하려면 `set [키 이름] [값] ex [만료시간]`을 실행하면 된다.  
이 때의 만료시간의 단위는 초 단위다.  
만약에 취미가 게임하기라는 데이터를 30초 동안만 저장하고 싶다면  
`set hobby "play game" ex 30`처럼 명령문을 작성하면 된다.

#### 만료시간 확인하기

특정 데이터의 잔여 만료시간을 확인하고 싶다면 `ttl [키 이름]`을 실행하면 된다.  
시간이 남아있다면 남은 시간을, 시간이 종료되었다면 "-2"를 출력한다.  
"-1"은 만료시간을 설정하지 않은 데이터에 대해서 만료시간을 조회했을 때 출력한다.

### 데이터 조회하기

데이터를 조회할 때는 `get [키 이름]`을 실행하면 된다.  
참고로 없는 데이터를 조회한다면 `(nil)`이라고 출력된다.

### 키 목록 조회하기

키 목록을 조회할 때는 `keys [패턴]`을 실행하면 된다.  
모든 키 목록을 조회하기 싶다면 `keys *`를 실행하면 된다.  
만약에 아까 만든 "hobby"라는 키를 조회싶다면 `keys ho*`처럼 실행하면  
"ho"라는 문자열로 시작하는 모든 키 목록을 조회할 수 있다.

### 데이터 삭제하기

데이터를 삭제할 때는 `del [키 이름]`을 실행하면 된다.  
데이터 삭제에 성공한다면 `(integer) 1`라는 메시지를 출력한다.

만약에 존재하지 않는 데이터를 삭제한다면 `(integer) 0`이라고 출력된다.

#### 모든 데이터 삭제하기

모든 데이터를 삭제하고 싶다면 `flushall`을 실행하면 된다.

### 키 네이밍 컨벤션

회사마다 업무 규칙이 다르긴 하지만  
결국 중요한 것은 키의 이름을 작성할 때는 일원화된 이름으로 작성하는 것이다.

예를 들어 `:`를 통해 구분한다고 생각해보자.  
`users:100:name`이라는 키가 있다면 어떨까?  
바로 사용자들 중에서 PK 값이 100번인 사용자의 이름을 의미한다는 것을 눈치챌 수 있을 것이다.

이처럼 고유하며 특징이 있는 이름으로 짓는 것이 중요하다.  
그러면 아래와 같은 장점을 얻을 수 있다.
- 가독성
    - 데이터의 의미와 용도를 쉽게 파악할 수 있다.
- 일관성
    - 컨벤션을 따름으로써 코드의 일관성이 높아지고 유지보수가 쉬워진다.
- 검색 용이성
    - `keys` 명령어 실행 시 패턴을 사용할 수 있다는 점을 통해 특정 유형의 키를 쉽게 찾을 수 있다.
- 확장성
    - 고유한 키 이름을 만들 수 있는 명명 규칙을 만들어 두면 서비스가 확장되어도 키가 충돌될 걱정이 없다.

### 출처

[비전공자도 이해할 수 있는 Redis 입문/실전 (조회 성능 최적화편)](https://www.inflearn.com/course/%EB%B9%84%EC%A0%84%EA%B3%B5%EC%9E%90-redis-%EC%9E%85%EB%AC%B8-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94)