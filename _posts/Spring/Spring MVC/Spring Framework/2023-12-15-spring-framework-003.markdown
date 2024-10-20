---
layout: post
title:  "스프링 빈"
date:   2023-12-15 11:43:00 +0900
categories: Spring&nbsp;MVC
---

### 스프링 컨테이너

- 스프링 컨테이너
    - 주입을 이용해서 객체를 관리하는 컨테이너
- 스프링 컨테이너의 역할
    - 빈의 생성과 관계, 사용, 생명 주기등을 관리
- 스프링 컨테이너 사용 이유
    - 종속객체 주입을 이용하여 애플리케이션을 구성하는 컴포넌트들을 관리한다.
- 스프링 컨테이너 종류
    - 빈 팩토리
        - DI의 기본사항을 제공하는 가장 단순한 컨테이너 팩토리 디자인 패턴을 구현한 것
        - 빈을 생성하고 분배하는 책임을 지는 클래스
        - 빈의 정의는 반드시 로딩한다.
        - 빈 자체가 필요하게 되기 전까지는 인스턴스화를 하지 않는다. (lazy loading, 게으른 호출)
    - 어플리케이션 컨텍스트
        - 빈 팩토리와 유사한 하지만 좀 더 많은 기능을 제공하는 컨테이너
        - 국제화가 지원되는 텍스트 메시지를 관리해준다.
        - 이미지같은 파일 자원을 로드할 수 있는 포괄적인 방법을 제공해준다.
        - 리너스로 등록된 빈에게 이벤트 발생을 알려준다.
        - 대부분의 어플리케이션에서는 빈 팩토리보다 어플리케이션 컨텍스트를 사용하는 것이 좋다.

### 빈 팩토리 사용법

- getBean()이 호출되면, 팩토리는 의존성 주입을 이용해 빈을 인스턴스화 하고 빈의 특성을 설정하기 시작한다.

{% highlight java %}
BeanFactory bf = new XmlBeanFactory(new FileInputStream("beanFactoryTest.xml"));

testBean testbean = (testBean) bf.getBean("testbean");
{% endhighlight %}

### 어플리케이션 컨텍스트 사용법

- ClassPathXmlApplicationContext
    - 클래스패스에 위치한 xml 파일에서 컨텐스트 정의 내용을 읽어들인다.
- FileSystemxmlApplicationContext
    - 파일 경로로 지정된 xml 파일에서 컨텐스트 정의 내용을 읽어들인다.
- XmlWebApplicationContext
    - 웹 어플리케이션에 포함된 xml 파일에서 컨텐스트 정의 내용을 읽어들인다.
{% highlight java %}
ApplicationContext AC = new ClassPathXmlApplicationContext("context/contextBean.xml");

testBean testbean = AC.getBean("testbean");
{% endhighlight %}

### 빈 팩토리와 어플리케이션 컨텍스트의 차이점

- 빈 팩토리
    - 처음으로 getBean()이 호출된 시점에서야 해당 빈을 생성
- 애플리케이션 컨텍스트
    - 컨텍스트 초기화 시점에 모든 싱글톤 빈을 미리 빈을 생성해 놓아 빈이 필요할 때 즉시 사용할 수 있도록 보장

### xml 파일을 통한 빈 등록하기

- bean 태그
    - id : 등록하는 빈의 고유 명칭
    - class : 등록하는 빈의 실제 형식
- property 태그 (Setter를 통한 의존 관계가 있는 Bean 주입시 사용)
    - name : 지정할 속성의 이름
    - value : 지정할 속성의 값
    - ref : 지정할 속성이 참조하는 빈의 id
- constructor-arg 태그 (생성자를 통한 의존 관계가 있는 Bean 주입시 사용)
    - ref : 지정할 속성이 참조하는 빈의 id
- qualifier 태그
    - value : @Qualifier("명칭")에서 사용할 이름
    
{% highlight xml %}
<bean id="beanTest" class="com.example.practice.beanTest">
    <property name="ref" ref="refTest"/>
    <property name="whatever" value="whatever"/>
</bean>

<bean id="refTest" class="com.example.practice.refTest"/>

<bean id="qualifierTest1" class="com.example.practice.qualifierTest">
    <qualifier value="target"/> 
</bean>
<bean id="qualifierTest2" class="com.example.practice.qualifierTest"/>
{% endhighlight %}