#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int number;
	scanf("%d", &number);

	int count = 1;
	int six = 6;
	int left, right = 1;

	while (number > right) {
		count++;
		left = right + 1;
		right += six;
		six += 6;
	}

	printf("%d", count);

	return 0;
}