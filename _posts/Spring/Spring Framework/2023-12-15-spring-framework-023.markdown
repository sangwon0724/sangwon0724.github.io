---
layout: post
title:  "어노테이션 목록"
date:   2023-12-15 14:55:00 +0900
categories: Group&nbsp;:&nbsp;Spring Spring&nbsp;Framework
---

### MVC - 컨트롤러
    
- @Contrller
    - 해당 클래스를 빈으로 등록
    - 해당 클래스를  컨트롤러로 사용할것임을 프레임워크에 알리는 어노테이션
- @RequestMapping, @GetMapping, @PostMapping
    - 요청 url을 연결하는 어노테이션
-  @RequestBody, @ResponseBody
    - 비동기 통신을 위해 움직이는 데이터인 http 요청에 대한 요청/응답 본문 어노테이션
-  @RequestParam(파라미터명)
    - url을 통해 해당 메소드를 요청할 때 전달해오는 값을 알기위한 어노테이션
-  @PathVariable
    - url에 명시된 동적 값을 알기위한 어노테이션
- @RestController
    - @Contrller + @ResponseBody
- @ModelAttribute
    - View에 데이터를 전달하기 위해 설정하는 어노테이션

### MVC - 서비스
    
- @Service
    - 빈 객체를 만들어 주는 어노테이션
    - 가시성을 위해 사용한다.
    - 비즈니스 로직에 대해서 처리하는 경우에 명시한다.
    
### 빈 관련 - 의존성 주입
    
- @Autowired
    - 해당하는 타입의 객체를 찾아서 자동으로 할당하는 어노테이션
    - 생성자, 메소드, 멤버변수 위에 모두 사용 가능
    - 탐색 순서 : 타입 -> 이름 -> @Qualifier -> 실패
- @Qualifier("qualifier 태그에 명시한 value")
    - @Autowired 어노테이션과 함께 사용하는 어노테이션
- @Inject
    - 해당하는 타입의 객체를 찾아서 자동으로 할당하는 어노테이션
    - 생성자, 메소드, 멤버변수 위에 모두 사용 가능
    - 탐색 순서 : 타입 -> @Named-> 이름 -> 실패
- @Named("id명")
    - @Inject 어노테이션과 함께 사용하는 어노테이션
- @Resource(name="등록된 빈의 id")
    - 주입하려고 하는 객체의 id가 일치하는 객체를 자동으로 주입한다.
    - 메소드, 멤버변수 위에 사용 가능
    - 사실상 @Autowired + @Qualifier
    - 탐색 순서 : 이름 -> 타입 -> @Qualifier -> 실패
    - @Resource나 @Resource(name="등록된 빈의 id")로 사용한다.
    - &lt;context:annotation-config/>를 xml 파일에 추가해야지 사용할수 있다.
    

### 빈 관련 - 컴포넌트 스캔
    
- @Component("빈 id")
    - 개발자가 직접 작성한 클래스를 bean 등록하고자 할 경우 사용하는 어노테이션
- @ComponentScan
    - 설정된 시작 지점부터 컴포넌트 클래스를 scanning하여 빈으로 등록해주는 역할을 하는 어노테이션
    - 스캔하는 컴포넌트 클래스
        - @Component
        - @Repository
        - @Service
        - @Controller
        - @Configuration
    - 속성
        - basePackages
           -  스캔을 시작할 패키지 경로를 명시
           - 예시 : com.my.app
        - basePackageClasses 속성
            - 스캔을 시작할 패키지 경로에 있는 클래스를 명시
            - 예시 : BlogController.class
    >basePackages 속성으로 명시하나 basePackageClasses 속성으로 명시하나  
    >같은 곳을 가리키게 한다면 결과는 같겠지만,  
    >basePackageClasses 속성으로 명시하는 것이 좀 더 안전하다.
- @Filter
    - @ComponentScan 어노테이션의 excludeFilters 속성에서 사용하는 어노테이션
    - 스캔을 제외할 조건을 명시한다.
    - 예시) excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = {Service.class})
- @Scope
    

### 빈 관련 - 외부 설정 파일
    
- @Configuration
    - 외부 라이브러리 또는 내장 클래스를 빈으로 등록하고자 할 경우 사용하는 어노테이션
    - 1개 이상의 @Bean을 제공하는 클래스의 경우 반드시 @Configuraton을 명시
- @PropertySource("classpath:설정파일경로")
    - 해당 설정 파일의 위치를 명시하는 어노테이션
- @Value("${빈id.속성명:디폴트값}")
    - 빈으로 등록된 클래스에서 값을 가져와서 주입하는 어노테이션
    

### 쿠키
    
- @CookieValue(value="가져올_쿠키명", required=true/false)
    

### 기타
    
- @Repository
    - 빈 객체를 만들어 주는 어노테이션
    - 가시성을 위해 사용한다.
    - 외부 I/O에 대해서 처리하는 경우에 명시한다.