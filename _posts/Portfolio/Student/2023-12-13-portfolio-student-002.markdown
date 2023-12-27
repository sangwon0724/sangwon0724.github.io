---
layout: post
title:  "Healthtory (헬스 관련 사이트)"
date:   2023-12-13 10:55:00 +0900
categories:  Student
---

### 개발환경, 개발인원, 개발 기간, 담당 역할

- 개발 환경
    - OS : Window
    - Language : JAVA, JSTL, Java Script
    - Tools : Eclipse, Spring, MySQL Workbench 8.0, Tomcat 8.5
- 개발 인원 : 2명
- 개발 기간 : 2020-11-20 ~ 2020-12-15
- 담당 역할
    - 웹페이지 디자인의 약 95% 담당
    - Java Script 코드 작성의 약 90% 담당
    - 메인 페이지 & 운동 게시판에 대한 DAO, VO 작성

### 개발개요

다양한 운동들에 대한 정보를 각 운동 부위마다 분류하여 정리해줌으로써  
운동에 대한 정보를 쉽게 얻을 수 있게 해주는 정보 제공 사이트

### 구현기능

- 메인 페이지 : 축제 검색 기능, 축제 랭킹 TOP 10, 분기별 축제 목록, 월별 축제 목록
- 자유 게시판 : 게시글 작성/보기/삭제 (글만 입력 가능)
- 몸짱/홍보 게시판 : 게시글 작성/보기/삭제 (이미지를 추가하는 등의 특수 기능 포함)
- 유저 : 로그인, 회원가입, 작성 글 목록, 작성 댓글 목록, 쪽지
- 관리자 페이지 : 운동 게시판에 게시글 추가

### 후기

첫 스프링 프로젝트인 STEP 종료 이후 시작한 두 번째 프로젝트입니다.  
어느새 전혀 이해할 수 없었던 MVC 구조를 이해할 수 있게 되었으며  
본격적으로 웹 페이지 제작에 재미를 느끼게 해준 뜻깊은 프로젝트였습니다.  
아쉬웠던 점으로는 이번에도 프로젝트 설게과정에서의 미흡함으로 인해서  
이전의 STEP 프로젝트와 똑같이 게시글을 수정하는 기능을 추가하지 못한 것과  
추가할까 말까 고민하다가 결국 못 넣었던 채팅 기능을 추가 하지 못한 것이 있습니다.  

### 링크
[깃허브](https://github.com/sangwon0724/Healthtory)

### 스크린샷

{% capture path %}
{{site.url}}{{site.portfolio_img_root}}/Student/Healthtory/
{% endcapture %}
{% include slider.html path=path extension="JPG" start="1" end="18" %}