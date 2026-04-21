# 23983 - Product Triplets

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 40 초 (추가 시간 없음) | 1024 MB |

## 문제

<p>Given&nbsp;<b>N</b>&nbsp;integers&nbsp;<b>A</b><sub>1</sub>,&nbsp;<b>A</b><sub>2</sub>, ...,&nbsp;<b>A</b><sub><b>N</b></sub>, count the number of triplets (x, y, z) (with 1 ≤ x &lt; y &lt; z ≤&nbsp;<b>N</b>) such that at least one of the following is true:</p>

<ul>
	<li><b>A</b><sub>x</sub>&nbsp;=&nbsp;<b>A</b><sub>y</sub>&nbsp;×&nbsp;<b>A</b><sub>z</sub>, and/or</li>
	<li><b>A</b><sub>y</sub>&nbsp;=&nbsp;<b>A</b><sub>x</sub>&nbsp;×&nbsp;<b>A</b><sub>z</sub>, and/or</li>
	<li><b>A</b><sub>z</sub>&nbsp;=&nbsp;<b>A</b><sub>x</sub>&nbsp;×&nbsp;<b>A</b><sub>y</sub></li>
</ul>

## 입력

<p>The first line of the input gives the number of test cases,&nbsp;<b>T</b>.&nbsp;<b>T</b>&nbsp;test cases follow. Each begins with one line containing an integer&nbsp;<b>N</b>: the number of integers in array&nbsp;<b>A</b>. The second line consists of&nbsp;<b>N</b>&nbsp;integers&nbsp;<b>A</b><sub>i</sub>; the i-th of these is the value of the i-th integer, as described above.</p>

## 출력

<p>For each test case, output one line containing&nbsp;<code>Case #x: y</code>, where&nbsp;<code>x</code>&nbsp;is the test case number (starting from 1) and&nbsp;<code>y</code>&nbsp;is the number of triplets satisfying the condition given in the problem statement.</p>

## 태그

- 실패
- 서브태스크
- 다국어
- 보기
- 수학
- 자료 구조
- 브루트포스 알고리즘
- 많은 조건 분기
- 해시를 사용한 집합과 맵
