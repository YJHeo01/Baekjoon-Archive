//https://www.acmicpc.net/board/view/151506 답변 검증용

#include <stdio.h>

int compatibility[17];

int sum(int x) {
  return (compatibility[x] + compatibility[x + 1]) % 10;
}

int main(void) {
  int phoneNumberA[8];
  int phoneNumberB[8];
  
  for(int i = 0; i < 8; i++) {
    scanf("%1d", &phoneNumberA[i]);
  }
  
  for(int i = 0; i < 8; i++) {
    scanf("%1d", &phoneNumberB[i]);
  }
  
  for(int i = 0; i < 8; i++) {
   compatibility[2 * i] = phoneNumberA[i];
   compatibility[(2 * i) + 1] = phoneNumberB[i]; 
  }
  
  for(int i = 16; 2 < i; --i) {
    for(int j = 0; j < i; j++) {
      compatibility[j] = sum(j);
    }
  }
  
  for(int i = 0; i < 2; i++) {
    printf("%d", compatibility[i]);
  }
  return 0;
}