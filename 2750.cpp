#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {
	int N;
	scanf("%d", &N);

	int* arr = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			int tmp;
			if (arr[i] > arr[j]) {
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}

	for (int i = 0; i < N; i++)
		printf("%d\n", arr[i]);

	free(arr);

	return 0;
}