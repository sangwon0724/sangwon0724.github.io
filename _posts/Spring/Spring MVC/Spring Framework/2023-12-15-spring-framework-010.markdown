---
layout: post
title:  "스프링 3대 요소 - 의존성 주입 (DI)"
date:   2023-12-15 13:05:00 +0900
categories: Spring&nbsp;MVC
tags: [스프링 3대 요소, 의존성 주입, DI]
---

### 정의

- 어떤 객체에 스프링 컨테이너가 또 다른 객체와 의존성을 맺어주는 행위
- DI : Dependency Injection

### 기본적인 사용법

{% highlight java %}
public class TestA{ }

@Component
public class TestB{ }

public static void main(String[] args) {
    TestA testA = new TestA();

    @Autowired
    TestB testB;
}
{% endhighlight %}

### @Autowired 어노테이션

- 해당하는 타입의 객체를 찾아서 자동으로 할당하는 어노테이션
- 생성자, 메소드, 멤버변수 위에 모두 사용 가능
- 스프링 컨테이너는 @Autowired가 붙어 있는 것을 확인하는 순간 해당 변수의 타입을 체크하고  
그 타입의 객체가 메모리 상에 존재하면 해당 변수에 객체를 대입한다.
- 만약 @Autowired를 선언한 것에 대한 객체가 존재하지 않는 타입이라면 NoSuchBeanDefinitionException이 발생한다.
- 탐색 순서 : 타입 -> 이름 -> @Qualifier -> 실패
- 만약 찾는 빈 객체가 없는 경우 발생하는 예외를 피하고 싶다면 @Autowired(required=false)처럼 쓰면 된다.
- @Autowired(required=false)를 통해 찾는 객체가 없는 경우에 대한 null 처리 소스도 작성해야 한다.

### @Qualifier 어노테이션

- @Autowired와 함께 사용하는 어노테이션
- 특정 객체의 이름을 사용하여 의존성 주입할 때 사용
- 인터페이스에 대해 @Autowired가 실행됬을 때, 적절한 빈을 컨테이너가 찾지 못하는 경우에 사용한다.
- @Qualifier를 사용하여 직접 빈의 이름을 지정하여 컨테이너가 어떤 객체를 주입할지 선택할 수 있게 해준다.
- 빈이 등록된 xml 파일에서 미리 qualifier 태그를 통해 지정을 해둬야 한다.
- 빈 자체의 id가 아닌 qualifier 태그에 명시한 value를 통해 이름을 지정한다.
- @Autowired를 먼저 사용한 후 @Qualifier("명칭")을 사용하면 된다.

### @Inject 어노테이션

- 해당하는 타입의 객체를 찾아서 자동으로 할당하는 어노테이션
- 생성자, 메소드, 멤버변수 위에 모두 사용 가능
- 탐색 순서 : 타입 -> @Named-> 이름 -> 실패

### @Named 어노테이션

- @Inject 함께 사용하는 어노테이션
- 특정 객체의 id를 사용하여 의존성 주입할 때 사용
- @Inject 먼저 사용한 후 @Named("id명")을 사용하면 된다.

### @Resource 어노테이션

- 주입하려고 하는 객체의 id가 일치하는 객체를 자동으로 주입한다.
- 메소드, 멤버변수 위에 사용 가능
- 사실상 @Autowired + @Qualifier
- 탐색 순서 : 이름 -> 타입 -> @Qualifier -> 실패
- @Resource나 @Resource(name="등록된 빈의 id")로 사용한다.
- &lt;context:annotation-config/>를 xml 파일에 추가해야지 사용할수 있다.