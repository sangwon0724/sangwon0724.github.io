---
layout: post
title:  "설치 및 실행"
date:   2023-12-14 15:31:00 +0900
categories:  DevOn&nbsp;NCD
---

### DevOn NCD 설치

1. LG NCD 사이트로 이동 <a href="https://lgcns.com/Solution/DevOn-NCD" target="_blank">링크</a>
2. DevOn NCD (비즈니스 개발) 클릭
3. 필요 정보 입력 및 다운로드 클릭
4. 다운로드 받은 exe 파일을 실행해서 설치하기

### DevOn NCD 실행

1. startDevOnNCD.cmd 실행하기 (WAS :  Tomcat 8.5.49)
2. BizActor Management Studio 실행하기
3. 접속 정보 입력하기 (설치시 제공하는 기본 제공 메모장 참고)

### DevOn NCD의 DB 접속하기

1. HeidiSQL 실행하기
2. 접속 추가하기
3. 접속 정보 입력하기 (Server IP : 127.0.0.1 / Port	3306 / ID : root / Password : [공백])

- DevOn NCD 설치시 자동으로 Maria DB도 설치한다.
- 해당 Maria DB는 설치될때 자동으로 3306 포트에 설치되므로 MySQL같은 다른 프로그램이 사용중인지 확인한다.
- 만약 다른 프로그램이 3306 포트를 사용중이면 해당 프로그램의 이용 포트를 변경하고 서비스에서 종료한다.