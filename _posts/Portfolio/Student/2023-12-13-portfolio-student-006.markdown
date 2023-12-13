---
layout: post
title:  "Natural Blog (보다 완성도 있고 자연스러운 블로그)"
date:   2023-12-13 11:03:00 +0900
categories: Group&nbsp;:&nbsp;Portfolio Student
---

### 개발환경, 개발인원, 개발 기간, 담당 역할

- 개발 환경
    - OS : Window
    - Language : JAVA, JSTL, Java Script
    - Tools : Eclipse, Spring, HeidiSQL (MariaDB), Tomcat 8.5, MyBatis
- 개발 인원 : 1명
- 담당 역할 : 프로젝트의 전반적인 계획, 디자인, 구현 등을 모두 담당
- 개발 목적 : 화면의 전환 및 데이터의 흐름을 최대한 자연스럽게 구현

### 개발개요

1. 다양한 블로그의 각각의 장점을 합쳐서 사용자들이 보다 이용하기 좋은 블로그를 만드는 것
2. 간단한 블로그를 만드는 것에서 그치는 것이 아닌 최대한 자세한 디테일까지 만들어서 블로그라는 하나의 주제를 완성시키는 것

### 구현기능

- 블로그 : 게시글 CRUD / 페이징 / 댓글 / 좋아요
- 마이페이지 : 프로필 변경 / 블로그 꾸미기 / 이웃관리 / 카테고리 관리

### 후기

우선 데이터를 처리하는 과정에 대해서 기존에 사용하고 있었던 Controller/Service/DAO/VO 방식에서  
VO 대신에 Map을 사용하여 불필요한 코드의 추가 작성을 줄이고자 하였습니다.  
왜냐하면 VO를 사용하게 되면 각각의 상황에 맞는 각각의 구조를 설계하는 시간이 생기기 때문에  
프로젝트의 크기도 커지고 추후의 유지보수에 불편함이 생길수도 있기 때문입니다.  
그래서 @ResponseBody 어노테이션과 @RequestBody 어노테이션을 사용하여 데이터를 Map 형식으로 받는 방법을 공부하였습니다.  
또한 화면 이동 방식에 대하여 기존에는 각각의 상황에 따라 모든 URL을 설정하였지만  
이번 프로젝트에서는 하나의 메소드에서 전달된 값을 통하여 다양한 작업이 진행되도록 하였습니다.  
추가적으로 URL을 설정하는 방식을 기존의 parameter 방식에서 Rest API 방식으로 이용하여 최대한 깔끔한 URL을 보여줄수 있도록 설계하였습니다.

### 링크
[깃허브](https://github.com/sangwon0724/https://github.com/sangwon0724/Natural_Blog)

### 스크린샷

<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/01.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/02.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/03.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/04.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/05.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/06.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/07.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/08.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/09.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/10.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/11.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/12.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/13.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/14.png"/>
<img src="{{site.url}}{{site.baseurl}}{{site.portfolio_img_root}}/Student/Natural_blog/15.png"/>