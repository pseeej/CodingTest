#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int N;
	scanf("%d", &N);
	
	for (int i = 1; i < N; ++i) {
		int sum = i;
		int part = i;

		while (part) {
			sum += part % 10;
			part /= 10;
		}

		if (N == sum) {
			printf("%d\n", i);
			return 0;
		}

	}

	printf("0");

	return 0;
}