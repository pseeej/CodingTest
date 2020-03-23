#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int N, M;
	scanf("%d %d", &N, &M);

	int* arr = (int*)malloc(sizeof(int)*N);

	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}

	int opt = 0;
	int sum;

	for (int i = 0; i < N-2; i++) {
		for (int j = i+1; j < N-1; j++) {
			for (int k = j+1; k < N; k++) {
				sum = arr[i] + arr[j] + arr[k];
				if (sum<=M && sum>=opt)
					opt = sum;
			}
		}
	}

	printf("%d\n", opt);

	return 0;
}