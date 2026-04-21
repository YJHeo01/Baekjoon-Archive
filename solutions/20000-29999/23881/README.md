# 23881 - 알고리즘 수업 - 선택 정렬 1

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 1 초 | 512 MB |

## 문제

<p>오늘도 서준이는 선택 정렬&nbsp;수업 조교를 하고 있다.&nbsp;아빠가 수업한&nbsp;내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><em>N</em>개의 서로 다른 양의&nbsp;정수가 저장된&nbsp;배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우&nbsp;<em>K&nbsp;</em>번째 교환되는 수를 구해서 우리 서준이를 도와주자.</p>

<p>크기가 <em>N</em>인 배열에 대한&nbsp;선택 정렬&nbsp;의사 코드는&nbsp;다음과 같다.</p>

<pre>selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last &lt;- N downto 2 {
&nbsp;       A[1..last]중 가장 큰 수 A[i]를 찾는다
&nbsp;       if (last != i) then A[last] &lt;-&gt; A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
    }
}</pre>

## 입력

<p>첫째 줄에 배열 A의 크기&nbsp;<em>N</em>(5&nbsp;≤&nbsp;<em>N</em>&nbsp;≤ 10,000), 교환 횟수&nbsp;<em>K</em>(1 ≤&nbsp;<em>K</em>&nbsp;≤ N)가&nbsp;주어진다.</p>

<p>다음&nbsp;줄에 서로 다른 배열 A의 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다.&nbsp;(1&nbsp;≤ A<sub>i</sub>&nbsp;≤ 10<sup>9</sup>)</p>

## 출력

<p><em>K&nbsp;</em>번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력한다. 교환 횟수가 <em>K&nbsp;</em>보다 작으면 -1을 출력한다.</p>

## 태그

- 성공
- 구현
- 정렬
- 시뮬레이션
