---
layout: post
title:  "Step (여행 소개 사이트)"
date:   2023-12-13 10:44:00 +0900
categories:  Student
---

### 개발환경, 개발인원, 개발 기간, 담당 역할

- 개발 환경
    - OS : Window
    - Language : JAVA, JSTL, Java Script
    - Tools : Eclipse, Spring, Oracle SQL Developer, Tomcat 8.5
- 개발 인원 : 4명
- 개발 기간 : 2020-04-19 ~ 2020-11-17
- 담당 역할
    - 웹페이지 디자인의 약 70% 담당
    - Java Script 코드 작성의 약 90% 담당
    - 축제 관리 & 커뮤니티 게시판 & 리뷰 게시판에 대한 DAO, VO 작성

### 개발개요

전국의 축제들에 대한 데이터를 수집해서 축제에 대해 정보를 얻고 싶어하는 사람들에게  
알아보기도 쉽고, 실제 내용도 실용적인 정보로 가공하여 제공하는 사이트

### 구현기능

- 메인 페이지 : 축제 검색 기능, 축제 랭킹 TOP 10, 분기별 축제 목록, 월별 축제 목록
- 축제 목록 : 정렬 기능, 태그별 (축제 종류) 보기 기능, 지역별 보기 기능, 한줄평 (평점용), 관련 축제 추천
- 커뮤니티 게시판 : 게시글 작성/보기/삭제 (글만 입력 가능)
- 리뷰 게시판 : 게시글 작성/보기/삭제 (이미지를 추가하는 등의 특수 기능 포함)
- 유저 : 로그인, 회원가입, 작성 글 목록, 작성 댓글 목록
- 특수 페이지 : 홍보 문의 (= 축제 추가)
- 관리자 페이지 : 홍보 문의로 등록한 축제에 대한 수락 및 거절

### 후기

본격적으로 협업을 하는 경험이 된 프로젝트였습니다.  
아직도 잘 만들어져있는 상태는 아니지만 프로젝트를 시작하면서  
내가 웹 개발에 재미를 느끼고 있다는 것을 알게 되었습니다.  
또한 1학기때 4월에서 8월까지 프로젝트에 도움이 될만한 추가적인 공부를 하면서  
1학년도 이렇게는 안 만들겠다라는 느낌을 주었던 매우 조잡했던 프로젝트를  
2학기때 9월에서 11월까지 단 3개월만에 이 정도면 3학년이 만들었다고 말할수 있는 정도까지  
자신을 발전시킬수 있었습니다.  
하지만 프로젝트 설계 과정에서 미흡했던 점으로 인해서  
커뮤니티 게시판이나 리뷰 게시판에 게시글 수정 기능이 없거나,  
홍보 문의를 하기 위해 필요한 기업용/단체용 아이디같은 특수 아이디 기능이 없거나,  
관리자가 사용할 수 있는 기능이 적은 것이 아쉬웠습니다.  
이후에는 AJAX같은 기술을 배워서 좀 더 동적인 페이지를 만드는 것이 목표입니다.

### 링크
[깃허브](https://github.com/sangwon0724/Step)

### 스크린샷

{% capture path %}{{site.url}}{{site.portfolio_img_root}}/Student/Step/{% endcapture %}
{% include slider.html path=path extension="JPG" start="1" end="17" %}