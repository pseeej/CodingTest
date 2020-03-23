#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int a, b;
	int sum = 0, min = 10000;

	scanf("%d %d", &a, &b);

	for (int i = a; i <= b; i++) {
		int check = 1;
		if (i == 1)
			check = 0;
		for (int j = 2; j < i; j++) {
			if (i%j == 0) {
				check = 0;
				break;
			}
		}
		if (check == 1) {
			sum += i;
			if (i < min)
				min = i;
		}
	}

	if (sum > 0)
		printf("%d\n%d", sum, min);
	else
		printf("-1");

	return 0;
}