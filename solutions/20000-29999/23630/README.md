# 23630 - 가장 긴 부분 수열 구하기

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 1 초 | 512 MB |

## 문제

<p>$N$개의 자연수로 이루어진 수열 $A = \{A_1, A_2, …, A_N\}$가 주어진다.</p>

<p>다음의 조건을 모두&nbsp;만족하는 $A$의 부분 수열 $\{A_{i_1}, A_{i_2}, ..., A_{i_m}\}$ 중 가장 긴 수열의 길이를 출력하라.</p>

<ol>
	<li>$A_{i_1}&nbsp;~\&amp;~ A_{i_2}&nbsp;~\&amp;~ …&nbsp;~\&amp;~ A_{i_m} \neq 0$ ($\&amp;$: <a href="https://www.acmicpc.net/problem/23042#hint">Bitwise AND</a>)</li>
	<li>$1 \leq i_1 &lt; i_2&nbsp; &lt; … &lt; i_m \leq N$</li>
</ol>

<p>예를 들어 $A = \{5, 6, 7, 11, 15\}$인 경우,</p>

<ul>
	<li>$\{5, 6, 11\}$은 <strong>조건 1</strong>을 만족하지 않는다. ($0101_{2}&nbsp;~\&amp;~ 0110_{2}&nbsp;~\&amp;~ 1011_{2}&nbsp;= 0000_{2}$)</li>
	<li>$\{5, 5\}$는&nbsp;<strong>조건 2</strong>를 만족하지 않는다. ($i_1 \nless i_2$)</li>
	<li>$\{5, 6, 7, 15\}$는 조건을 모두 만족하는&nbsp;가장 긴 부분 수열이다.</li>
</ul>

## 입력

<p>첫 번째 줄에는 수열 $A$의 길이를 나타내는 정수&nbsp;$N$이 주어진다. 두 번째 줄에는 수열 $A$의 각 원소&nbsp;$A_i$가 공백으로 구분되어&nbsp;주어진다.</p>

<ul>
	<li>$1 \leq N \leq&nbsp;1,000,000$</li>
	<li>$1 \leq A_i&nbsp;\leq&nbsp;1,000,000$ ($1 \leq&nbsp;i \leq&nbsp;N$)</li>
</ul>

## 출력

<p>첫 번째 줄에 조건을 모두 만족하는 가장 긴 부분 수열의 길이를&nbsp;출력한다.</p>

## 태그

- 성공
- 애드 혹
- 비트마스킹
