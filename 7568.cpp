#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int N;
	scanf("%d", &N);

	int* height = (int*)malloc(sizeof(int)*N);
	int* weight = (int*)malloc(sizeof(int)*N);
	int* rank = (int*)malloc(sizeof(int)*N);

	for (int i = 0; i < N; i++)
		scanf("%d %d", &weight[i], &height[i]);

	for (int i = 0; i < N; i++) {
		int cnt = 0;
		for (int j = 0; j < N; j++) {
			if ((height[i] < height[j]) && (weight[i] < weight[j])) {
				cnt++;
			}
			else;
		}
		rank[i] = cnt + 1;
	}

	for (int i = 0; i < N; i++)
		printf("%d ", rank[i]);

	free(height);
	free(weight);
	free(rank);

	return 0;
}