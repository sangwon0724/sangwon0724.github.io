---
layout: post
title:  "maven (메이븐)"
date:   2023-12-15 11:40:00 +0900
categories: Spring&nbsp;MVC
---

### maven의 정의

- 프로젝트를 빌드하고 라이브러리를 관리해주는 도구
- 자바 프로젝트의 빌드를 자동화 해주는 빌드 툴
- 자바 소스를 compile하고 package해서 deploy하는 일을 자동화 해주는 도구

### maven의 사용 이유

- 개발자들이 편하게 서로 같이 협력하면서 일을 할 수 있도록 하기 위해서
- 필요한 라이브러리의 하위 라이브러리까지 버전에 맞게 알아서 받아주기 때문에

### maven의 라이프사이클

- maven 라이프사이클 : maven이 프로젝트를 빌드함에 있어서 동작하는 작업들에 대한 구조
- phase : maven 라이프사이클 안에서 동작하는 각각의 작업
- goal : 각각의 phase 안에 존재하는 플러그인에서 수행가능한 명령

>※ maven의 라이프사이클은 내부의 phase가 차례대로 진행되기 때문에  
>나중 단계의 명령을 호출하면 이전 단계의 작업들은 먼저 진행되고 해당 명령을 진행한다.  
>
>예시 ) maven install을 실행한다고 가정했을 때,  
>compile → test → package 순으로 작업이 진행된 다음에 install이 진행된다.

### maven의 라이프사이클 종류

- Default (기본) 라이프사이클
    1. compile
        - 소스코드를 컴파일해주는 단계
        - 작업이 성공적으로 진행되면 target/classes 폴더가 만들어지고 컴파일된 class파일이 생성된다.
    2. test
        - 테스트 코드를 실행해주는 단계
        - 실패하면 빌드가 멈춘다.
        - 작업이 성공적으로 진행되면 target/test-classes 폴더와 안에 컴파일된 class파일이 생성되고  
        target/surefire-reports 폴더에 테스트 결과가 기록된다.
    3. package
        - 해당 프로젝트를 지정한 확장자로 묶어주는 단계
        - pom.xml에 packaging 태그에 명시되있는 확장자로 파일이 만들어진다.
        - "artifactId-version.packaging"형태의 파일을 target 폴더안에 생성한다.
    4. install
        - Maven이 설치되어 있는 PC인 로컬 리포지토리에 배포한다.
    5. deploy
        - 원격 리포지토리가 등록되어 있다면 해당 원격 리포지토리에 배포한다.
- Clean 라이프사이클
    1. clean
        - 생성된 target 폴더를 삭제한다.
- Site 라이프사이클 : 문서 사이트를 생성할 수 있도록 지원한다.
    1. site
    2. site-deploy