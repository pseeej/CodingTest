#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);

	float sum = 0;
	float* scores = (float*)malloc(times * sizeof(float));
	float max=0;

	for (int i = 0; i < times; i++) {
		scanf("%f", &scores[i]);
		if (scores[i] > max)
			max = scores[i];
	}

	for (int i = 0; i < times; i++) {
		scores[i] = (scores[i] / max) * 100;
		sum += scores[i];
	}

	double avg = sum / times;

	printf("%.2f", avg);



	return 0;
}