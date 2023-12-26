---
layout: post
title:  "스프링 3대 요소 - 관점 지향 프로그래밍 (AOP)"
date:   2023-12-15 13:08:00 +0900
categories: Spring&nbsp;Framework
tags: [스프링 3대 요소, 관점 지향 프로그래밍, AOP]
---

### 정의

- AOP (Aspect Oriented Programming) : 관점지향적 프로그래밍
- 기능을 비즈니스 로직과 공통 모듈로 구분한 뒤에  
개발자의 코드 밖에서 필요한 시점에  
비즈니스 로직에 삽입하여 실행되도록 하는 방법
- OOP를 더욱 보완 확장하여 OOP를 OOP답게 사용할 수 있도록 도와주는 개념
- DI가 의존성의 주입이라면, AOP는 기능의 주입이다.

### AOP가 필요한 이유

- 중복을 최대한 줄여서 적은 량의 코드 수정만으로도 프로젝트의 전체적인 부분을 변경할 수 있도록 하기 위해서

### 특징

- 중복되는 코드가 줄어든다.
- 프로젝트의 유지보수를 효율적으로 할 수 있다.
- 생산성이 높아진다.
- 재활용성이 극대화된다.
- 변화에 대한 수용성이 높아진다.

### AOP 용어

- Joinpoint
    - Advice를 적용가능한 지점
    - 특정 작업이 실행되는 시점
    - 스프링은 프록시를 이용해서 AOP를 구현하기 때문에 필드 값 변경에 대한 Joinpoint는 불가능하다.
    - 메소드 호출에 대한 Joinpoint 가능
- Aspect
    - 여러 객체에 공통으로 적용되는 기능
    - 일정한 패턴을 가지는 클래스에 Advice를 적용하도록 지원할 수 있는 것
    - Advice + Pointcut
    - 예시) 트랜잭션, 로그, 보안, 인증 등등
- Weaving
    - AOP에서 Joinpoint들을 Advice로 감싸는 과정
    - Weaving 하는 작업을 도와주는 것이 AOP Tool의 역할이다.
- Advice
    - Joinpoint에서 실행되어야 하는 코드
- Target
    - 실질적인 비즈니스 로직을 구현하고 았는 코드
    - Advice를 받을 대상
    - 비즈니스 로직을 수행하는 클래스 또는 프록시 객체
- Pointcut
    - 실제 Advice가 적용되는 Joinpoint
    - Joinpoint의 부분 집합
    - 스프링에서는 정규식이나 AspectJ 문법을 이용해서,
    Target 클래스와 Advice가 결합 (Weaving) 될 때
    둘 사이의 결합 규칙을 정의할 수 있다.

### AOP 관련 어노테이션

- Aspect : AOP 적용시 사용하는 어노테이션
- @Before : AOP 메소드 호출의 이전에 대한 어노테이션
- @After : AOP 메소드 호출의 이후에 대한 어노테이션
- @Around : AOP 이전/이후 모두에 대한 어노테이션
- @AfterReturning : AOP 메소드의 호출이 정상일 때에 대한 어노테이션
- @AfterThrowing : AOP시 해당 메소드가 예외발생하는 경우에 대한 어노테이션

### AOP 적용 방법

{% highlight java %}
/* 추후 작성 */
{% endhighlight %}