#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#pragma warning(disable:4996)

void star(int y, int x, int n);

int main() {

	int N;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			star(i, j, N);
		printf("\n");
	}

	return 0;
}

void star(int y, int x, int n) {
	if ((y/n) % 3 == 1 && (x/n) % 3 == 1)
		printf(" ");
	else {
		if (n / 3 == 0)
			printf("*");
		else
			star(y, x, n / 3);
	}
}