---
layout: post
title:  "설정 파일 - root-context.xml"
date:   2023-12-15 14:34:00 +0900
categories: Group&nbsp;:&nbsp;Spring Spring&nbsp;Framework
---

### 설정 파일 - root-context.xml

- 모든 서블릿이 공유할 수 있는 공통 빈을 설정하는 파일
- 프로젝트의 어플리케이션 영역 설정
- 스프링 MVC 설정과 관련된 여러 처리를 담당
- View와 관련없는 빈을 설정 (예시 : 서비스, 레포지토리 등등)
- View와 밀접하지 않은 정보를 기술하는 xml 파일
- 외부 jar파일등으로 사용하는 클래스는 bean 태그를 이용해 작성

### 빈 설정 

- bean
    - 객체 정의 태그
    - 속성
        - id
            - 해당 객체의 고유 id
            - 예시 : dataSourceSpied
        - class
            해당 클래스명
            예시 : org.springframework.jdbc.datasource.DriverManagerDataSource
        - destroy-method
            - 주어진 세션을 자동으로 close하라는 의미
            - 예시 : close
- property
    - bean
        - 태그 안에 작성하는 해당 객체의 속성을 설정하는 태그
    - name
        - 해당 속성의 이름
        - 예시 : driverClassName
    - value
        - 해당 속성의 값
        - 예시 : org.mariadb.jdbc.Driver
    - ref
        - 해당 빈이 참고하는 다른 빈의 id
        - 예시 : dataSource & dataSourceSpied
- constructor-arg
    - bean 태그 안에 작성하는 의존하는 객체를 생성자를 통해 주입받는 태그
    - 속성
        - ref
            - 해당 빈이 참고하는 다른 빈의 id
            - 예시 : dataSourceSpied

>※ property 태그 안에서도 bean을 설정할 수 있다.

### 컴포넌트 스캔 설정

- root-context.xml의 beans 태그 안에 작성한다.
- context:component-scan
    - 명시한 패키지에 있는 클래스들을 빈으로 등록하기 위한 태그
    - 속성
        - base-package
            - 빈으로 등록하려고 하는 클래스가 포함된 패키지 경로
            - 예시 : com.my.mapper
- 기본 예시 코드
{% highlight xml %}
<context:component-scan base-package="com.my.mapper" />
{% endhighlight %}
- 필터링 기능이 적용된 예시 코드
{% highlight xml %}
<context:component-scan base-package="com.my">
    <context:exclude-filter type="annotation" expression="org.springframework.stereotype.Controller" />
</context:component-scan>
{% endhighlight %}

### 자주 쓰는 기능

- JDBC 연결 (mariaDB의 경우)
{% highlight xml %}
<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
    <property name="driverClassName" value="org.mariadb.jdbc.Driver" />
    <property name="url" value="jdbc:mariadb://url주소/데이터베이스명" />
    <property name="username" value="유저명" />
    <property name="password" value="비밀번호" />
</bean>
{% endhighlight %}

- myBatis 사용
{% highlight xml %}
<bean id="SqlSessionFectory" class="org.mybatis.spring.SqlSessionFactoryBean">
    <property name="dataSource" ref="dataSource" />
    <property name="configLocation" value="classpath:/mybatis-config.xml" />
    <property name="mapperLocations" value="classpath:/mappers/*Mapper.xml" />
</bean>
<bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate" destroy-method="clearCache">
    <constructor-arg name="sqlSessionFactory" ref="SqlSessionFectory" />
</bean>
<bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
    <property name="basePackage" value="com.my.mapper" />
</bean>
{% endhighlight %}

- SQL log 사용 (DBMS의 유저정보를 정의하는 dataSource가 이미 정의되어있는 경우)
    1. DBMS의 유저정보를 정의하는 id가 dataSource인 빈의 id를 dataSourceSpied로 변경한다.
    2. 아래의 코드를 작성한다.
    {% highlight xml %}
    <bean id="dataSource" class="net.sf.log4jdbc.Log4jdbcProxyDataSource"> 
        <constructor-arg ref="dataSourceSpied" /> 
        <property name="logFormatter"> 
            <bean class="net.sf.log4jdbc.tools.Log4JdbcCustomFormatter"> 
                <property name="loggingType" value="MULTI_LINE" /> 
                <property name="sqlPrefix" value="SQL : "/> 
            </bean> 
        <property> 
    </bean>
    {% endhighlight %}
