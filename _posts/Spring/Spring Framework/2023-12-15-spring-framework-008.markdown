---
layout: post
title:  "컴포넌트 스캔"
date:   2023-12-15 13:01:00 +0900
categories: Spring&nbsp;Framework
tags: [컴포넌트 스캔]
---

### 정의

- 스프링에서 제공하는 설정 정보가 없어도 자동으로 스프링 빈을 등록하는 기능

### 기본적인 사용방법

- 클래스에 @ComponentScan 어노테이션을 추가한다.
- 빈으로 등록할 대상에 @Component 어노테이션을 추가한다.

### 특정 대상을 컴포넌트 스캔 대상에서 제외하는 방법

- @ComponentScan 어노테이션의 excludeFilters 속성을 추가한다.
- excludeFilters의 값으로 @Filter 어노테이션을 추가한다.
- @Filter 어노테이션의 속성인 type과 classes에  
각각 FileterType.ANNOTATION과 스캔 대상에서 제외할 클래스의 명을 작성한다.
- 특수한 경우에만 사용한다.
{% highlight java %}
@Configuration
@ComponentScan(
    excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = Configuration.class)
)
public class ComponentSscanTest {

}
{% endhighlight %}

### 탐색할 패키지의 시작 위치를 지정하는 방법

- @ComponentScan 어노테이션에 basePackages 속성을 준다.
    - 예시) @ComponentScan(basePackages = "com.practice")
- 2개 이상의 패키지를 지정하고 싶을 때는 {}를 사용한다.
    - 예시) @ComponentScan(basePackages = {"com.practiceA", "com.com.practiceB"})

### 컴포넌트 스캔의 특징
- basePackages 속성을 지정하지 않으면 @ComponentScan 어노테이션이 붙은 설정 정보 클래스의 패키지가 시작 위치가 된다.


### 컴포넌트 스캔의 기본 대상

- @Component 어노테이션 : 컴포넌트 스캔에서 사용
- @Controlller 어노테이션 : 스프링 MVC 컨트롤러에서 사용
- @Service 어노테이션 : 스프링 비즈니스 로직에서 사용
- @Repository 어노테이션 : 스프링 데이터 접근 계층에서 사용
- @Configuration 어노테이션 : 스프링 설정 정보에서 사용


### 컴포넌트 스캔의 필터 기능

- includeFilters 속성 : 컴포넌트 스캔 대상을 추가로 지정한다.
- excludeFilters 속성 : 컴포넌트 스캔에서 제외할 대상을 지정한다

### @Filter 어노테이션의 type 속성의 종류

- FilterType.ANNOTATION: 기본값, 애노테이션을 인식해서 동작한다.
- FilterType.ASSIGNABLE_TYPE: 지정한 타입과 자식 타입을 인식해서 동작한다.
- FilterType.ASPECTJ: AspectJ 패턴 사용
- FilterType.REGEX: 정규 표현식
- CUSTOM: TypeFilter 이라는 인터페이스를 구현해서 처리