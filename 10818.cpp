#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);

	int min = 1000000;
	int max = -1000000;

	int num;
	for (int i = 0; i < times; i++) {
		scanf("%d", &num);
		if (num < min)
			min = num;
		if (num > max)
			max = num;
	}

	printf("%d %d", min, max);


	return 0;
}