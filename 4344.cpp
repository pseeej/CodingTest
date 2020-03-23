#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int total_times;
	scanf("%d", &total_times);

	int times;
	int* scores;
	int sum;

	for (int i = 0; i < total_times; i++) {
		scanf("%d", &times);
		scores = (int*)malloc(sizeof(int)*times);
		sum = 0;
		for (int j = 0; j < times; j++) {
			scanf("%d", &scores[j]);
			sum += scores[j];
		}
		double avg;
		avg = sum / (double)times;
		double percent = 0;
		for (int j = 0; j < times; j++) {
			if (scores[j] > avg)
				percent = percent + (1.0 / times);
		}
		printf("%0.3f%%\n", percent*100);
		free(scores);
	}



	return 0;
}