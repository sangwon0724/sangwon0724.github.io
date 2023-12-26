---
layout: post
title:  "설정 파일 - pom.xml"
date:   2023-12-15 13:42:00 +0900
categories: Spring&nbsp;Framework
---

### pom.xml의 역할

- POM : Project Object Model
- 프로젝트의 구조와 내용을 설명하는 파일
- 프로젝트 관리 및 빌드에 필요한 환경 설정, 의존성 관리 등의 정보들을 기술한다.
- 프로젝트의 세부 메타데이터 정보를 포함한다.
    - 예시 ) 버전 및 설정 관리, 빌드 환경, 라이브러리 저장소 및 의존성
- 프로젝트의 구조와 내용을 설명하는 파일

### 프로젝트 정보

- pom.xml의 project 태그 내부에 작성
- modelVersion
    - POM 모델의 버전 (예시 : 4.0.0)
- groupId
    - 프로젝트의 큰 틀
    -  표현 예시) 어떤 회사에서 프로젝트를 진행한다고 가정했을 때 그 회사 자체를 가리킨다.
    -  작성 예시) com.my (기본 패키지 경로 : com.my.app)
    -  작성 방법)
        1. 프로젝트가 운영되는 도메인 주소를 결정한다. (예시 : app.my.com)
        2. 해당 도메인 주소를 뒤집는다. (예시 : com.my.app)
- artifactId
    - 프로젝트의 각 기능들
    -  표현 예시) 어떤 회사에서 프로젝트를 진행한다고 가정했을 때 그 회사의 각 부서를 가리킨다.
    -  작성 예시) app (기본 패키지 경로 : com.my.app)
- name
    - 진행하는 프로젝트명
- packaging
    - jar, war, ear, pom등 패키지 유형을 나타낸다. (기본 값 : war)
- version
    - 진행하는 프로젝트의 버전 (기본 값 : 1.0.0-BUILD-SNAPSHOT)
- description
    - 프로젝트 설명 (필수 값 아님)
- url
    - 프로젝트를 찾을 수 있는 URL (필수 값 아님)
- parent
    - 해당 프로젝트가 상속받는 상위 pom.xml에 대한 정보 (필수 값 아님)
- properties
    -  pom.xml에서 중복해서 사용되는 상수 값들을 지정해놓는 부분
    -  예시) java-version에 1.8을 적용하고 다른 파트에서 ${java-version}을 작성하면 "1.8"이라는 값이 적용된다.
- dependencies
    - 의존성 라이브러리 정보를 적을 수 있다.
- build
    - 빌드와 관련된 정보를 설정할 수 있는 곳

>※ 최상위의 project 태그의 xmlns, xmlns:xsi, xsi:schemaLocation같은 속성들은  
모두 정해진 값이기 때문에 그냥 복사해다가 쓰면 된다.

### 의존성 정보

- pom.xml의 project 태그 → dependencies 태그 → dependency 태그 내부에 작성
- groupId
    - 해당 라이브러리의 그룹명 (예시 : org.springframework)
- artifactId
    - 해당 라이브러리의 기능명 (예시 : spring-context)
- version
    - 해당 라이브러리의 버전
- scope
    - 해당 라이브러리가 언제 필요한지, 언제 제외되는지를 나타내는 것  
    (사용 값 : compile, runtime, provided, test 등)
- exclusions
    - 해당 라이브러리와 관련된 실행에 대한 예외 처리 설정
    {% highlight xml %}
    <exclusions>
        <exclusion>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
        </exclusion>
    </exclusions>
{% endhighlight %}

### 빌드 정보

- pom.xml의 project 태그 → build 태그 → plugins 태그 → plugin 태그 내부에 작성
- groupId
    - 해당 플러그인의 그룹명
    - 예시 : org.apache.maven.plugins
- artifactId
    - 해당 플러그인의 기능명
    - 예시 : maven-compiler-plugin
- version
    - 해당 플러그인의 버전
- executions
    - 플러그인과 관련된 실행에 대한 설정
- configuration
    - 플러그인에서 필요한 설정 값 지정

>※ maven-compiler-plugin 플러그인을 찾아서 configuration 설정에서  
>source와 target의 값을 바꾸면 해당 프로젝트의 jdk 버전을 변경할 수 있다.

### pom.xml의 상속

- pom.xml의 project 태그 → parent 태그 내부에 작성
- groupId
    - 상속받는 pom.xml이 해당하는 프로젝트의 groupId
- artifactId
    - 상속받는 pom.xml이 해당하는 프로젝트의 artifactId
- version
    - 상속받는 pom.xml이 해당하는 프로젝트의 version

### 자주 쓰는 dependency

- mybatis 관련
{% highlight xml %}
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.2.2</version>
</dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>1.2.0</version>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>${org.springframework-version}</version>
</dependency>
{% endhighlight %}

- user DataSource 관련
{% highlight xml %}
<dependency>
    <groupId>commons-dbcp</groupId>
    <artifactId>commons-dbcp</artifactId>
    <version>1.4</version>
</dependency>
{% endhighlight %}
    
- mariaDB 관련
{% highlight xml %}
<dependency>
    <groupId>org.mariadb.jdbc</groupId>
    <artifactId>mariadb-java-client</artifactId>
    <version>2.6.0</version>
</dependency>
{% endhighlight %}
    
- ajax 관련
{% highlight xml %}
<dependency>
    <groupId>org.codehaus.jackson</groupId>
    <artifactId>jackson-mapper-asl</artifactId>
    <version>1.9.13</version>
</dependency>
{% endhighlight %}
    
- @ResponseBody 어노테이션 사용
{% highlight xml %}
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.10.1</version>
</dependency> 
{% endhighlight %}
    
- Sql Log 출력 기능 사용
{% highlight xml %}
<dependency>
    <groupId>org.lazyluke</groupId>
    <artifactId>log4jdbc-remix</artifactId>
    <version>0.2.7</version>
</dependency>
{% endhighlight %}
    
- 파일 처리 관련
{% highlight xml %}
<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>2.6</version>
</dependency>
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.3.1</version>
</dependency>
{% endhighlight %}

- json 변환 기능 사용
{% highlight xml %}
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.8.6</version>
</dependency>
{% endhighlight %}