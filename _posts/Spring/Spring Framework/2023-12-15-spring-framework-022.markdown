---
layout: post
title:  "설정 파일 분리하기"
date:   2023-12-15 14:52:00 +0900
categories: Group&nbsp;:&nbsp;Spring Spring&nbsp;Framework
---

### 설정 값 분리의 필요성

- 환경에 따라 유연한 값 설정 가능
- 초기값을 설정 가능
- 불필요한 컴파일 축소 가능

### 전제 조건

- classpath의 기본 위치는 프로젝트/src/main/resources다.

### PropertyPlaceHolderConfigurer를 통한 수동 변환

- 설명
    - 빈 설정 메타정보가 모두 준비됐을 때 빈 메타정보 자체를 조작하기 위해 사용하는 방식
- 전체 조건
    - 해당 클래스에 @Configuration 어노테이션과 @PropertySource("classpath:설정파일경로") 어노테이션을 명시해준다.
- 사용 예시
    - xml
        - user.username=HongGilDong
        - user.birthday=970229
    - class
        {% highlight java %}
        @Value("${user.username}")
        private String userName;
        
        @Value("${user.birthday}")
        private String birthday;
        
        //defaultvalue 설정 가능
        @Value("${user.hoddy:게임}")
        private String hoddy;
        {% endhighlight %}

### SpEL을 통한 능동 변환

- 설명
    - 다른 빈 오브젝트에 직접 접근할 수 있는 표현식을 이용해 원하는 프로퍼티 값을 능동적으로 가져온다.
- 전체 조건
    - 해당 클래스에 @Component 어노테이션을 명시해준다.
- 사용 예시
    - 빈으로 등록할 클래스
        {% highlight java %}
        @Component("userInfo")
        public class config{
            public static String username="HongGilDong";
            public String getBirthday(){
                return "970229";
            }
        }
        {% endhighlight %}
    - 빈을 사용할 클래스 >>>
        {% highlight java %}
        @Value("#{userInfo.username}")
        private String userName;
        
        @Value("#{userInfo.getBirthday()}")
        private String birthday;
        {% endhighlight %}

>※ 주의점
>메소드 및 생성자 인자에 @Value를 사용할 때는  
>@Autowired나 @Resource같은 어노테이션이 반드시 존재해야 한다.

### Environment을 통한 능동 변환

- 설명
    - 다른 빈 오브젝트에 직접 접근할 수 있는 표현식을 이용해 원하는 프로퍼티 값을 능동적으로 가져온다.
- 전체 조건
    - 해당 클래스에 @Configuration 어노테이션과 @PropertySource("classpath:설정파일경로") 어노테이션을 명시해준다.
- 사용 예시
    - xml
        - user.username=HongGilDong
        - user.birthday=970229
    - class
        {% highlight java %}
        @Autowired 
        Environment env;

        private String userName=env.getProperty("user.username");
        private String birthday=env.getProperty("user.birthday");
        {% endhighlight %}

