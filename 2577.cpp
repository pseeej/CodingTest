#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)

int main() {

	int nums[3];
	int mul = 1;

	for (int i = 0; i < 3; i++) {
		scanf("%d", &nums[i]);
		mul *= nums[i];
	}

	int count[10] = { 0, };

	int div = 1;

	while (mul/div > 0){
		for (int j = 0; j < 10; j++) {
			if ((mul/div)%10 == j) {
				count[j]++;
			}
		}
		div *= 10;
	}

	for (int i = 0; i < 10; i++)
		printf("%d\n", count[i]);

	return 0;
}