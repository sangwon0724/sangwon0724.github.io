---
layout: post
title:  "Effect Hooks"
date:   2023-12-14 10:13:00 +0900
categories: React&nbsp;Hooks
published: false
---

### useEffect

#### useEffect란?

- useEffect : Element에 효과 부여하기
- 사용 방법
    1. 기존의 import React from "react";에서 import React, {useEffect} from "react";로 변경한다.
    2. useEffect(func, [deps]);로 사용하면 된다.
- 특징
    - useEffect는 componentDidmount의 역할을 한다.
    - useEffect는 두 개의 인자가 사용된다.
        1. useEffect가 실행될 때 실행되는 함수
        2. 해당하는 값일 있을 때만 값이 변하도록 활성화하는 배열
    - useEffect 내에서 사용되는 return은 해당 effect가 더 이상 실행할 필요가 없을 때 청소하는 용도를 한다.
    - useEffect가 더 이상 실행할 필요가 없는 경우
        -  dependancy가 바뀌어서 effect가 달라져야할 때 (이전 effect 제거)
        - 해당 component가 unmount 될 때
            - 해당하는 unmount 될 때만 사용하려면 dependancy가 항상 같도록 useEffect의 두번째 인자에 []를 넘기면 된다.

#### 사용 방법

{% highlight react %}

{% endhighlight %}

### useBeforeLeave (useEffect 활용)

- useBeforeLeave : 마우스가 문서를 떠나려고 하는 시점에 실행되는 기능
- 사용 방법
    1. import React, {useEffect} from "react";를 진행한다.
    2. useBeforeLeave를 선언한다.
    {% highlight javascript %}
    const useBeforeLeave = (onBefore) => {
            if(typeof onBefore !== "function"){
                return;
            }
            const handle = event => {
                const {clientY} = event;
                if(clientY &lt;= 0)
                {
                    onBefore();
                }
            };
            useEffect(
                () => {
                    document.addEventListener("mouseleave", handle);
                    return () => document.removeEventListener("mouseleave", handle);
                }
            ,[]);
        };
    {% endhighlight %}