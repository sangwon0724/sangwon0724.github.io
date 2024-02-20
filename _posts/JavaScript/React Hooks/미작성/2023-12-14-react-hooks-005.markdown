---
layout: post
title:  "Compositive Hooks"
date:   2023-12-14 10:31:00 +0900
categories: React&nbsp;Hooks
published: false
---

### useTitle

- useTitle : Document의 title을 변경하는 기능
- 사용 방법
  1. import React, {useState, useEffect} from "react";를 진행한다.
  2. useTitles를 선언한다.
  {% highlight javascript %}
  const useTitles = initailTitle => {
      const [title, setTitle] = useState(initailTitle);
      const updateTitle = () => {
          const htmlTitle = docuement.querySelecor("title");
          htmlTitle.innerText = title;
      };
      useEffect(updateTitle, [title]);
      return setTitle;
  };
  {% endhighlight %}

### useClick

- useClick : 클릭한 시점에 일어나는 이벤트
- 사용 방법
  1. import React, {useEffect, useRef} from "react";를 진행한다.
  2. useClick를 선언한다.
  {% highlight javascript %}
  const useClick = onClick => {
      if(typeof onClick !== "function"){return;}
      const element = useRef();
      useEffect(
          () => {
              if(element.current){
                  element.current.addEventListener("click",onClick);
              }
              return () => {
                  if(element.current){
                      element.current.removeEventListener("click",onClick);
                  }
          }
      ,[]);
      return element;
  };
  {% endhighlight %}
{:start="3"}
  3. App()에서 const title = useClick(사용할 함수명);을 선언한다.
  4. App()의 return에서 적용할 컴포넌트의 ref 속성에 {title}이라고 작성한다.
- useEffect에서 빈 배열을 넣는 이유는 그렇게 해야지 componentDidmount때 단 한 번만 실행되라는 의미가 되기 때문이다.
- useEffect에서 빈 배열을 넣지 않으면 매번 업데이트 될 때마다 eventListener가 추가된다.
- useEffect 안에서 return을 시켜서 removeEventListener를 시키는 이유는 componentWillUnMoount때 호출되게 하기 위해서다.

### useFadeIn

- useFadeIn : 어떤 Element든 상관없이 애니메이션을 Element 안으로 서서히 사라지게 하는 이벤트
- 사용 방법
  1. import React, {useEffect, useRef} from "react";를 진행한다.
  2. useFadeIn를 선언한다.
  {% highlight javascript %}
  const useFadeIn = (duration = 1, delay = 0) => {
      if(typeof duration !== "number" || typeof delay !== "number"){
          return;
      }
      const element = useRef();
      useEffect(
          () => {
              if(element.current){
                  const {current} = element;
                  current.style.transition = `opacity ${duration}s ease-in-out ${delay}s`;
                  current.style.opacity = 1;
              }
          }
      ,[]);
      return {ref : element, style : {opacity : 0}};
  };
  {% endhighlight %}
{:start="3"}
  3. App()에서 const fadeIn = useFadeIn(동작시간, 딜레이시간);를 작성한다.
  4. 사용할 컴포넌트에서 {...fadeIn}을 작성한다.

### useNetwork

- useNetwork : 온라인/오프라인 여부 확인
- 사용 방법
  1. import React, {useState , useEffect} from "react";를 진행한다.
  2. useNetwork를 선언한다.
  {% highlight javascript %}
  const useNetwork = onChange => {
      const [status, setStatus] = useState(navigator.onLine);
      const handleChange = () => {
          if(typeof onChange === "function"){
              onChange(navigator.onLine);
          }
          setStatus(navigator.onLine);
      };
      useEffect(
          () => {
              window.addEventListener("online",handleChange);
              window.addEventListener("offline",handleChange);
              return () => {
                  window.removeEventListener("online",handleChange);
                  window.removeEventListener("offline",handleChange); 
              };
          }
      ,[]);
      return status;
  };
  {% endhighlight %}
{:start="3"}
  3. App()에서 const fadeIn
  3. App()에서 const online = useNetwork();를 작성한다.
  4. {onLine ? "온라인" : "오프라인"}처럼 사용하여 네트워크의 상태를 확인한다.

### useScroll

- useScroll : 스크롤 사용시 발생하는 이벤트
- 사용 방법
  1. import React, {useState , useEffect} from "react";를 진행한다.
  2. useScroll를 선언한다.
  {% highlight javascript %}
  const useScroll = () => {
      const [state, setState] = useState({x : 0, y : 0});
      const onScroll = () => {
          setState({x : window.scrollX, y : window.scrollY});
      };
      useEffect(
          () => {
              window.addEventListener("scroll", onScroll);
              return () => window.removeEventListener("scroll", onScroll);
          }
      );
      return state;
  };
  {% endhighlight %}