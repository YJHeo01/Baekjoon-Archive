# 26638 - Nowy kontrakt

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 2 초 | 1024 MB |

## 문제

<p>Twoja firma, zajmująca się produkcją gier wideo, odniosła oszałamiający sukces – seria N gier o wędrującym przez Galaktykę pogromcy kwazarów sprzedała się znakomicie, przynosząc Ci sławę, pieniądze, a także niespodziewane kłopoty. Oto gruchnęła wieść, że znany pisarz science-fiction, na podstawie którego książek powstały Twoje gry, uznał właśnie, że prawa do adaptacji sprzedał po zbyt niskiej cenie i przez swoich prawników domaga się zmiany zapisów kontraktu.<sup>∗</sup></p>

<p>Umowa przewidywała, że za udzielenie licencji na grę numer i (gdzie i = 1, 2, . . . , N) pisarz otrzyma wynagrodzenie a<sub>i</sub>, będące pewną liczbą całkowitą dodatnią. Prawnicy argumentują jednak, że skoro każda następna gra sprzedawała się lepiej niż poprzednia, także wynagrodzenie powinno być wyższe. Chcesz uniknąć niepotrzebnego rozgłosu (a także paniki wśród akcjonariuszy), zatem ingerencja w zapis umowy powinna być jak najmniejsza. Zdecydowałeś się zatem do każdej z liczb a<sub>1</sub>, . . . , a<sub>N</sub> dopisać pewną liczbę cyfr na końcu tak, aby otrzymany w ten sposób nowy ciąg był ściśle rosnący. Dla każdego a<sub>i</sub> dopisane cyfry (oraz ich liczba) mogą być inne, możesz też niektórych liczb nie zmieniać w ogóle.</p>

<p>Rozstrzygnij, ile minimalnie cyfr musisz w tym celu łącznie dopisać.</p>

## 입력

<p>W pierwszym wierszu wejścia znajduje się jedna liczba całkowita N (1 ≤ N ≤ 200 000). W kolejnych N wierszach podane są liczby całkowite a<sub>1</sub>, . . . , a<sub>N</sub> (1 ≤ a<sub>i</sub> ≤ 10<sup>9</sup>).</p>

## 출력

<p>Twój program powinien wypisać na wyjście jedną liczbę całkowitą – minimalną możliwą liczbę dopisanych cyfr.</p>

## 태그

- 성공
- 다국어
- 구현
- 그리디 알고리즘
- 문자열
- 많은 조건 분기
