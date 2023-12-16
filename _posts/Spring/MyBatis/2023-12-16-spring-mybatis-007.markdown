---
layout: post
title:  "MyBatis 캐시"
date:   2023-12-16 16:43:00 +0900
categories: Group&nbsp;:&nbsp;Spring MyBatis
---

### Local Session Cache (1nd Level)

- Session Level Cache 라고도 한다
- SqlSesison 객체마다 가지고 있는 캐시
- 개발자가 임의로 기능을 해제할 수 없다

### Second Level Cache (2nd Level)

- Mapper 의 namespace 마다 존재하는 캐시