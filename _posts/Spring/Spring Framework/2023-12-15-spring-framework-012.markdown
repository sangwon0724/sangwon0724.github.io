---
layout: post
title:  "PSA (Portable Service Abstraction)"
date:   2023-12-15 13:11:00 +0900
categories: Spring&nbsp;Framework
---

### PSA란?

- 하나의 추상화로 여러 서비스를 묶어둔 것
- 항상 일관된 방식의 기술로의 접근 환경을 제공하는 추상화 구조

### 서비스 추상화란?

- 추상화 계층을 사용하여 어떤 기술을 내부에 숨기고 개발자에게 편의성을 제공해주는 것
- 추상화의 개념을 애플리케이션에서 사용하는 서비스에 적용하는 기법

### PSA가 필요한 이유

- PSA를 통해서 요구 사항 변경에 유연한 대처가 가능하다.
    - 사용되는 기술 스펙이 변경되는 등의 요구사항 변경이 일어나도 최소한의 변경만으로 대처가 가능하다.

### 동작 원리

{% highlight java %}
//s:인터페이스 생성
    public interface JdbcConnector {
        Connection getConnection();
    }
//e:인터페이스 생성

//s:인터페이스 구현
    public class MariaDBJdbcConnector implements JdbcConnector {
        @Override
        public Connection getConnection() {
            return null;
        }
    }
    public class OracleJdbcConnector implements JdbcConnector {
        @Override
        public Connection getConnection() {
            return null;
        }
    }
    public class SQLiteJdbcConnector implements JdbcConnector {
        @Override
        public Connection getConnection() {
            return null;
        }
    }
//e:인터페이스 구현

//s:PSA 적용
JdbcConnector connector = new MariaDBJdbcConnector();
connector = new OracleJdbcConnector();
connector = new SQLiteJdbcConnector();
//e:PSA 적용
{% endhighlight %}