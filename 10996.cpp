#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n * 2; i++) {
		for (int j = 1; j <= n; j++) {
			if (i % 2 == 0) {
				if (j % 2 == 0)
					printf("*");
				else
					printf(" ");
			}
			else {
				if (j % 2 == 0)
					printf(" ");
				else
					printf("*");
			}
		}
		printf("\n");
	}

	return 0;
}