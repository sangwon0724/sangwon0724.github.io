---
layout: post
title:  "실제로 Redis 사용해보기"
date:   2025-02-24 07:00:00 +0900
categories:  Redis
published: false
---

### Spring의 경우

#### 라이브러리 추가하기

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

`Lettuce`라는 라이브러리를 통해 레디스와의 연결을 관리할 수 있다.  
`RedisStandaloneConfiguration` 클래스를 통해 레디스 연결에 대한 환경설정을 진행하고,  
방금 생성한 `RedisStandaloneConfiguration` 클래스를 파라미터로 넘겨서  
레디스의 연결을 관리하는 `LettuceConnectionFactory` 클래스를 생성하자.  
마지막으로 `@Bean` 애노테이션을 통해 `LettuceConnectionFactory`를 빈 컨테이너에 등록하면  
레디스 서버가 연결된다.

{% highlight java %}
@Bean
public LettuceConnectionFactory redisConnectionFactory() {
    RedisStandaloneConfiguration config = new RedisStandaloneConfiguration();
    return new LettuceConnectionFactory(config);
}
{% endhighlight %}

`RedisStandaloneConfiguration` 클래스의 인스턴스를 기본 생성자를 통해 생성하게 되면 아래와 같은 정보를 가진다.
- `hostname`
    - 연결할 레디스 서버의 호스트
    - 기본값 : localhost
- `port`
    - 연결할 레디스 서버의 포트
    - 기본값 : 6379
- `username`
    - 연결할 레디스 서버의 계정명
    - 기본값 : null
- `password`
    - 연결할 레디스 서버의 계정 비밀번호
    - 기본값 : RedisPassword.none()
- `database`
    - 연결할 레디스 서버 내부의 데이터베이스
    - 레디스는 하나의 서버에 0번에서 15번까지 최대 16개까지의 데이터베이스를 가질 수 있다.
    - 기본값 : 0

`RedisStandaloneConfiguration` 클래스의 각 필드는 getter 메소드와 setter 메소드가 존재하기 때문에,  
자유롭게 값을 설정하고 가져올 수 있다.

`LettuceConnectionFactory` 클래스에도 getter 메소드와 setter 메소드가 존재하기 때문에,  
서버를 연결할 때 필요한 추가 설정은 `LettuceConnectionFactory` 클래스에 하면 된다.  
`RedisStandaloneConfiguration` 클래스는 이름은 환경설정이지만  
사실상 일반적인 데이터소스를 설정한다고 보면 된다.

`RedisStandaloneConfiguration` 클래스를 살펴보면 알겠지만  
hostname만 넘기거나, hostname이랑 port를 같이 넘기는 생성자도 있다.  
굳이 setter 메소드를 사용하지 않고 생성자를 통해 값을 설정할 수도 있다.

{% highlight java %}
@Bean
public LettuceConnectionFactory redisConnectionFactory() {
    return new LettuceConnectionFactory(new RedisStandaloneConfiguration(host, port));
}
{% endhighlight %}

#### 레디스 캐싱에 대한 환경설정

레디스 캐싱에 대한 환경설정을 하려면  
우선 환경설정용 클래스에 `@EnableCaching` 애노테이션을 추가해서  
스프링 부트의 캐싱 설정을 활성화해줘야 한다.

그런 다음에 캐시를 관리하는 관리자 역할인 `CacheManager` 인터페이스를  
빈으로 등록해주면 된다.

{% highlight java %}
@Bean
public CacheManager redisCacheManager(RedisConnectionFactory redisConnectionFactory) {
    RedisCacheConfiguration redisCacheConfiguration = 
        RedisCacheConfiguration
        .defaultCacheConfig()
        .serializeKeysWith(
            RedisSerializationContext.SerializationPair.fromSerializer(
                new StringRedisSerializer()
            )
        ) 
        .serializeValuesWith(
            RedisSerializationContext.SerializationPair.fromSerializer(
                new Jackson2JsonRedisSerializer<Object>(Object.class)
            )
        )
        .entryTtl(Duration.ofMinutes(1L)); // 데이터의 만료기간(TTL)을 1분으로 설정

    return RedisCacheManager
            .RedisCacheManagerBuilder
            .fromConnectionFactory(redisConnectionFactory)
            .cacheDefaults(redisCacheConfiguration)
            .build();
}
{% endhighlight %}

우선 캐시에 대한 환경설정을 구성해줘야 한다.  
`RedisCacheConfiguration.defaultCacheConfig()` 메소드를 통해 기본 구성을 생성하고,  
`serializeValuesWith()` 메소드와 `serializeValuesWith()` 메소드를 통해  
데이터를 저장하기 위한 어댑터를 설정하고,  
`entryTtl()` 메소드를 통해 캐시의 만료시간을 설정한다.

이 때 `serializeValuesWith()` 메소드는 레디스에 key를 저장할 때  
String으로 직렬화해서 저장하기 위한 어댑터를 등록하는 역할을 하고,  
`serializeValuesWith()` 메소드는 레디스에 value를 저장할 때  
Json으로 직렬화해서 저장히기 위한 어댑터를 등록하는 역할을 한다.  
보통 `StringRedisSerializer`와 `Jackson2JsonRedisSerializer`를 많이 사용한다.

#### 캐싱 로직 적용하기

스프링 부트에서 캐시를 적용하는 것은 매우 간단하다.  
데이터를 반환하는 메소드에 `@Cacheable` 애노테이션을 적용하면 된다.

만약에 게시글 목록 데이터를 조회하는 메소드가 있다고 가정해보자.  
페이징을 위해서 페이지 번호와 페이지 단위가 필요할 것이고,  
그러면 페이지 번호와 페이지 단위를 각각 `int page`와 `int size`처럼  
메소드 시그니처에 정의했을 것이다.

위와 같은 메소드가 있다고 가정한다면  
`@Cacheable` 애노테이션은 아래와 같이 적용할 수 있을 것이다.
{% highlight java%}
@Cacheable(cacheNames = "getBoards", key = "'boards:page:' + #page + ':size:' + #size", cacheManager = "redisCacheManager")
{% endhighlight %}

여기서 `cacheNames`와 `key`라는 속성을 통해 실제 레디스의 key가 생성된다.  
`key` 속성에는 `#변수명`처럼 값을 동적으로 대입할 수 있는데,  
여기에는 `#변수명`에 설정한 변수명이 메소드 시그니처에 있는 필드 중에 동일한 게 있다면  
그 값을 자동으로 대입해준다.  
만약에 page가 3이고, size가 10이라면  
실제 레디스에 저장되는 key는 `getBoards::boards:page:3:size:10`이 되는 것이다.

참고로 `cacheNames`에 보면 `s`가 있는 것을 볼 수 있다.  
중괄호처럼 묶어서 `cacheNames`에 `{"cacheName1", "cacheName2"}`처럼 넣을 수 있다.  
그러면 하나의 캐시를 생성할 때 `cacheName1::~`와 `cacheName2::~`와 같이  
2가지 캐시를 생성할 수 있다.

`cacheManager`에는 빈으로 등록한 `CacheManager` 인터페이스의 빈 이름을 작성하면 된다.

#### 성능 비교해보기

성능 비교를 위해 아주 간단하게 PK, 제목, 내용, 작성일 정도만 있는 테이블을 만들어서  
100만 건 정도 데이터를 넣어보자.  
그리고 별도의 조건 없이 최근 10건을 조회하는 간단한 API를 만들어보자.

이제 캐시를 적용하지 않은 상황과 캐시를 적용한 상황을 만들어서  
캐시의 만료시간을 1분으로 설정했다고 가정해서  
각 상황마다 1분 안에 5번씩 실행해보자.

캐시를 적용하지 않고 API를 실행한 경우 (총합 : 6,409 ms)
1. 1,689 ms
2. 1,028 ms
3. 1,395 ms
4. 1,164 ms
5. 1,132 ms

캐시를 적용하고 API를 실행한 경우 (총합 : 2,428 ms)
1. 2.32 s (2,327 ms)
2. 61 ms
3. 17 ms
4. 12 ms
5. 11 ms

캐시를 사용하지 않는 경우에는 항상 DB에 직접 요청하기 때문에  
네트워크나 DB의 상황에 따라 시간이 줄어들기도 하고 늘어나기도 하고  
매우 들쯕날쭉한 상황이다.  
그런데 캐시를 사용하는 경우에는 최초 조회 시 캐시를 저장하는 과정때문에  
캐시를 사용하지 않는 경우보다 속도가 좀 걸리긴 했지만,  
대신에 캐시를 사용할 때마다 레디스 내부의 스케쥴링 방식을 통해서  
점점 응답 속도가 빨라지는 것을 확인할 수 있다.

5번 호출했을 때의 응답시간의 총합을 비교해보면  
무려 약 62.1% 정도나 빨라진 것을 알 수 있다.

### NextJs의 경우

#### 라이브러리 추가하기

#### 리소스 수정하기

#### 레디스 서버 연결에 대한 환경설정

#### 레디스 캐싱에 대한 환경설정

#### 캐싱 로직 적용하기

### 캐시 is not 만능

캐시가 무조건 만능은 아니다.  
항상 적합한지 확인하고 캐시를 적용해야 한다.

만약에 뭔가 사이트 메인 같은 곳에서 최신 공지 게시글 5개를 가져온다고 생각해보자.  
공지 게시글이 자주 등록되는 일은 없으니 캐시에 적합한 데이터다.  
그런데 아까 테스트를 위한 예시처럼 일반 게시글이라고 생각해보자.  
사람들이 자주 이용하는 게시판이거나 데이터가 엄청 많은 경우에는  
데이터가 자주 변경될 수 있기 때문에 캐시로 적합한 경우는 아니다.

그리고 애초에 캐시가 먼저가 아니라 SQL 튜닝을 먼저 하는 게 우선이다.  
우선 SQL 튜닝을 먼저 하고,  
여러 가지 최적화 방법 중에 캐시 적용이 가장 적절한지 확인하고,  
그 다음에 캐시로 저장하는 게 적합한지 확인하는 것이 베스트다.

### 출처

[비전공자도 이해할 수 있는 Redis 입문/실전 (조회 성능 최적화편)](https://www.inflearn.com/course/%EB%B9%84%EC%A0%84%EA%B3%B5%EC%9E%90-redis-%EC%9E%85%EB%AC%B8-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94)