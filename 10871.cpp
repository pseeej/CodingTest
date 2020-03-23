#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int times, find;
	scanf("%d %d", &times, &find);

	int* nums = (int*)malloc(sizeof(int)*times);
	for (int i = 0; i < times; i++)
		scanf("%d", &nums[i]);
	
	for (int i = 0; i < times; i++) {
		if (nums[i] < find)
			printf("%d ", nums[i]);
	}

	free(nums);

	return 0;
}