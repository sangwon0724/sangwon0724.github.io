---
layout: post
title:  "세션"
date:   2023-12-15 13:13:00 +0900
categories: Group&nbsp;:&nbsp;Spring Spring&nbsp;Framework
---

### 세션 얻기

- 방법 1 : HttpServletRequest를 통한 세션 얻기
    - 컨트롤러 클래스의 메소드의 매개변수로 HttpServletRequest 객체 명시하기
    - 해당 객체의 명이 request라고 했을 때  
        예시) HttpSession session = request.getSession();

- 방법 2 : HttpSession을 통한 세션 얻기
    - 컨트롤러 클래스의 매개변수로 HttpSession 객체 명시하기

- 방법 1과 방법 2의 차이점
    - HttpServletRequest
        - 생성 시점 : 클라이언트가 최초로 접속할 때
        - 삭제 시점 : 클라이언트가 접속을 종료할 때
        - 유지 기간 : 클라이언트가 접속 중인 동안 존재
    - HttpSession
        - 생성 시점 : 클라이언트가 요청 시
        - 삭제 시점 : 서버가 응답 시
        - 유지 기간 : Request 중인 동안인만 존재

### 세션에 값 설정하기

1. 세션 객체를 얻는다. (변수명 : session)
2. session.setAttribute("속성명","값");

### 세션에서 값 가져오기

1. 세션 객체를 얻는다. (변수명 : session)
2. session.getAttribute("속성명","값");

### 세션 삭제하기

1. 세션 객체를 얻는다. (변수명 : session)
2. session.invalidate();