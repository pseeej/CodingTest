#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);

	for (int i = 0; i < times; i++) {
		int how;
		scanf("%d", &how);
		char word[20];
		scanf("%s", word);
		for (int l = 0; l < (int)strlen(word); l++) {
			for (int k = 0; k < how; k++) {
				printf("%c", word[l]);
			}
		}
		printf("\n");

	}


	return 0;
}