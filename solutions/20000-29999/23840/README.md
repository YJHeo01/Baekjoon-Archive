# 23840 - 두 단계 최단 경로 4

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 7 초 | 1024 MB |

## 문제

<p>서준이는 아빠로부터 생일선물로 세계 지도를 받아서&nbsp;매우 기뻤다. 세계 지도에서 최단 경로를 찾는 프로그램을 개발해서 아빠께 감사의 마음을 전달하려고 한다.&nbsp;세계 지도는 도시를 정점으로 갖고 도시 간의 도로를 간선으로 갖는 무방향성&nbsp;그래프이며(undirected graph), 도로의 길이가 간선의 가중치이다. 출발 정점&nbsp;<em>X</em>에서 출발해서 <em>P</em>개의 중간 정점&nbsp;<strong>모두를&nbsp;</strong>반드시 거친 후&nbsp;도착 정점&nbsp;<em>Z</em>에 도달하는 최단 거리를 구해서 우리 서준이를 도와주자.</p>

## 입력

<p>첫째 줄에 정점의 수&nbsp;<em>N</em>(10&nbsp;≤&nbsp;<em>N</em>&nbsp;≤ 100,000), 간선의 수&nbsp;<em>M</em>(10 ≤&nbsp;<em>M</em>&nbsp;≤ 300,000)이&nbsp;주어진다.</p>

<p>다음&nbsp;<em>M</em>개 줄에 간선 정보&nbsp;<em><code>u v w</code></em>가 주어지며 도시&nbsp;<em>u</em>와&nbsp;도시&nbsp;<em>v</em>&nbsp;사이의&nbsp;가중치가 정수&nbsp;<em>w</em>인 양방향&nbsp;도로를 나타낸다. (1 ≤&nbsp;<em>u</em>,&nbsp;<em>v</em>&nbsp;≤&nbsp;<em>N</em>,&nbsp;<em>u</em>&nbsp;≠&nbsp;<em>v</em>, 1 ≤&nbsp;<em>w</em>&nbsp;≤ 1,000,000)</p>

<p>다음 줄에&nbsp;<em><code>X Z</code></em>가 주어진다. (1 ≤&nbsp;<em>X</em>,&nbsp;<em>Z</em>&nbsp;≤&nbsp;<em>N</em>,&nbsp;<em>X</em>&nbsp;≠&nbsp;<em>Z</em>)</p>

<p>다음 줄에&nbsp;<em>P</em>가 주어진다. (3 ≤&nbsp;<em>P</em>&nbsp;≤ min(20,&nbsp;<em>N</em>&nbsp;- 3))</p>

<p>다음 줄에&nbsp;<em>P</em>개의 서로 다른 중간 정점&nbsp;<em>Y</em>(1 ≤&nbsp;<em>Y</em>&nbsp;≤&nbsp;<em>N</em>,&nbsp;<em>X</em>&nbsp;≠&nbsp;<em>Y</em>&nbsp;≠&nbsp;<em>Z</em>)가&nbsp;빈칸을 사이에 두고 주어진다.</p>

## 출력

<p>출발 정점&nbsp;<em>X</em>에서 출발해서 모든&nbsp;<em>P</em>개의 중간 정점을&nbsp;반드시 거친 후&nbsp;도착 정점&nbsp;<em>Z</em>에 도달하는 최단 거리를 출력한다. 도착 정점&nbsp;<em>Z</em>에 도착할 수 없는 경우 -1을 출력한다.</p>

## 태그

- 성공
- 다이나믹 프로그래밍
- 그래프 이론
- 비트마스킹
- 최단 경로
- 데이크스트라
- 비트필드를 이용한 다이나믹 프로그래밍
- 외판원 순회 문제
