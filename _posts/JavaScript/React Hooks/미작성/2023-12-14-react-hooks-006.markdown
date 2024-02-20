---
layout: post
title:  "None Import Hooks"
date:   2023-12-14 10:36:00 +0900
categories: React&nbsp;Hooks
published: false
---

### useConfirm

- useConfirm : 사용자가 행동을 하기전에 미리 확인하는 기능
- 사용 방법
{% highlight javascript %}
const useConfirm = (message, onConfirm, onCancle) => {
    //반드시 필요한 함수
    if(!onConfirm || typeof onConfirm !== "function"){
        return;
    }
    //반드시 필요한 건 아닌 함수
    if(onCancle && typeof onCancle !== "function"){
        return;
    }
    const confirmAction = () => {
        //confirm : 예 or 아니오를 묻는 JS의 기본 기능
        if(confirm(message)){
            onConfirm();
        }
        else{
            onCancle(); //confirm 실행시 아니오를 눌렀을 때 진행될 함수
        }
    }
    return confirmAction;
};
{% endhighlight %}

### usePreventLeave

- usePreventLeave : 유저가 페이지를 벗어나려는 시점에 실행되는 함수
  1. usePreventLeave를 선언한다.
  {% highlight javascript %}
  const usePreventLeave = () => {
      const listener = (event) => {
          event.preventDefault();
          event.reurnValue = "";
      };
      const enablePrevent = () => window.addEventListener("beforeunload", listener);
      const disablePrevent = () => window.removeEventListener("beforeunload", listener);
      return {enablePrevent, disablePrevent};
  };
  {% endhighlight %}
{:start="2"}
  2. App()에서 const {enablePrevent, disablePrevent} = usePageLeave();를 작성한다.
  3. 사용할 컴포넌트에서 enablePrevent 또는 disablePrevent를 사용한다.

### useNotification

- useNotification : Notification API를 사용할 때 유저에게 알림을 보낸다.
- 사용 방법
{% highlight javascript %}
const useNotification = (title, options) => {
    if (!("Notification" in window)) {
      return;
    }
    const fireNotif = () => {
      if (Notification.permission !== "granted") {
        Notification.requestPermission().then(permission => {
          if (permission === "granted") {
            new Notification(title, options);
          } else {
            return;
          }
        });
      } else {
        new Notification(title, options);
      }
    };
    return fireNotif;
  };
{% endhighlight %}
- 참고 : https://developer.mozilla.org/ko/docs/Web/API/notification