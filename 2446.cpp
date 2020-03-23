#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int N;
	scanf("%d", &N);

	for (int i = 0; i < N * 2 - 1; i++) {
		if (i < N) {
			for (int k = 0; k < i; k++)
				printf(" ");
			for (int j = N * 2 - 1; j > i * 2; j--)
				printf("*");
		}
		else {
			for (int k = N * 2 - 1; k > i + 1; k--)
				printf(" ");
			for (int j = 1; j <= (i-N+2)*2-1; j++)
				printf("*");
		}
		printf("\n");
	}

	return 0;
}