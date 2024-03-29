---
layout: post
title:  "트리 (Tree)"
date:   2024-02-13 23:16:00 +0900
categories: 이론&nbsp;-&nbsp;자료&nbsp;구조
tags: [트리, 힙]
---

### 트리란?

- 1:n 관계의 비선형 자료 구조
- 계층 관계로 만들어진 계층형 자로구조이기도 하다.

### 트리의 구성

- 노드 (Node)
    - 트리를 구성하는 원소 (자료)
- 간선 (Edge)
    - 노드를 연결하는 선
- 레벨 (Level)
    - 트리의 깊이
    - 한 단계씩 들어갈 수록 1씩 증가한다.
    - 0부터 시작한다.
- 높이 (Height)
    - 트리의 최대 깊이
    - 만약에 최하위 레벨이 3이라면 높이도 3이 된다.
- 루트 (Root)
    - 트리의 시작이 되는 레벨
    - 레벨 0라고 부르기도 한다.
- 루트 노드 (Root Node)
    - 트리의 시작 노드
- 부모 노드 (Parent Node)
    - 하위 레벨의 노드를 보유하고 있는 상위 노드
- 자식 노드 (Child Node)
    - 부모 노드에 속해 있는 하위 노드
- 조상 노드 (Ancestor Node)
    - 해당 노드에서 루트 노드에 이르기까지에 해당하는 모든 부모 노드
- 형제 노드 (Sibling Node)
    - 같은 부모 노드를 가진 자식 노드
- 단말 노드 (Terminal Node)
    - 자식 노드가 없는 노드
    - 차수가 0인 노드를 의미한다.
    - 리프 노드(Leaf Node)라고도 부른다.
- 내부 노드 (Internal Node)
    - 차수가 1 이상인 노드
- 서브 트리 (Sub Tree)
    - 해당 노드의 하위 레벨에 존재하는 트리
- 노드의 차수 (Node's Degree)
    - 한 노드가 가지는 서브 트리의 수
    - 자식 노드의 수와 같은 의미다.
    - 1레벨 아래에 있는 노드만 해당되며, 그보다 더 아래 레벨에 있는 노드들은 포함되지 않는다.
- 트리의 차수 (Tree's Degree)
    - 해당 노드를 포함한 하위의 모든 서브 트리들에 포함되어 있는 노드의 차수 중 가장 높은 값
- 포레스트 (Forest)
    - 여러 개의 트리 집합
    - n개의 서브 트리를 가진 루트 노드를 제거하면 n개의 트리가 생기며,  
    분리된 트리들이 포레스트를 이룬다.

### 트리 예시

```mermaid
flowchart TD
    A --- B
    A --- C
    A --- D
    B --- E
    B --- F
    C --- G
    C --- H
    C --- I
    C --- J
    F --- K
    F --- L
```

### 이진 트리

#### 이진 트리란(Binary Tree)?

- 트리의 모든 노드의 차수를 2 이하로 제한하여 전체 트리의 차수가 2 이하가 되도록 정의한 것
- 트리의 구조를 일정하게 제한하여 정의하면 트리의 연산이 단순하고 명확해진다.

#### 이진 트리의 특징

- 좌우가 구분된 왼쪽과 오른쪽 자식 노드 두 개만 가질 수 있다.
- 값이 저장되어 있지 않은 공백 노드도 이진 트리의 노드로 취급한다.
- 노드가 n개인 이진 트리는 항상 간선이 (n-1)개다.
- 높이가 h인 이진 트리가 가질 수 있는 노드 개수는 최소 (h+1)개이며, 최대 (2<sup>h+1</sup> - 1)개이다.

#### 일반 트리를 이진 트리로 변환하는 법

1. 첫번째 자식 노드 간선만 남기고 나머지 간선을 제거한다.
2. 형제 노드를 간선으로 연결한다.
3. 시계 방향으로 45도 회전한다.

#### 이진 트리의 종류

##### 포화 이진 트리 (Full Binary Tree)

- 모든 레벨에 존재하는 노드가 꽉 차있어서  
높이를 늘리지 않는 한 노드를 추가할 수 없는 포화 상태의 이진 트리
- 높이가 h일 때 노드가 (2<sup>h+1</sup> - 1)개로 최대 노드 수를 갖는다.
- 포화 이진 트리의 노드는 위치에 따라 일정한 노드 번호를 붙일 수 있다.
    - 루트 노드를 1번으로 한다.
    - 하위 레벨로 내려가면서 왼쪽에서 오른쪽으로 차례로 (2<sup>h+1</sup> - 1)까지 번호를 붙인다.
    - 만약 높이가 3이라면 번호는 1 ~ 15를 사용한다.

##### 완전 이진 트리 (Complete Binary Tree)

- 높이가 h이고, 노드 수가 n개일 때 (단 n < 2<sup>h+1</sup> - 1),  
노드 위치가 포화 이진 트리에서의 노드 1번부터 n번까지의 위치와 완전히 일치하는 이진 트리
- 완전 이진 트리에서는 (n+1)번부터 (2<sup>h+1</sup> - 1)번까지 노드는 모두 값이 없는 공백 노드가 된다.

##### 편향 이진 트리 (Skewed Binary Tree)

- 이진 트리 중에서 최소한의 노드만 가지고 있는 이진 트리
- 높이가 h일 때 h+1개의 노드를 가지면서 모든 노드가 왼쪽이나 오른쪽 중 한 방향으로만 서브 트리르 가지고 있는 트리

#### 이진 트리의 순회

- 순회 (Travesal)
    - 모든 원소를 빠뜨리거나 중복하지 않고 처리하는 연산
- 리스트, 스택, 큐 등과 같은 선형 자료구조는  
원소를 1:1 관계로 구성하기 때문에 순회 연산을 별도로 작성할 필요가 없다.
- 이진 트리는 1:2의 비선형 계층 구조이므로  
현재 노드를 처리한 후에 어떤 노드를 처리할지 결정하는 기준을 정해 놓은 순회 연산이 필요하다.

##### 순회를 위한 작업의 종류

- 작업 D
    - 현재 노드를 방문하여 처리한다.
- 작업 L
    - 현재 노드의 왼쪽 서브 트리로 이동한다.
- 작업 R
    - 현재 노드의 오른쪽 서브 트리로 이동한다.

##### 전위 순회 (Preorder Traversal)

- D → L → R 순서로 순회한다.

##### 중위 순회 (Inorder Traversal)

- L → D → R 순서로 순회한다.

##### 후위 순회 (Postorder Traversal)

- L → R → D 순서로 순회한다.

##### 순회 종류별 예시

```mermaid
flowchart TD
    A --- B
    A --- C
    B --- D
    B --- E
    C --- F
    C --- G
    D --- H
    E --- I
    E --- J
    G --- K
```

- 전위 순회 경로
    - A → B → D → H → E → I → J → C → F → G → K
- 중위 순회 경로
    - H → D → B → I → E → J → A → F → C → G → K
- 후위 순회 경로
    - H → D → I → J → E → B → F → K → G → C → A

#### 스레드 이진 트리 (Thread Binary Tree)

- 재귀호출 없이 순화할 수 있도록 수정한 이진 트리

##### 스레드 이진 트리의 탄생 배경

- 이진 트리는 부모 노드와 자식 노드의 이진 트리 기본 구조가  
각 레벨에서 순환적으로 반복되어 전체 트리가 구성되는 구조다.
- 그래서 각 노드에서의 순회 연산을 재귀호출을 이용하여  
순환적으로 반복하여 전체 트리에 대한 순회를 처리하였다.
- 재귀 호출 방식의 알고리즘이나 함수 구현은 간단하지만,  
수행 성능 측면에서는 시스템 스택을 사용하면서 호출과 복귀를 관리해야 하고  
이진 트리의 하위 레벨로 내려 갈수록 재귀호출의 깊이가 깊어지므로 비효율적일 수 있다.
- 이런 문제를 고려하여 재귀호출 없이 순화할 수 있도록 수정한 이진 트리가 스레드 이진 트리다.

##### 스레드 이진 트리의 구성

- 스레드 (Thread)
    - 자식 노드가 없는 경우에 널 포인터 대신 순회 순서상의 다른 노드를 가리키도록 설정하는 링크 필드
- 선행자 (Predecessor)
    - 현재 노드 직전에 처리한 노드
- 후행자 (Successor)
    - 현재 노드 직후에 처리할 노드

##### 스레드 이진 트리에서 스레드를 만드는 방법

1. 이진 트리의 순회 경로에 따라 선행자에 대한 포인터를 현재 노드의 왼쪽 널 링크 대신에 저장한다.
2. 후행자에 대한 포인터를 현재 노드의 오른ㅉ꼬 널 링크 대신에 저장한다.

##### 스레드 이진 트리의 특징

- 재귀호출 없이 순화할 수 있다.
- 스레드 이진 트리에서는 순회를 위해서  
현재 노드의 다음 노드를 재귀호출을 이용하여 처리하지 않고  
오른쪽 링크 필드의 포인터를 이용한다.
- 이진 트리의 순회 경우는 순회의 종류가 전위/중위/후위 중 어떤 것이냐에 따라 달라지므로  
사용할 순회 방법을 먼저 정하고 그 순회 경로에 따라 스레드를 설정한다.

### 이진 탐색 트리

#### 이진 탐색 트리(Binary Search Tree)란?

- 이진 트리를 탐색용 자료구조로 사용하기 위해 원소 크기에 따라 노드 위치를 정의한 것

#### 이진 탐색 트리의 정의

- 모든 원소는 서로 다른 유일한 키를 갖는다.
- 왼쪽 서브 트리에 있는 원소들의 키는 그 루트의 키보다 작다.
- 오른쪽 서브 트리에 있는 원소들의 키는 그 루트의 키보다 크다.
- 왼쪽 서브 트리와 오른쪽 서브 트리도 이진 탐색 트리다.

#### 이진 탐색 트리의 탐색 연산

- 전제
    - 이진 탐색 트리에서 키 값이 x인 원소를 탐색한다.
    - 탐색은 항상 루트 노드에서 시작하므로 먼저 키값 x와 루트 노드의 키값을 비교한다.
- 결과
    - (키값 x = 루트 노드의 키값)인 경우
        - 원하는 원소를 찾았으므로 탐색 연산에 성공
    - (키값 x <> 루트 노드의 키값)인 경우
        - 루트 노드의 왼쪽 서브 트리에서 탐색 연산 수행
    - (키값 x > 루트 노드의 키값)인 경우
        - 루트 노드의 오른쪽 서브 트리에서 탐색 연산 수행

#### 이진 탐색 트리의 삽입 연산

- 이진 탐색 트리에 원소를 삽입하려면 이진 탐색 트리에 같은 원소가 있는지 먼저 확인해야 한다.
- 탐색 연산을 수행하여 성공하면 이미 같은 원소가 트리에 있다는 뜻이므로  
삽입 연산을 수행하지 않는다.
- 탐색 연산을 수행하여 실패하면 삽입하려는 원소가 트리에 없다는 뜻이므로  
탐색 실패가 발생한 현재 위치에 원소를 삽입한다.

#### 이진 탐색 트리의 삭제 연산

- 이진 탐색 트리에서 노드를 삭제할 때도 삭제할 노드의 위치를 탐색하는 작업을 먼저 수행해야 한다.
- 삭제할 노드는 자식 노드의 수에 따라 3가지 경우 중 하나에 속한다.
    - 삭제할 노드가 단말 노드인 경우 (차수 = 0)
    - 삭제할 노드가 자식 노드를 1개 가진 경우 (차수 = 1)
    - 삭제할 노드가 자식 노드를 2개 가진 경우 (차수 = 2)
- 노드를 삭제한 후에도 이진 탐색 트리를 유지해야하므로  
삭제할 노드의 종류에 따라서 후속 조치가 필요하다.

##### 삭제할 노드가 단말 노드인 경우

- 해당 노드를 삭제하고 부모 노드의 링크 필드를 NULL로 설정한다.

##### 삭제할 노드가 자식 노드를 1개 가진 경우

- 대상이 되는 노드를 삭제하면 자식 노드는 트리에서 떨어진 고아 노드가 된다.
- 고아 노드가 되는 걸 방지하기 위해 자식 노드를 부모 노드의 자리로 올려주는 후처리 작업을 한다.
- 대상이 되는 노드를 삭제하면 자식 노드가 부모 노드의 자리를 물려받아 이진 탐색 트리를 재구성한다.

##### 삭제할 노드가 자식 노드를 2개 가진 경우

- 대상이 되는 노드를 삭제하면 자식 노드는 트리에서 떨어진 고아 노드가 된다.
- 고아 노드가 되는 걸 방지하기 위해 자식 노드를 부모 노드의 자리로 올려주는 후처리 작업을 한다.
- 그러나 자식 노드가 1개일 때와는 다르게 물려줄 노드를 선택해야 한다.
- 직계 자식 노드뿐만 아니라 전체 자손 노드 중에서 후계자를 찾는다.
- 노드가 삭제되고 이진 탐색 트리의 정의를 만족해야 한다.
    - 후계자로 선택된 자손 노드의 키값은 왼쪽 서브 트리에 있는 노드들의 키값보다 커야 한다.
    - 후계자로 선택된 자손 노드의 키값은 오른쪽 서브 트리에 있는 노드들의 키값보다 작야 한다.
- 즉, 2가지 중 1가지에 해당하는 자손 노드가 자리를 물려받게 된다.
    - 왼쪽 서브 트리에서 키값이 가장 큰 노드
    - 오른쪽 서브 트리에서 키값이 가장 작은 노드

### 균형 이진 탐색 트리

#### 균형 이진 탐색 트리(Balanced Binary Search Tree)란?

- 이진 탐색 트리에 왼쪽 서브 트리의 높이와 오른쪽 서브 트리의 높이에 대한 균형을 조건을 추가하여 정의한 트리
- 이진 탐색 트리가 한쪽으로 치우치지 않고 균형을 이루도록 맞춰주면 탐색 성능을 높일 수 있다.
    - 최소 높이를 가지면서 n개의 노드를 가진 이진 탐색 트리의 비교 연산 횟수
        - O(log<sub>2</sub>n)
    - 최대 높이를 가지면서 n개의 노드를 가진 이진 탐색 트리의 비교 연산 횟수
        - O(n)
- 균형 트리(Balanced Tree)라고도 부른다.

#### AVL 트리 (Adelson-Velskii, Landis Tree)

- 대표적인 균형 이진 탐색 트리
- 각 노드에서 왼쪽 서브 트리의 높이와 오른쪽 서브 트리의 높이의 차이가 1 이하인 트리
- 관련 용어
    - hL (height of Left subtree)
        - 해당 노드에서 왼쪽 서브 트리의 높이
    - hR (height of Left subtree)
        - 해당 노드에서 오른쪽 서브 트리의 높이
- 특징
    - 왼쪽 서브 트리 < 부모 노드 < 오른쪽 서브 트리의 관계를 갖는다.
    - 각 노드의 (hL-hR)을 노드의 균형 인수(BR, Balance Factor)라고 한다.
    - 각 노드의 균형 인수로 {-1, 0, +1} 값만 가지게 함으로써  
    왼쪽 서브 트리와 오른쪽 서브 트리의 균형을 맞춘다.
- 회전 (Rotation) 연산
    - 이진 탐색 트리처럼 노드를 삭제한 후에 트리를 재구성하듯이 동작하는 AVL 트리의 연산
    - 불균형 유형
        - LL 유형
            - 불균형 발생 노드의 왼쪽 자식 노드와 자식의 왼쪽 노드에 의해 왼쪽으로 치우침
            - LL 회전을 적용해야 함
        - RR 유형
            - 불균형 발생 노드의 오른쪽 자식 노드와 자식의 오른쪽 노드에 의해 왼쪽으로 치우침
            - RR 회전을 적용해야 함
        - LR 유형
            - 불균형 발생 노드의 왼쪽 자식 노드와 자식의 오른쪽 노드에 의해 왼쪽으로 치우침
            - LR 회전을 적용해야 함
        - RL 유형
            - 불균형 발생 노드의 오른쪽 자식 노드와 자식의 왼쪽 노드에 의해 왼쪽으로 치우침
            - RL 회전을 적용해야 함
    - 회전 유형
        - LL 회전
            - 문제 구간 중 상위 구간을 오른쪽으로 회전시킴
        - RR 회전
            - 문제 구간 중 상위 구간을 왼쪽으로 회전시킴
        - LR 회전
            1. 문제 구간 중 하위 구간을 왼쪽으로 회전 시켜 LL 유형으로 변환
            2. LL 회전 적용
        - RL 회전
            1. 문제 구간 중 하위 구간을 오른쪽으로 회전 시켜 RR 유형으로 변환
            2. RR 회전 적용
    - 단순 회전 (Single Rotation)
        - 한 번만 회전하는 것
        - LL 회전과 RR 회전이 해당한다.
    - 이중 회전 (Double Rotation)
        - 두 번 회전하는 것
        - LR 회전과 RL 회전이 해당한다.

### 힙 (Heap)

#### 힙이란?

- 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해 만든 자료구조
- 힙은 같은 키값의 노드를 중복해서 가질 수 있다.
- 일반적으로 말하는 힙은 최대 힙을 의미한다.

#### 최대 힙 (Max Heap)

- 키값이 가장 큰 노드를 찾기 위한 힙
- 최대 힙은 부모 노드의 키값이 자식 노드의 키값보다 항상 크거나 같은 크기의 관계를 가지는 노드들의 완전 이진 트리다.
- 최대 힙에서는 키값이 가장 큰 노드가 루트 노드가 된다.

#### 최소 힙 (Min Heap)

- 키값이 가장 작은 노드를 찾기 위한 힙
- 최대 힙은 부모 노드의 키값이 자식 노드의 키값보다 항상 작거나 같은 크기의 관계를 가지는 노드들의 완전 이진 트리다.
- 최대 힙에서는 키값이 가장 작은 노드가 루트 노드가 된다.

#### 힙의 삽입 연산

1. 완전 이진 트리의 조건이 만족하도록 다음 자리를 확장한다.
2. 부모 노드와 크기 조건이 만족하도록 삽입 원소의 위치를 찾는다.

#### 힙의 삭제 연산

- 힙에서 원소를 삭제하는 연산은 언제나 루트 노드에 있는 원소를 삭제하여 반환한다.
- 루트 노드의 원소를 삭제한 후에도 다음과 같은 조건을 만족해야 한다.
    - 완전 이진 트리의 형태
    - 노드의 키값에 대한 힙의 조건
- 최대 힙에서 수행하는 삭제 연산은 언제나 키값이 가장 큰 원소를 삭제하여 반환하는 연산이 된다.
- 최소 힙에서 수행하는 삭제 연산은 언제나 키값이 가장 작은 원소를 삭제하여 반환하는 연산이 된다.