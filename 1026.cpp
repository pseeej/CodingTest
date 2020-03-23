#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int N;
	scanf("%d", &N);

	int* A = (int*)malloc(sizeof(int)*N);
	int* B = (int*)malloc(sizeof(int)*N);

	for (int i = 0; i < N; i++)
		scanf("%d", &A[i]);
	for (int i = 0; i < N; i++)
		scanf("%d", &B[i]);

	int S = 0;
	
	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			int temp;
			if (A[i] > A[j]) {
				temp = A[i];
				A[i] = A[j];
				A[j] = temp;
			}
			if (B[i] < B[j]) {
				temp = B[j];
				B[j] = B[i];
				B[i] = temp;
			}
		}
	}

	for (int i = 0; i < N; i++)
		S += A[i] * B[i];

	printf("%d", S);
	
	free(A);
	free(B);

	return 0;
}