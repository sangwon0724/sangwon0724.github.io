---
layout: post
title:  "Publishing to NPM"
date:   2023-12-14 10:39:00 +0900
categories: React&nbsp;Hooks
published: false
---

### NPM에 제작한 리액트 훅 등록하기

1. 등록할 JS 파일에 가서 터미널 패널을 연 다음에 npm init을 입력한다.
2. 필요한 정보를 다 입력한다.
3. react가 필요한 훅이기 때문에 터미널에서 npm i react react-dom을 입력한다.
4. package.json의 dependencies 속성의 이름을 peerDependencies로 변경한다.  
→ 이미 설치되어 있다면 설치하지 않고, 설치되어 있지 않다면 설치한다.
5. 터미널에서 npm login을 입력한다.
6. 터미널에서 npm publish -access public을 입력한다.  

-  npm 계정이 없는 경우 npm 계정을 만든다.