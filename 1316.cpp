#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int check(char* word);

int main() {

	int times;
	scanf("%d", &times);

	char word[100];

	int count = 0;

	for (int i = 0; i < times; i++) {
		scanf("%s", word);
		if (check(word) == 1)
			count++;
	}

	printf("%d", count);

	return 0;
}

int check(char* word) {
	int check_alpha[26] = { 0, };
	int result = 1;

	int temp;
	for (int i = 0; i < (int)strlen(word); i++) {
		temp = word[i] - 'a';
		if (check_alpha[temp] == 0)
			check_alpha[temp] = 1;
		else if ((check_alpha[temp] == 1) && (word[i] != word[i - 1])) {
			result = 0;
			break;
		}
		else if ((check_alpha[temp] == 1) && (word[i] == word[i - 1]))
			;
		else;
	}

	return result;
}