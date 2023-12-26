---
layout: post
title:  "resultMap"
date:   2023-12-16 16:36:00 +0900
categories: MyBatis
tags: [resultMap]
---

### resultMap이란?

- 데이터를 계층적으로 저장할수 있게 해주는 유틸 (요약 : vo 모음집)

### 1:1 매핑 (association)

- 가정
    - 특정 이벤트에 참여한 유저들의 정보를 저장한다.

- vo
    {% highlight java %}
    //유저 테이블
    @Data  
    public class Member{
        private String member_id; //유저 아이디
        private String name; //이름
        private String phone_number; //연락처
        private String home_address; //주소
    }

    //이벤트 참가자 테이블
    @Data  
    public class EventParticipant{
        private int no; //번호
        private String event_id; //이벤트 고유 ID
        private String member_id; //참가한 유저 아이디

        Member member;
    }
    {% endhighlight %}

- SQL
    {% highlight xml %}
    <!-- ★ resultType이 아닌 resultMap을 사용 -->
    <!-- ★ resultMap 속성의 값으로는 작성한 resultMap의 id를 명시 -->
    <select id="list" parameterType="hashmap" resultMap="eventParticipantMap">
    SELECT 
        E.NO,
        E.EVENT_ID,
        M.MEMBER_ID,
        M.NAME,
        M.PHONE_NUMBER,
        M.HOME_ADDRESS
    FROM
        EventParticipant E
        INNER JOIN MEMBER M
        ON E.MEMBER_ID = M.MEMBER_ID
    WHERE
        EVENT_ID = #{event_id}
    </select>
    {% endhighlight %}

- resultMap
    {% highlight xml %}
    <!-- resultMap 태그 →  id 속성 : 사용할 resultMap의 고유 id -->
    <!-- resultMap 태그 → type 속성 : 데이터를 저장할 클래스 -->
    <resultMap id="eventParticipantMap" type="com.my.vo.EventParticipant">
        <!-- property: 해당 VO에서 사용하는 필드명 -->
        <!-- column : 실제 Database에서 사용중인 칼럼명 -->
        <result property="no" column="NO" />
        <result property="event_id" column="EVENT_ID" />
        <result property="member_id" column="MEMBER_ID" />

        <!-- association 태그 → property 속성 : 참조 객체 변수명 -->
        <!-- 예시 : EventParticipant 클래스에서 MEMBER 클래스를 member라고 명시했으니 해당 속성의 값은 member가 된다. -->
        <!-- association 태그 → javaType 속성 : 해당 참조 객체가 사용하는 클래스 -->
        <!-- ★ association → id 태그 : Primary Key -->
        <association property="member" javaType="com.my.vo.Member">
            <id property="member_id" column="MEMBER_ID" />
            <result property="name" column="NAME" />
            <result property="phone_number" column="PHONE_NUMBER" />
            <result property="home_address" column="HOME_ADDRESS" />
        </association>
    </resultMap>
    {% endhighlight %}

### 1:N 매핑 (collection)

- 가정
    - 특정 게시글에 대해서 작성되어 있는 댓글 목록을 가져온다.

- vo
    {% highlight java %}
    //게시글 테이블
    @Data
    public class Board{
        private int no; //고유 번호
        private String title; //제목
        private String content; //내용
        private String writer; //작성자
        private Date sign_date; //작성일
        private Data modify_date; //수정일

        private List<Comment> comments; //댓글 목록
    }

    //댓글 테이블
    @Data
    public class Comment{
        private int no; //고유 번호
        private String content; //내용
        private String writer; //작성자
        private Date sign_date; //작성일
        private Data modify_date; //수정일

        private int board_no; //댓글을 작성한 게시글의 고유 번호
    }
    {% endhighlight %}

- sql
    {% highlight xml %}
    <!-- 게시글 정보 -->
    <select id="getOneBoard" resultMap="boardInfo">
    SELECT 
        NO,
        TITLE,
        CONTENT,
        WRITER,
        SIGN_DATE,
        MODIFY_DATE
    FROM
        Board B
    WHERE
        NO = #{no}
    </select>

    <!-- 댓글용 서브쿼리 -->
    <select id="getCommentList" resultType="com.my.vo.Comment">
    SELECT 
        NO,
        CONTENT,
        WRITER,
        SIGN_DATE,
        MODIFY_DATE,
        BOARD_NO
    FROM
        Comment C
    WHERE
        BOARD_NO = #{no}
    </select>
    {% endhighlight %}

- result
    {% highlight xml %}
    <!-- resultMap 태그 →  id 속성 : 사용할 resultMap의 고유 id -->
    <!-- resultMap 태그 → type 속성 : 데이터를 저장할 클래스 -->
    <resultMap id="boardInfo" type="com.my.vo.Board">
        <result property="no" column="NO"/>
        <result property="title" column="TITLE"/>
        <result property="content" column="CONTENT"/>
        <result property="writer" column="WRITER"/>
        <result property="sign_date" column="SIGN_DATE"/>
        <result property="modify_date" column="MODIFY_DATE"/>

        <!-- collection 태그 → property 속성 : 참조 객체 변수명 -->
        <!-- 예시 : Board 클래스에서 Comment 클래스를 comments라고 명시했으니 해당 속성의 값은 comments가 된다. -->
        <!-- collection 태그 → column 속성 : 서브쿼리에서 참조할 값이 될 메인쿼리의 칼럼 -->
        <!-- 값을 여러개 참조해야 할 때는 column="{prop1=COLUMN1, prop2=COLUMN2}"처럼 쓰면 된다. -->
        <!-- collection 태그 → javaType 속성 : List로 받을 것이기 때문에 java.util.ArrayList가 된다. -->
        <!-- collection 태그 → ofType 속성 : List로 받을 객체 클래스-->
        <!-- collection 태그 → select 속성 : List로 결과 값을 받기 위해 실행할 서브쿼리의 id -->
        <collection property="comments" column="NO" javaType="java.util.ArrayList" ofType="com.my.vo.Comment" select="getCommentList"/>
    </resultMap>
    {% endhighlight %}