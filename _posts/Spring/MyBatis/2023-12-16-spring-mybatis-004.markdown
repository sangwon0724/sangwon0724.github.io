---
layout: post
title:  "데이터 치환"
date:   2023-12-16 16:27:00 +0900
categories: MyBatis
tags: [CDATA]
---

### 태그를 삭제하고 싶은 경우

- REGEXP_REPLACE(칼럼명, 정규식, 교체 내용) 함수를 사용한다.
- 사용 예시
    {% highlight sql %}
    /* html 태그를 빈 문자열로 교체한다. */
    REGEXP_REPLACE(title, '&lt;[^>]*>|\&([^;])*;', '') LIKE '%${search}%'
    {% endhighlight %}

### 특수문자를 사용하고 싶은 경우

- &lt;![CDATA[ 내용 ]]>을 사용한다.
- 사용 예시
    {% highlight sql %}
    SELECT
        TITLE, CONTENT
    FROM
        BLOG_POST
    WHERE
        USE_YN = 'Y'
        <![CDATA[
            AND (
                REGEXP_REPLACE(title, '&lt;[^>]*>|\&([^;])*;', '') LIKE '%${search}%'
                or 
                REGEXP_REPLACE(content, '&lt;[^>]*>|\&([^;])*;', '') LIKE '%${search}%'
            )
        ]]>
    {% endhighlight %}