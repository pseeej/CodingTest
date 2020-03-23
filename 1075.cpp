#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int N, F;
	scanf("%d", &N);
	scanf("%d", &F);

	int change = N - (N % 100);

	while (change % F != 0) {
		change++;
	}

	printf("%02d", change % 100);


	return 0;
}