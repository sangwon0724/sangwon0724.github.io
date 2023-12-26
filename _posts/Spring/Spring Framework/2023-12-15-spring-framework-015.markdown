---
layout: post
title:  "인터셉터와 필터"
date:   2023-12-15 13:15:00 +0900
categories: Spring&nbsp;Framework
tags: [인터셉터, 필터]
---

### 정의 (인터셉터)

- 컨트롤러에 들어오는 요청인 HttpRequest와 컨트롤러가 응답하는 HttpResponse를 가로채는 역할

### 환경설정 (인터셉터)

1. 인터셉터 클래스 구현하기
    - HandlerInterceptorAdapter 상속받기
        - preHandle() : 컨트롤러로 보내기 전에 처리하는 인터셉터, return 값이 false면 컨트롤러로 요청을 안한다.
        - postHandle() : 컨트롤러의 handler가 끝나면 처리된다.
        - afterCompletion() : 뷰까지 처리가 끝난 후에 처리된다.

2. spirng-servlet.xml에 인터셉터 태그를 통해서 사용 설정하기
    {% highlight xml %}
    <mvc:interceptors>
        <mvc:interceptor>
            <mvc:mapping path="/**" /> 
            <bean class="com.project.util.MyInterceptor" />
        </mvc:interceptor>
    </mvc:interceptors>
    {% endhighlight %}

### 정의 (필터)

- 추후 작성

### 환경 설정 (필터)

- 추후 작성

### 인터셉터와 필터의 차이

- 인터셉터
    - 호출 시점 : DispatcherServlet이 실행된 후
    - 설정 위치 : spirng-servlet.xml
    - 구현 방식 : 설정 + 메소드 구현

- 필터
    - 호출 시점 : DispatcherServlet이 실행되기 전
    - 설정 위치 : web.xml
    - 구현 방식 : 설정