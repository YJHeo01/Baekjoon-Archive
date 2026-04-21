# 15119 - Purple Rain

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 1 초 | 512 MB |

## 문제

<p>Purple rain falls in the magic kingdom of Linearland which is a straight, thin peninsula.</p>

<p>On close observation however, Professor Nelson Rogers finds that the purple rain is actually a mix of red and blue raindrops.</p>

<p>In his zeal, he records the location and color of the raindrops in different locations along the peninsula. Looking at the data, Professor Rogers wants to know which part of Linearland had the “least” purple rain.</p>

<p>After some thought, he decides to model this problem as follows. Divide the peninsula into n sections and number them west to east from 1 to n. Then, describe the raindrops as a sequence of R and B, depending on whether the rainfall in each section is primarily red or blue. Finally, find a subsequence of contiguous sections where the difference between the number of R and the number of B is maximized.</p>

## 입력

<p>The input consists of a single line containing a string of n characters (1 ≤ n ≤ 10<sup>5</sup>), describing the color of the raindrops in sections 1 to n.</p>

<p>It is guaranteed that the string consists of uppercase ASCII letters ‘R’ and ‘B’ only.</p>

## 출력

<p>Print, on a single line, two space-separated integers that describe the starting and ending positions of the part of Linearland that had the least purple rain. These two numbers should describe an inclusive range; both numbers you print describe sections included in the range.</p>

<p>If there are multiple possible answers, print the one that has the westernmost starting section. If there are multiple answers with the same westernmost starting section, print the one with the westernmost ending section.</p>

## 태그

- 성공
- 다국어
- 누적 합
