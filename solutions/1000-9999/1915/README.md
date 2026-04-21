# 1915 - 가장 큰 정사각형

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 1 초 | 128 MB |

## 문제

<p>n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.</p>

<table class="table table-bordered" style="width: 16%">
	<tbody>
		<tr>
			<td style="width: 4%; text-align: center;">0</td>
			<td style="width: 4%; text-align: center;">1</td>
			<td style="width: 4%; text-align: center;">0</td>
			<td style="width: 4%; text-align: center;">0</td>
		</tr>
		<tr>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">1</td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">0</td>
		</tr>
		<tr>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">0</td>
		</tr>
	</tbody>
</table>

<p>위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다.</p>

## 입력

<p>첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.</p>

## 출력

<p>첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.</p>

## 태그

- 성공
- 다이나믹 프로그래밍
