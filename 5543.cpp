#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int prices[5];
	for (int i = 0; i < 5; i++) {
		scanf("%d", &prices[i]);
	}

	int sum = 0;
	int min = 5000;
	for (int i = 0; i < 3; i++) {
		for (int j = 3; j < 5; j++) {
			sum = prices[i] + prices[j];
			if (sum < min)
				min = sum;
			sum = 0;
		}
		sum = 0;
	}

	printf("%d", min-50);

	return 0;
}