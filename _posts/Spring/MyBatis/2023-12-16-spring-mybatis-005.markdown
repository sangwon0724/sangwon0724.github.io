---
layout: post
title:  "설정 파일 이용하기"
date:   2023-12-16 16:31:00 +0900
categories: Group&nbsp;:&nbsp;Spring MyBatis
---

### 별칭 사용하기

1. 자신이 설정한 [프로젝트명/src/main/resources] 경로에 있는 mybatis 관련 설정 파일로 이동
2. &nbsp;configuration> 태그 안에 &nbsp;typeAliases> 태그 작성
3. &nbsp;typeAliases> 태그 안에 &nbsp;typeAlias type="com.my.vo.BoardVO" alias="BoardVO" />처럼 작성

{% highlight xml %}
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
  <typeAliases>
      <typeAlias type="com.my.vo.BoardVO" alias="BoardVO" />
  </typeAliases>
</configuration>
{% endhighlight %}

{% highlight xml %}
<!-- 별칭 사용 전 -->
<select id="selectPostA" resultType="com.my.vo.BoardVO" >
  SELECT * FROM BOARD WHERE CATEGORY=#{category} ORDER BY NO DESC
</select>

<!-- 별칭 사용 후 -->
<select id="selectPostB" resultType="BoardVO" >
  SELECT * FROM BOARD WHERE category=#{category} ORDER BY NO DESC
</select>
{% endhighlight %}

### 언더바(_)가 포함된 필드명 CamelCase로 맵핑하기

1. 자신이 설정한 [프로젝트명/src/main/resources] 경로에 있는 mybatis 관련 설정 파일로 이동
2. &lt;configuration> 태그 안에 <settings> 태그 작성
3. &lt;settings> 태그 안에 &lt;setting name="mapUnderscoreToCamelCase" value="true" /> 작성

{% highlight java %}
@Data
public class MemberVO{
  private String memberId; //실제 컬럼명 : MEMBER_ID
  private String phoneNumber; //실제 컬럼명 : PHONE_NUMBER
  private String homeAddress; //실제 컬럼명 : HOME_ADDRESS
}
{% endhighlight %}