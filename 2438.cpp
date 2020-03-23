#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);

	for (int i = 0; i < times; i++) {
		for (int j = times-1; j > i; j--) {
			printf(" ");
		}
		for (int j = i; j >= 0; j--)
			printf("*");
		printf("\n");
	}

	return 0;
}