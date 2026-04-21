# 6386 - Cog-Wheels

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 1 초 | 128 MB |

## 문제

<p>Your little sister has got a new mechanical building kit, which includes many cog-wheels of different sizes. She starts building gears with different ratios, but soon she notices that there are some ratios which are quite difficult to realize, and some others she cannot realize at all. She would like to have a computer program that tells her what ratios can be realized and what ratios cannot. She asks you to write a program that does the job.</p>

<p>&nbsp;</p>

<p>For example, let us assume that the kit contains cog-wheels with 6, 12, and 30 cogs. Your sister wants to realize a gear of ratio 5 : 4. One possible solution is shown in Figure 2.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/fe8edd7a-df66-4b0a-b6b2-ef572a387d18/-/preview/" style="width: 164px; height: 211px;"></p>

<p style="text-align: center;">Figure 2: Combination of cog-wheels realizing a gear of 5 : 4.</p>

<p>It depicts a complete gear of ratio 5 : 4. Four wheels are used: cog-wheels of sizes 30 and 12 on the first axis, cog-wheels of sizes 6 and 12 on the second axis. The gear ratio is given by</p>

<p>\[\frac{30}{12} \cdot \frac{6}{12} = \frac{5}{2} \cdot \frac{1}{2} = \frac{5}{4} = 5 : 4\]</p>

<p>as desired. However, a gear of ratio 1 : 6 cannot be realized using the cog-wheels your sister has.</p>

<p>Given the sizes of the cog-wheels in the kit (i.e. the number of cogs they have), decide whether a given gear ratio can be built or not. You may use any finite number of cog-wheels of each size available.</p>

## 입력

<p>The input begins with a line containing the number of scenarios.</p>

<p>The input for each scenario starts with a description of the cog-wheels in the kit. First, there is a line containing the number n of different sizes of cog-wheels (1 ≤ n ≤ 20). The next line contains n numbers c<sub>1</sub> . . . c<sub>n</sub>, separated by single blanks. These denote the n different sizes of the cog-wheels in the kit, with 5 ≤ c<sub>i</sub> ≤ 100 for i = 1, . . . , n. You may assume that there is a cog-wheel of smallest size c = min{c<sub>1</sub>, . . . , c<sub>n</sub>} in the kit such that all sizes c<sub>1</sub>, . . . , c<sub>n</sub> are multiples of c.</p>

<p>The line describing the available cog-wheels is followed by the list of gear ratios to be realized. It starts with a line containing the number m of ratios. The next m lines each contain two integers a and b, separated by a single blank. They denote the ratio a : b, with 1 ≤ a, b ≤ 10000.</p>

## 출력

<p>The output for every scenario begins with a line containing “<code>Scenario #i:</code>”, where <code>i</code> is the number of the scenario starting at 1. Then print the results for all the gear ratios given in that scenario. For each gear ratio a : b, print a line containing either</p>

<pre>Gear ratio a:b can be realized.</pre>

<p>or</p>

<pre>Gear ratio a:b cannot be realized.</pre>

<p>Terminate the output of each scenario with a blank line.</p>

## 태그

- 실패
- 다국어
- 보기
- 수학
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
