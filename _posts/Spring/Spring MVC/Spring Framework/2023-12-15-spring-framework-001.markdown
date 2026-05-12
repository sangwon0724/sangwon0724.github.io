---
layout: post
title:  "스프링 프레임워크에 대하여"
date:   2023-12-15 11:34:00 +0900
categories: Spring&nbsp;MVC
---

### 기본 소개

- 핵심 기술 : 스프링 DI 컨테이너, AOP, 이벤트, 기타
- 웹 기술 : 스프링 MVC, 스프링 WebFlux
- 데이터 접근 기술 : 트랜잭션, JDBC, ORM 지원, XML 지원
- 기술 통합 : 캐시, 이메일, 원격접근, 스케쥴링
- 테스트 : 스프링 기반 테스트 지원
- 언어 : 코틀린, 그루비

### 스프링의 핵심

- 스프링은 자바 언어 기반의 프레임워크
- 자바 언어의 가장 큰 특징 - 객체 지향 언어
- 스프링은 객체 지향 언어가 가진 강력한 특징을 살려내는 프레임워크
- 스프링은 좋은 객체 지향 애플리케이션을 개발할 수 있게 도와주는 프레임워크

### 스프링 프로젝트 폴더 구조

1. src/main/java
    - 자바 파일이 모여있는 곳
    - 스프링에서 이미 MVC 패턴의 서블릿 구조를 잡아주기 때문에  
    따로 서블릿을 만들 필요 없이 스프링 구조에 맞춰 클래스 파일들을 작성하면 된다.
2. src/main/resources
    - 자바 클래스에서 사용하는 리소스를 보관하는 폴더 (예시 : myBatis 관련 xml 파일)
3. src/test/java & src/test/resources
    - 테스트를 위한 자바 코드와 리소스를 보관하는 폴더
4. Maven Dependencies
    - maven에서 자동으로 관리해주는 라이브러리 폴더
    - pom.xml에 작성된 라이브러리들을 자동으로 다운받아서 관리한다.
5. src
    - Web에 관련된 자원이 담겨있는 루트 폴더
    - 하위 폴더에 웹과 관련된 모든 자원들이 분류되어 있다.
    - 하위 목록
        1. src/main/webapp/resources
            - 웹에 필요한 다양한 자원들을 보관하는 폴더
            - 사용자가 직접 접근할 수 있는 공간
            - js, css, img 파일 등이 보관된다.
            - 컨트롤러가 요청을 가로채지 않고 바로 접근할 수 있도록 따로 설정해서 사용하는 폴더
        2. src/main/webapp/WEB-INF
            - 웹에 필요한 코드 파일, 컴파일된 파일, 환경설정 파일이 보관되는 폴더
            - 보안이 중요한 파일들이기 때문에 외부 사용자가 직접 접근할 수 없는 폴더
            - 컨트롤러와 핸들러를 통해 내부적으로만 접근할 수 있는 폴더
            - 하위 목록
                1. src/main/webapp/WEB-INF/classes
                    - 컴파일 된 파일이 보관되는 폴더
                2. src/main/webapp/WEB-INF/spring
                    - 스프링 환경설정 파일이 보관되는 폴더 (root-context.xml, servelt-context.xml)
                3. src/main/webapp/WEB-INF/views
                    - jsp 및 html 파일이 보관되는 폴더
                    - 루트(/)의 기준점

### 스프링 설치하기

1. 이클립스 최상단의 Help 메뉴에서 Eclipse Marketplace 선택하기
2. STS (Spring Tool Suite)를 검색한 후에 해당 확장 모듈 설치하기

### 스프링 프로젝트 생성하기

1. 이클립스 최상단의 File 메뉴의 New 메뉴에서 Spring Legacy Project 선택하기
2. Spring MVC Project 선택한 후에 프로젝트명을 입력하고 Next 누르기
3. 해당 프로젝트의 최상단 패키지명 작성한 후 Finish 누르기
    > 예시
    >
    >서비스 예정 URL : metro.guide.com
    >패키지명 : com.guide.metro