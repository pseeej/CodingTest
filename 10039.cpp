#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int sum = 0;

	for (int i = 0; i < 5; i++) {
		int score;
		scanf("%d", &score);
		if (score < 40)
			score = 40;
		sum += score;
	}

	printf("%d\n", sum / 5);


	return 0;
}