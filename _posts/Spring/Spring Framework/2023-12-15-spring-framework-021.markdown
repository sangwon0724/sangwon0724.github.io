---
layout: post
title:  "설정 파일 - servelt-context.xml"
date:   2023-12-15 14:43:00 +0900
categories: Spring&nbsp;Framework
---

### servelt-context.xml의 역할

- 요청과 관련된 객체를 정의하는 설정 파일

### 어노테이션 설정

- &lt;annotation-driven />
    - 어노테이션을 사용하기 위해서 필수적으로 작성해야 하는 내용
    - servelt-context.xml의 beans 태그 안에 작성
    - 단일 태그로 사용

### 자원 관리 설정

- &lt;resources mapping="/resources/**" location="/resources/" />
    - servelt-context.xml의 beans 태그 안에 작성
    - 단일 태그로 사용
    - 속성
        - mapping
            - resource와 관련되어 매핑되는 url 형태를 작성한다.
        - location
            - resource 관련 호출시 탐색하는 실제 경로를 작성한다.

### 빈 설정

- 기본 구조
    - 최상위 beans => 추가할 기능 beans => beans:property
- servelt-context.xml의 beans 태그 안에 작성
- 단일 태그로 사용 가능
    - 속성
        - beans:bean
            - 속성
                - id
                    - 빈의 고유명
                - class
                    - 해당 빈이 참조하는 클래스
        - beans:property
            - 속성
                - name
                    - 해당 빈의 가진 속성의 이름
                - value
                    - 해당 빈의 가진 속성의 실제 값

### 컴포넌트 스캔 설정

- context:component-scan
    - 명시한 패키지에 있는 클래스들을 빈으로 등록하기 위한 태그
    - servelt-context.xml의 beans 태그 안에 작성
    - 단일 태그로 사용
    - 속성
        - base-package
            - 빈으로 등록하려고 하는 클래스가 포함된 패키지 경로
            - 예시 : com.my.app
- 기본 예시 코드 )
    &lt;context:component-scan base-package="com.my.app" />

    >※ servelt-context.xml는 요청과 관련된 객체를 정의하는 설정 파일이기 때문에  
    >컴포넌트 스캔도 @Contrller가 포함된 패키지만 작성한다.

### interceptors 설정

- 기본 구조
    - 최상위 beans => interceptors => interceptor 태그 안에 작성
- 속성
    - mapping : 인터셉터를 실행시킬 url들을 매핑시키기 위한 태그
        - path : 인터셉터를 실행시킬 url을 작성한다.
            - 예시 1 ) &lt;mapping path="/blog/setting/profile"/>
            - 예시 2 ) &lt;mapping path="/blog/{userID}/write"/>
    - beans:ref : 실행될 인터셉터에 대해서 작성한 클래스를 참조한 빈에 대해서 작성하는 태그
            - 예시 - 준비 )  
            interceptors 태그 밖에  
            &lt;beans:bean id="authenticationInterceptor" class="com.my.util.UrlInterceptor"/> 작성  
            (authenticationInterceptor와 com.my.util.UrlInterceptor는 임의값)
            - 예시 - 설정 )
            interceptors 태그 내부의 interceptor 태그 내부에  
            &lt;beans:ref bean="authenticationInterceptor"/> 작성  
            (authenticationInterceptor는 임의값)

### 자주 쓰는 기능

- 어노테이션 사용
{% highlight xml %}
<annotation-driven />
{% endhighlight %}

- 리소스 설정 (기본 설정)
{% highlight xml %}
<resources mapping="/resources/**" location="/resources/" />
{% endhighlight %}

- view 페이지 설정 (기본 설정)
{% highlight xml %}
<beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    <beans:property name="prefix" value="/WEB-INF/views/" />
    <beans:property name="suffix" value=".jsp" />
</beans:bean>
{% endhighlight %}

- 컨트롤러 관련 컴포넌트 스캔 (com.my.app은 임의값)
{% highlight xml %}
<context:component-scan base-package="com.my.app" />
{% endhighlight %}

- 파일 업로드 관련
{% highlight xml %}
<beans:bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
    <beans:property name="maxUploadSize" value="100000000"></beans:property>
</beans:bean>
{% endhighlight %}

- 인터셉터 관련 (authenticationInterceptor와 com.my.util.UrlInterceptor는 임의값)
{% highlight xml %}
<beans:bean id="authenticationInterceptor" class="com.my.util.UrlInterceptor"/>
<interceptors>
    <interceptor>
        <mapping path="/blog/{userID}/write"/>
        <mapping path="/blog/setting/profile"/>
        <beans:ref bean="authenticationInterceptor"/>
    </interceptor>
</interceptors>
{% endhighlight %}