---
layout: post
title:  "Redis의 다양한 자료구조"
date:   2025-02-24 07:00:00 +0900
categories:  Redis
published: false
---

Strings, Sets, Sorted Sets, Lists, Hashes, Bitmaps, Bitfields, HyperLogLog, Geospatial indexes, Streams

### 출처

[Data structures](https://redis.io/technology/data-structures/)  
[[REDIS] 📚 자료구조 명령어 종류 & 활용 사례 💯 총정리](https://inpa.tistory.com/entry/REDIS-%F0%9F%93%9A-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%80%EC%9E%85Collection-%EC%A2%85%EB%A5%98-%EC%A0%95%EB%A6%AC)  
[[Redis] Redis 자료구조 알아보기](https://sabarada.tistory.com/134)  
[Redis 기본 자료구조](https://velog.io/@6v6/Redis-%EA%B8%B0%EB%B3%B8-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)  
[[Redis] 레디스 알고 쓰자. - 정의, 저장방식, 아키텍처, 자료구조, 유효 기간](https://velog.io/@banggeunho/%EB%A0%88%EB%94%94%EC%8A%A4Redis-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90.-%EC%A0%95%EC%9D%98-%EC%A0%80%EC%9E%A5%EB%B0%A9%EC%8B%9D-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%9C%A0%ED%9A%A8-%EA%B8%B0%EA%B0%84#redis-%EC%9E%90%EB%A3%8C-%EA%B5%AC%EC%A1%B0)  
[Redis의 기본 자료구조 및 사용법](https://devoong2.tistory.com/entry/Redis%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EB%B2%95#google_vignette)