---
layout: post
title:  "빈 생명주기"
date:   2023-12-15 11:46:00 +0900
categories: Spring&nbsp;Framework
---

### 빈 생명주기

- 기본적인 생명주기
    1. 생성
    2. 빈 설정 (초기화)
    3. 사용
    4. 소멸

- 기초적인 사용방법

{% highlight java %}
AnnotationConfigApplicationContext test = new AnnotationConfigApplicationContext(AnnotationBeanTest.class);
//ApplicationContext test = new ClassPathXmlApplicationContext("applicationContextTest.xml");

//빈 생성하기
test.register();

//빈 설정하기
test.refresh();

//빈 사용하기
whatever what = (whatever)test.getBean("what");

//빈을 직접 소멸시키기
test.close();

//JVM 소멸시 자동으로 소멸시키는 방법
test.registerShutdownHook();
{% endhighlight %}

### 기본적인 전제조건

- 빈에 관련된 메소드를 정의한 클래스에는 @Configuration 어노테이션을 추가해야 한다.

### 빈 생명주기 사용방법 1 : 인터페이스 활용하기

- 빈 초기화 하기
    - InitializingBean 인터페이스를 활용한다.
    - afterPropertiesSet()가 초기화를 지원한다.
    - 빈이 생성되면 afterPropertiesSet()가 자동으로 실행되어 빈이 초기화된다.

- 빈 소멸하기
    - DisposableBean 인터페이스를 활용한다.
    - destroy() 메소드가 소멸을 지원한다.
    - 빈의 사용이 완료되면 destroy() 메소드가 자동으로 실행되어 빈이 소멸된다.

- 인터페이스를 활용하는 방법의 장단점
    - 스프링 전용 인터페이스에 해당 코드가 의존한다.
    - 초기화, 소멸 메소드의 이름을 변경할 수 없다.
    - 내가 코드를 고칠수 없는 외부 라이브러리에 적용할 수 없다.
    - 이 방법은 스프링 초창기에 나온 방법이라서 지금은 거의 사용하지 않는 방법이다.

### 빈 생명주기 사용방법 2 : 사용자 정의 메소드 활용하기

- 빈 초기화 하기 + 소멸하기
    - 해당 클래스에서 빈을 초기화할 때의 메소드와 소멸할 때의 메소드를 직접 정의한다.

- 사용방법
    - BeanLifeCycle이라는 이름의 빈 메소드를 정의한 클래스를 생성했다고 가정한다.
    - 해당 클래스인 BeanLifeCycle을 사용하는 코드의 위쪽에 @Bean 어노테이션을 추가한다.
    - @Bean 어노테이션의 속성으로 initMethod와 destroyMethod를 추가한다.
    - 각 속성의 값은 빈 관련 메소드를 작성했던 클래스인 BeanLifeCycle에서 자신이 작성한 각각의 빈 초기화 메소드와 빈 소멸 메소드의 이름을 작성한다.

- 사용자 정의 메소드 활용하는 방법의 특징
    - 메소드의 이름을 자유롭게 줄 수 있다.
    - 스프링 빈이 스프링 코드에 의존하지 않는다.
    - 코드가 아니라 설정 정보를 사용하기 때문에
    코드를 고칠 수 없는 외부 라이브러리에도 적용시킬 수 있다.

- @Bean 어노테이션의 destroyMethod 속성의 기본 값
    - @Bean 어노테이션의 destroyMethod 속성은 기본 값이 (inferred)로 등록되어 있다.
    - (inferred)는 close와 shutdown이라는 메소드를 자동으로 호출해서 빈을 소멸시켜 준다.
    - 따라서 해당 방법을 이용시에는 빈 소멸메소드를 따로 만들지 않아도 잘 작동한다.

### 빈 생명주기 사용방법 3 : 어노테이션 활용하기

- 빈 초기화 하기
    - 본인이 작성한 빈 초기화 메소드에 @PostConstruct 어노테이션을 추가한다.

- 빈 소멸 하기
    - 본인이 작성한 빈 소멸 메소드에 @PreDestroy 어노테이션을 추가한다.

- 사용하기
    - BeanLifeCycle이라는 이름의 빈 메소드를 정의한 클래스를 생성했다고 가정한다.
    - 해당 클래스인 BeanLifeCycle을 사용하는 코드의 위쪽에 @Bean 어노테이션을 추가한다.
    - 해당 방법에서는 @Bean 어노테이션에 속성을 추가하지 않아도 된다.

- 어노테이션을 사용하는 방법의 특징
    - 어노테이션만 붙이면 되니 매우 간편하다.
    - 스프링에 종속적인 기술이아는 자바 표준 기술이기 때문에 스프링이 아닌 다른 컨테이너에서도 잘 작동한다.
    - 컴포넌트 스캔과 잘 어울린다.
    - 외부 라이브러리에는 적용하지 못한다.
    - 외부 라이브러이를 초기화나 소멸시키고 싶을 때에는 @Bean의 기능을 사용하면 된다.
    - 최신 스프링에서 가장 권장하는 방법이다.