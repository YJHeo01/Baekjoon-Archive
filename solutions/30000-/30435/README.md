# 30435 - Die Hard

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 1 초 (추가 시간 없음) | 1024 MB |

## 문제

<p>John and Hans are playing a game involving 3 dice. Even though they are all 6-sided, they are not guaranteed to be identical.</p>

<p>First John picks one of the dice and then Hans picks one of the remaining two. Then they both roll their chosen die. If they roll the same number, they both re-roll their die. Otherwise the winner is the one who rolled the highest number.</p>

<p>In case neither John or Hans can win with their chosen dice, they do not bother to re-roll the dice indefinitely and no winner is declared.</p>

<p>Can you help John pick a die that guarantees that he wins with a probability of at least $\frac{1}{2}$?</p>

## 입력

<p>The input consists of three lines. Line $i$ contains $6$ positive integers $x_j$ ($1 \leq x_j \leq 1000$), describing the sides of the $i$'th die.</p>

## 출력

<p>Output the smallest $i \in \{1, 2, 3\}$, such that John can pick die $i$ and be guaranteed to win with probability at least $\frac{1}{2}$. If no such die exists, output "No dice".</p>

## 태그

- 성공
- 다국어
- 수학
- 구현
- 브루트포스 알고리즘
- 확률론
