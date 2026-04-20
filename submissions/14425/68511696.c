#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct student
{
	char name[500];
	struct student* next;
};

typedef struct student STUDENT;
#define SIZE 500
STUDENT* hashTable[SIZE];

int hashFunction(char* str) {
	//문자값을 모두 더한다
	int sum = 0;
	int len = strlen(str);
	int i;
	for (i = 0; i < len; i++) {
		sum += str[i];
	}
	// % size
	return(sum % SIZE);
}

void addToHashTable(char* name) {
	STUDENT* cur = (STUDENT*)malloc(sizeof(STUDENT));
	int idx;
	strcpy(cur->name, name);
	cur->next = 0;

	idx = hashFunction(name);

	if (hashTable[idx] == 0) {
		hashTable[idx] = cur;
		return;
	}
	else {
		STUDENT* temp = hashTable[idx];
		while (temp->next != 0) {
			temp = temp->next;
		}
		temp->next = cur;
		return;
	}
}

int searchInHash(char* name) {
	STUDENT* cur;
	int i = hashFunction(name);
	cur = hashTable[i];
	if (cur == 0) {
		return 0;
	}
	while (strcmp(cur->name, name) != 0) {
		cur = cur->next;
		if (cur == 0) {
			return 0;
		}
	}
	return 1;
	
}
int main() {
    int m,n;
    scanf("%d %d",&n,&m);
    char name[500];
    for(int i=0;i<n;i++){
    scanf("%s",name);
	addToHashTable(name);
    }
    int cnt = 0;
    for(int i=0;i<m;i++)
	{   scanf("%s",name);
        cnt += searchInHash(name);
    }
    printf("%d",cnt);
}