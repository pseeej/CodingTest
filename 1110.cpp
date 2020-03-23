#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int first;
	scanf("%d", &first);

	int ten = (first / 10);
	int one = (first % 10);
	int mid = one * 10 + ((ten + one) % 10);

	int count = 1;

	while (mid != first) {
		ten = mid / 10;
		one = mid % 10;
		mid = one * 10 + ((ten + one) % 10);
		count++;
	}

	printf("%d", count);

	return 0;
}