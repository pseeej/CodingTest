#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int nums[3];

	scanf("%d %d %d", &nums[0], &nums[1], &nums[2]);

	int temp;
	for (int i = 0; i < 3; i++) {
		for (int i = 0; i < 2; i++) {
			if (nums[i] > nums[i + 1]) {
				temp = nums[i];
				nums[i] = nums[i + 1];
				nums[i + 1] = temp;
			}
		}
	}

	printf("%d", nums[1]);
	

	return 0;
}