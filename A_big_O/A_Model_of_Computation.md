#시간복잡도
### Random Access Memory
#### 상수 시간 Θ(1)에 할 수 있는 일
* load word r(i) into register r(j)
  * word를 레지스터로 로드하기
* compute +, -, *, /, &, |, ^
  * 단순연산 하기
* store register r(j) into memory r(i)
  * word를 메모리로 저장하기

<br>
<hr>
<br>

###pointer machine
#### 동적 할당된 객체
* 하나의 필드는 O(1) 속성 1개를 가짐
* 속성: word 혹은 pointer 혹은 null 값을 가짐
* Weaker than RAM

<br>
<hr>
<br>

###python model
#### python에서는 RAM, Pointer machine 둘다 상수시간에 처리 가능하다
* RAM (=List)
  * L[i] = L[j] + 5 => 상수 시간 Θ(1)
* Pointer Machine
  * x = x.next => 상수 시간 Θ(1)

1. 리스트
   1. 요소 추가, L.append(x)
      * 상수 시간 Θ(1)
   2. 리스트 통합, L = L1 + L2
      * 2n => Θ(n)
    ``` python
    for x in L1  # n
        L.append(x)
    for x in L2  # n
        L.append(x)
    ```
   3. 리스트에 리스트 추가하기, L1.extend(L2)
      * Θ(n)
    ``` python
    for x in L2
    ```
   4. 리스트 길이 확인
      * Θ(n) 걸리지만, 파이썬은 카운터가 있으므로 Θ(1)
   5. 리스트에 다른 리스트 일부 추가
      * Θ(n)
   6. 리스트 내 검색
      * Θ(n)
 
2. 튜플
   * 리스트와 매우 유사한 시간 복잡도
3. 딕셔너리
   * 임의의 key 지정/저장 (해싱)
   * Θ(1) w.h.p
4. set
   * 딕셔너리와 유사(vals를 제외한다고 생각)
5. 기타
   * 힙 큐, long => 나중에


<br>
<hr>
<br>

## 시간복잡도가 큰 순서
* ![img.png](img.png)
  * n! > 2^x > x^3 > x^2 > nlogn > n > logn > 1(상수)