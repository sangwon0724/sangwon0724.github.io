---
layout: post
title:  "기본 사용법"
date:   2023-12-16 16:18:00 +0900
categories: Group&nbsp;:&nbsp;Spring MyBatis
---

### 사용법 (v 3.0 이상)

1. 해당 기능 그룹에 관련된 SQL을 사용할 xml 파일의 namespace에 해당 기능에 대해서 작성하는 DAO interface명으로 짓는다.
  - 예시
    - com.my.mapper.BlogMapper
2. DAO로 사용할 패키지에서 각각의 기능 그룹에 대한 interface를 만든다.
  - 예시
    - 블로그에 대한 DAO를 만든다고 했을 때 BlogMapper (interface)
3. DAO의 interface에서 public [반환형] [메소드명] (매개변수)  throws Exception;의 형태로 메소드를 정의한다.
  - 예시
     - public List<HashMap<String, Object>> selectPost(Map<String, Object> map) throws Exception;
4. 작성된 메소드는 해당 메소드를 필요로 하는 서비스에서 호출하여 사용한다.
  - 예시
    {% highlight java %}
    @Autowired
    private BlogMapper mapper;
    @Override
    public List<HashMap<String, Object>> selectPost(Map<String, Object> map) throws Exception {
        return mapper.selectPost(map);
    }
    {% endhighlight %}
5. root-context.xml의 SqlSession에 등록된 정보에 따라 사용할 DAO interface를 namespace로 지정한  
*Mapper.xml을 찾아서 호출한 메소드명과 같은 id의 SQL을 실행한다.

### SqlSession 메소드

- <T> T selectOne(String statement, Object Parameter)
  - 하나의 객체를 리턴하는 조회 구문 수행 메소드
- <E> List<E> selectList(String statement, Object Parameter)
  - 한 개 이상의 객체를 리턴하는 조회 구문 수행 메소드
- <K, V> Map<K, V> selectMap (String, statement, Object Parameter, String mapKey)
  - 결과 데이터를 Map 으로 변환하기 위해 제공되는 메소드
- <T> Cursor<T> selectCursor(String statement, Object Parameter)
  - 결과 데이터를 Cursor 객체로 반환하는 메소드
- int insert(String statement, Object parameter)
  - SQL 구문에 의해 영향을 받은 레코드(행) 수를 반환하는 메소드
- int update(String statement, Object parameter)
  - SQL 구문에 의해 영향을 받은 레코드(행) 수를 반환하는 메소드
- int delete(String statement, Object parameter)
  - SQL 구문에 의해 영향을 받은 레코드(행) 수를 반환하는 메소드

>※ 위 모든 메소드들은 Object parameter 없이 호출될 수 있도록 오버로딩 되어있다.

### 쿼리 수행 태그

- 태그 종류
  - select
  - insert
  - update
  - delete

    
- 쿼리 수행 태그의 속성 (공통)
  - id
    - 해당 매퍼 파일에서 사용되는 유일한 값
  - parameterType
    - 쿼리 수행에 필요한 전달 파라미터의 데이터타입을 명시하는 속성 (예시 : hashmap)
  - flushCache
    - 구문이 실행될 때마다 캐시를 지울 것인지 설정하는 항목 (기본값 : false)
  - timeout
    - 데이터베이스 처리 결과를 기다리는 최대 시간
  - statementType
    - 쿼리 수행방식에 대한 설정
    - PreparedStatement(기본값)
    - Statement
    - Callable

- 쿼리 수행 태그의 속성 (select 태그 전용)
  - resultType
    - SELECT 수행 결과를 처리할 데이터타입 (실제 데이터 타입, 예시 : hashmap),
    - 참조형(VO)이라면 패키지까지 포함하여 풀패키지명으로 작성한다 (예시 : com.my.vo.BlogVO)
  - resultMap
    - SELECT 수행 결과를 처리할 &lt;resultMap> 태그를 이용하여 생성한 id를 이용한다
  - useCache
    - 구문의 결과를 캐시에 저장할 것인지 설정하는 항목 (기본값 : true)
  - fetchSize
    - SELECT 결과를 한번에 가져올 크기(개수)를 설정하는 속성 (기본값 : 10)
    - 대용량 데이터 처리 필요시 약 1000 정도로 사용한다.
    - 메모리와 연관되어있기 부분이기 때문에 많은 생각과 고민이 필요하다.
  - resultSetType
    - 조회 결과값을 읽어오는 동작에 대한 설정
    - FORWARD_ONLY
    - SCROLL_SENSITIVE
    - SCROLL_INSENSITIVE

>※ 수행할 SQL 쿼리에 맞게 태그를 골라 작성하면 된다.

>※ 각 태그의 이름은 역할을 나눌뿐이기 때문에 쿼리와 똑같지 않은 태그를 사용해도 실행은 되지만 왠만하면 일치시키는것이 좋다.

>※ 주로 사용하는 속성은 id, parameterType, resultType, resultMap정도다.