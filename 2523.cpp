#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int num;
	scanf("%d", &num);

	for (int i = 1; i <= num * 2 - 1; i++) {
		if (i <= num) {
			for (int j = 1; j <= i; j++) {
				printf("*");
			}
		}
		else {
			for (int j = i; j <= num * 2 - 1; j++)
				printf("*");
		}
		printf("\n");
	}

	return 0;
}