---
layout: post
title:  "State Hooks"
date:   2023-12-14 09:57:00 +0900
categories: React&nbsp;Hooks
published: false
---


### useInput

- useInput : 값 변경 + 유효성 검사
- 사용 방법
  1. import React, {useState} from "react";를 진행한다.
  2. useInput을 선언한다.
{% highlight javascript %}
const useInput = (initialValue, validator) => {
        const [value , setValue] = useState(initialValue);
        const onChange = event => {
            const { 
                target : {value}
            } = event;
        };
        let willUpdate = true;
        if(typeof validator === "function"){
            willUpdate = validator(value);
        }
        if(willUpdate){
            setValue(value);
        }
        return {value, onChange};
    };
{% endhighlight %}  
{:start="3"}
  3. const name = useInput("원하는 값");을 선언한다.
  4. input에서 값을 사용할 때 {name.value}로 사용하면 된다.  
  {name.value}가 사용가능한 이유는 useInput이 value라는 이름의 값을 return하기 때문이다.  
  아니면 name안의 내용물을 모두 풀어주는 {...name}을 사용하면 된다.

### useTabs

- useTabs : 값의 전환을 쉽게 사용하기 위한 기능
- 사용 방법
  1. import React, {useState} from "react";를 진행한다.
  2. useTabs를 선언한다.
  {% highlight javascript %}
  const useTabs = (initialTab, allTabs) -> {
          if(!allTabs || Array.isArray(allTabs)){
              return; 
          }
          const [currentIndex, setCurrentIndex] = useState(initialTab);
          return {
              currentItem : allTabs[currentIndex],
              changeItem : setCurrentIndex
          };
      };
  {% endhighlight %}