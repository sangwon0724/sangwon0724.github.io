---
layout: post
title:  "부하 테스트를 통한 Redis 성능 확인"
date:   2025-02-27 17:17:00 +0900
categories:  Redis
---

### 부하 테스트

백앤드 서버를 구현했다면 그 안에는 여러가지 서비스가 포함되어 있을 것이다.  
그 중에서도 인기있는 서비스가 있을텐데  
만약 사용자가 해당 서비스에 몰린다면 서버가 견디지 못 해서  
전체 서비스가 다운될 수도 있을 것이다.

그래서 이를 방지하기 위해서는 구현한 서비스가  
어느 정도의 요청까지 견딜수 있는 지 미리 테스트해봐야 한다.  
이러한 테스트를 `부하 테스트`라고 한다.  
정확한 부하 테스트의 뜻은  
`임계값 한계에 도달할 때까지 시스템의 부하를 지속적으로 꾸준히 증가시켜 시스템의 성능을 시험하는 것`이다.

#### 관련 용어

- Throughput
    - 서비스가 1초당 처리할 수 있는 작업량
    - 단위 : TPS
- TPS
    - Transaction Per Seconds
    - 1초당 처리한 트랜잭션의 수

### k6

#### k6 설치하기 (Windows OS 기준)

[참고](https://grafana.com/docs/k6/latest/set-up/install-k6/)

1. CMD 창에서 `winget install k6 --source winget` 실행해서 k6 설치
2. k6가 설치된 경로로 이동
    - 별도 설정이 없을 경우 `cd C:\Program Files\k6`
3. `k6`를 실행해서 k6 로고가 보이는 지 확인

#### 테스트를 위한 스크립트 작성하기

k6가 설치된 경로로 이동해서 `script.js`를 작성하자.
{% highlight js %}
import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  http.get('테스트할 API 주소');
}
{% endhighlight %}

#### 부하 테스트 실행하기

k6가 설치된 경로로 이동해서 아래 명령어를 실행하자.
{% highlight bash %}
k6 run --vus 30 --duration 10s script.js
{% endhighlight %}

`--vus 30`에서 `vus`는 `Virtual Users`의 줄임말로  
가상의 유저 30명이 요청을 보내는 것처럼 부하를 생성한다는 뜻이다.

`--duration 10s`는 테스트를 30초간 진행한다는 뜻이다.

테스트를 진행하면 `http_reqs`라는 항목 뒤에 흐릿한 하늘색으로  
`숫자/s`라고 수치가 나오는데,  
이 값이 해당 서비스가 1초에 처리할 수 있는 요청의 처리 개수를 의미한다.

만약에 결과값이 `30/s`라고 나온다면  
해당 서비스의 Throughput이 30TPS라고 할 수 있다.

### 출처

[비전공자도 이해할 수 있는 Redis 입문/실전 (조회 성능 최적화편)](https://www.inflearn.com/course/%EB%B9%84%EC%A0%84%EA%B3%B5%EC%9E%90-redis-%EC%9E%85%EB%AC%B8-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94)