---
layout: post
title:  "MyBatis에 대하여"
date:   2023-12-16 16:11:00 +0900
categories: MyBatis
---

### MyBatis란?

- 추후 작성

### 설치

1. pom.xml에 의존성 추가
  {% highlight xml %}
  <dependency>
      <groupId>org.mybatis</groupId>
      <artifactId>mybatis</artifactId>
      <version>3.5.15</version>
  </dependency>
  <dependency>
      <groupId>org.mybatis</groupId>
      <artifactId>mybatis-spring</artifactId>
      <version>3.0.3</version>
  </dependency>
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-jdbc</artifactId>
      <version>6.1.0</version>
  </dependency>
  {% endhighlight %}

{:start="2"}
2. root-context.xml에 DBMS 유저 정보 등록
  {% highlight xml %}
  <bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
      <property name="driverClassName" value="org.mariadb.jdbc.Driver" />
      <property name="url" value="jdbc:mariadb://url주소/데이터베이스명" />
      <property name="username" value="유저명" />
      <property name="password" value="비밀번호" />
  </bean>
  {% endhighlight %}

{:start="3"}
3. root-context.xml에 sqlSession 등록
  {% highlight xml %}
  <bean id="SqlSessionFectory" class="org.mybatis.spring.SqlSessionFactoryBean">
      <property name="dataSource" ref="dataSource" />
      <property name="configLocation" value="classpath:/mybatis-config.xml" />
      <property name="mapperLocations" value="classpath:/mappers/*Mapper.xml" />
  </bean>
  <bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate" destroy-method="clearCache">
      <constructor-arg name="sqlSessionFactory" ref="SqlSessionFectory" />
  </bean>
  {% endhighlight %}

{:start="4"}
4. root-context.xml에 DAO를 작성할 패키지를 등록 (임의값 : com.my.mapper)
  {% highlight xml %}
  <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
      <property name="basePackage" value="com.my.mapper" />
  </bean>
{% endhighlight %}

{:start="5"}
5. DAO를 작성할 패키지를 빈으로 등록할 수 있게 컴포넌트 스캔 추가 (임의값 : com.my.mapper)
{% highlight xml %}
<context:component-scan base-package="com.my.mapper" />
{% endhighlight %}

{:start="6"}
6. 3에서 작성한 SqlSessionFectory의 property의 value의 classpath가 의미하는 지점인  
프로젝트명/src/main/resources에 가서 mybatis-config.xml을 작성한다.
  {% highlight xml %}
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">
  <configuration>
    <!-- ... -->
  </configuration>
  {% endhighlight %}
  
{:start="7"}
7. 3에서 작성한 SqlSessionFectory의 property의 mapperLocations 파라미터에 명시한 대로 폴더를 만든 후  
그 위치에 지정한 형식의 이름을 가진 xml 파일을 만든다.  
해당 파일은 SQL을 작성할 문서가 된다. (*Mapper.xml => blogMapper.xml, userMapper.xml 등등)

8. SQL을 작성할 xml 파일에 가서 기본 코드를 작성해준다.
{% highlight xml %}
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="">
    <!-- ... -->
</mapper>
{% endhighlight %}