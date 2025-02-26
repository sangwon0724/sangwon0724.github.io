---
layout: post
title:  "실제로 Redis 사용해보기"
date:   2025-02-24 07:00:00 +0900
categories:  Redis
published: false
---

### Spring의 경우

#### build.gradle

레디스를 사용하기 위해 build.gradle에 의존성을 추가하자.
{% highlight gradle %}
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
{% endhighlight %}

#### 리소스 수정하기

application.properties나 application.yaml에 레디스에 대한 설정을 추가해주자.
- `spring.data.redis.host`
    - 레디스 서버의 주소의 호스트
    - 로컬에 설치한 레디스 서버를 이용할 것이니 "localhost"로 작성하자.
- `spring.data.redis.port`
    - 레디스 서버가 사용하는 포트 번호
    - 로컬에 설치한 레디스 서버가 사용하는 기본 포트인 "6379"로 작성하자.
- `logging.level.org.springframework.cache`
    - 레디스에 대한 로그 레벨
    - 자세한 내역을 보기 위해 "trace"로 작성하자.

#### 레디스 서버 연결에 대한 환경설정

#### 레디스 캐싱에 대한 환경설정

#### 캐싱 로직 적용하기

#### 성능 비교해보기

### NextJs의 경우

### 출처

[비전공자도 이해할 수 있는 Redis 입문/실전 (조회 성능 최적화편)](https://www.inflearn.com/course/%EB%B9%84%EC%A0%84%EA%B3%B5%EC%9E%90-redis-%EC%9E%85%EB%AC%B8-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94)