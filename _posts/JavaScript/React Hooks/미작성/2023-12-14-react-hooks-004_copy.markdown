---
layout: post
title:  "useRef"
date:   2023-12-14 10:18:00 +0900
categories: React&nbsp;Hooks
published: false
---

### useRef

#### useRef란?

- useRef : 리액트의 컴포넌트가 특정 요소를 참조하게 하는 기능
- 리액트의 컴포넌트는 기본적으로 ref를 가지고 있다.
- 사용 방법
  1. useRef를 import한다.
  2. const refTest = useRef();를 선언한다. (refTest는 임의 변수명이다.)
  3. 사용할 컴포넌트에 ref 속성을 명시하고 값을 {refTest}로 작성한다.
  4. 만약 임의의 input 태그를 만들어서 refTest를 참조하게 했다면,  
  refTest.current를 통해서 해당 요소에 접근할 수 있다.
  - 예시) setTimeouy(() => refTest.current.focus(), 3000);

#### 사용 방법

{% highlight jsx %}

{% endhighlight %}

### userFullscreen (useRef 활용)

- userFullscreen : 어떤 Element든 풀스크린으로 만들거나 일반 화면으로 돌아가게 한다.
- 사용 방법
  1. import React, {useRef} from "react";를 진행한다.
  2. userFullscreen를 선언한다.
  {% highlight javascript %}
  const userFullscreen = callback => {
    const element = useRef();
    const runCb = isFull => {
        if(callback && typeof callback === "function"){
            callback(isFull);
        }
    };
  {% endhighlight %}
{:start="3"}
  3. App()에서 const {element, triggerFull, exitFull} = userFullscreen();를 작성한다.
  4. 크기를 키우고 싶은 곳의 ref 속성에 {element}를 작성한다.
  5. 크기를 변경하는 기능을 넣을 버튼의 onclick 속성으로 {triggerFull} 또는 {exitFull}를 작성한다.
  {% highlight javascript %}
    const triggerFull = () => {
        if(element.current){
            if(element.current.requestFullscreen)
            {
                element.current.requestFullscreen();
            }
            else if element.current.mozRequestFullscreen)
            {
                element.current.mozRequestFullscreen();
            }
            else if element.current.webkitRequestFullscreen)
            {
                element.current.webkitRequestFullscreen();
            }
            else if element.current.msRequestFullscreen)
            {
                element.current.msRequestFullscreen();
            }
            runCb(true);
        }
    };
    const exitFull = () => {
        document.exitFullscreen();
        if(document.exitFullscreen)
        {
            document.exitFullscreen();
        }
        else if (document.mozCancleFullscreen)
        {
            document.mozCancleFullscreen();
        }
        else if (document.webkitExitFullscreen)
        {
            document.webkitExitFullscreen();
        }
        else if (document.msExitFullscreen)
        {
            document.msExitFullscreen();
        }
        runCb(true);
    }
        if(callback && typeof callback === "function"){
            runCb(false);runCb(false);
        }
    };
    return {element, triggerFull, exitFull};
  };
  {% endhighlight %}