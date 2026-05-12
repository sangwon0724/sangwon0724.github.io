---
layout: post
title:  "쿠키"
date:   2023-12-15 13:12:00 +0900
categories: Spring&nbsp;MVC
tags: [쿠키]
---

### 쿠키 생성하기

{% highlight java %}
//1. 쿠키 객체 생성하기
Cookie cookie = new Cookie("속성명", "값");

//2. HttpServletResponse 객체에 추가하기 (변수명 : response)
response.addCookie(cookie);
{% endhighlight %}

### 쿠키 사용하기

- 컨트롤러 메소드의 매개변수로 쿠키 사용
    {% highlight java %}
    @RequestMapping("/main")
    public String mallIndex(@CookieValue(value="가져올쿠키명", required=false) Cookie cookie, HttpServletRequest request) {
        if(cookie != null)
            System.out.pringln("쿠키값 : "+cookie);

        return "/common/main";
    }
    {% endhighlight %}

- 주의점
    ○ required=false를 입력하지 않으면 만약 쿠키가 없을 때 에러가 발생한다.

### 쿠키 삭제하기

{% highlight java %}
cookie.setMaxAge(0); //존재 시간을 0초로 하기
{% endhighlight %}