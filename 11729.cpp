#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)

void hanoi(int n, int from, int tmp, int to);

int main() {

	int N;
	scanf("%d", &N);

	printf("%d\n", (int)pow(2, N) - 1);
	hanoi(N, 1, 2, 3);

	return 0;
}

void hanoi(int n, int from, int tmp, int to) {
	if (n == 1) {
		printf("%d %d\n", from, to);
	}
	else {
		hanoi(n - 1, from, to, tmp);
		printf("%d %d\n", from, to);
		hanoi(n - 1, tmp, from, to);
	}
}