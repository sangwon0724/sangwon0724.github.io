---
layout: post
title:  "설정 파일 - web.xml"
date:   2023-12-15 13:50:00 +0900
categories: Group&nbsp;:&nbsp;Spring Spring&nbsp;Framework
---

### web.xml의 역할

- Web Application의 환경파일

### web.xml의 특징

- 모든 Web application은 반드시 하나의 web.xml 파일을 가져야 함
- web.xml 파일의 설정들은 Web Application 시작시 메모리에 로딩된다.
- web.xml 파일을 수정 할 경우 web application을 재시작 해야 한다.

### web.xml의 작성 내용

- ServletContext의 초기 파라미터
- Session의 유효시간 설정
- Servlet/JSP에 대한 정의
- Servlet/JSP 매핑
- Mime Type 매핑
- Welcome File list
- Error Pages 처리
- 리스너/필터 설정
- 보안

### 설정 정보 (web.xml의 web-app 태그 내부에 작성)

- context-param
    - 모든 서블릿과 필터에서 사용되는 루트 스프링 컨테이너에 대한 설정
    - 속성
        - param-name
            - 설정파일에 대한 별명
            - 예시 : contextConfigLocation
        - param-value
            - 설정파일 경로 및 이름
            - 예시 : /WEB-INF/spring/root-context.xml
- listener
    - 웹서버가 동작 할때 특정 상황에 따라 각각의 기능을 작동시키는 리스너 클래스를 명시하는 태그
    - 속성
        - listener-class
            - 웹서버 동작 관련 인터페이스를 상속받은 클래스를 명시하는 태그
            - 예시
            {% highlight xml %}
            <listener>
                <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
            </listener>
            {% endhighlight %}
- servlet
    - 서블릿 객체 설정
    - 속성
        - servlet-name
            - 객체의 이름
            - 예시 : appServlet
        - servlet-class
            - 객체를 생성할 클래스
            - org.springframework.web.servlet.DispatcherServlet
        - init-param
            - 서블릿 초기화 매개변수 설정하기
            - 각각의 변수를 init-param 태그로 설정
            - 속성
                - param-name
                    - 서블릿 초기화 파라미터명
                    - 예시 : contextConfigLocation
                - param-value
                    - 서블릿 초기화 파라미터 값
                    - 예시 : /WEB-INF/spring/appServlet/servlet-context.xml
        - load-on-startup
            1. 서블릿은 브라우저에서 최초 요청되어 init() 메서드를 실행한 된 후에 메모리에 로드되어 기능을 수행한다.
            2. (1)의 이유로 서블릿에 대한 최초 요청에 대해서 실행 시간이 길어지는 단점을 보완하기 위해 생긴 기능이다.
            3. 톰캣 컨테이너가 실행되면서 미리 서블릿을 실행하는 역할을 한다. (예시 : 1)
            4. 지정한 숫자가 0보다 크면 톰캣 컨테이너가 실행되면서 서블릿이 초기화 된다.
            5. 지정한 숫자를 우선순위를 의미하며, 작은 숫자부터 먼저 초기화 된다.
- servlet-mapping
    - servlet 태그를 통해 등록한 서블릿을 연결시키는 방법
    - 속성
        - servlet-name
            - 연결될 서블릿의 이름
            - 예시 : appServlet
        - url-pattern
            - 클라이언트가 요청할 url 패턴
            - 예시 : /
- filter
    - HTTP 요청/응답을 변경할 수 있는 재사용 가능한 코드
    - 속성
        - filter-name
            - 생성할 필터의 별명
            - 예시 : MultipartFilter
        - filter-class
            - HTTP 요청/응답 변경 변경을 진행할 클래스
            - 예시 : org.springframework.web.multipart.support.MultipartFilter
- filter-mapping
    - 필터 적용방식 설정
    - 속성
        - filter-name
            - 적용할 필터의 별명
            - 예시 : MultipartFilter
        - url-pattern
            - 적용할 필터의 범위
            - 예시 : /*
- session-config
    - 세션 설정
    - 속성
        - session-timeout
            - 세션 시간 설정
            - 단위 : 분
            - 예시 : 30
- error-page
    - 에러 페이지 설정
    - 속성
        - error-code
            - 발생할 에러 코드 설정
            - 예시 : 404
        - location
            - 에러 발생시 보여질 에러 페이지 경로
            - 예시 : /WEB-INF/views/error/error.jsp
- welcome-file-list
    - 시작 페이지 목록 설정
    - 여러 파일이 지정된 경우 해당 경로에 맞는 파일들 중에서 가장 먼저 작성된 파일을 먼저 보여준다.
    - 속성
        - welcome-file
            - 시작 페이지 설정
            - 예시 : index.jsp
- multipart-config
    - 파일 처리 관련 설정
    - 속성
        - location
            - 업로드한 파일이 임시로 저장될 위치
            - 절대 경로만 가능
            - 기본 값 : java가 실행되는 temp 폴더
        - max-file-size
            - 업로드 가능한 파일의 최대 크기
            - 단위 : 바이트
            - 기본 값 :  -1 (제한 없음을 의미)
        - max-request-size
            - 전체 Multipart 요청 데이터의 최대 크기 지정
            -  단위 : 바이트
            - 기본 값 :  -1 (제한 없음을 의미)
        - file-size-threshold
            - 업로드한 파일의 크기가 해당 태그에서 설정한 값보다 크면  
            location 태그에서 지정한 디렉터리에 임시로 파일을 복사한다.
            - 단위 : 바이트
            - 기본 값 : 0

### 자주 쓰는 기능

- 한글 깨짐 방지

{% highlight xml %}
<filter>
    <filter-name>encodingFilter</filter-name>
    <filter-class>rg.springframework.web.filter.CharacterEncodingFilter</filter-class>
    <init-param>
        <param-name>encoding</param-name>
        <param-value>UTF-8</param-value>
    </init-param>
</filter>
<filter-mapping>
    <filter-name>encodingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
{% endhighlight %}

- 파일 전송

{% highlight xml %}
<filter>
    <filter-name>MultipartFilter</filter-name>
    <filter-class>org.springframework.web.multipart.support.MultipartFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>MultipartFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
{% endhighlight %}