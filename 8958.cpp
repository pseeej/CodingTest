#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);

	char ox[80];
	int score, count;

	for (int i = 0; i < times; i++) {
		score = 0;
		count = 0;
		scanf("%s", ox);
		for (int j = 0; j < (int)strlen(ox); j++) {
			if (ox[j] == 'X') {
				count = 0;
			}
			if (ox[j] == 'O') {
				count++;
				score += count;
			}
		}
		printf("%d\n", score);
	}



	return 0;
}