#include <stdio.h>
#pragma warning(disable:4996)

int main() {
	int max=0, maxNum;
	int num;

	for (int i = 0; i < 9; i++) {
		scanf("%d", &num);
		if (num > max) {
			max = num;
			maxNum = i+1;
		}
	}

	printf("%d\n", max);
	printf("%d\n", maxNum);

	return 0;
}