#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int left[10];

	for (int i = 0; i < 10; i++) {
		scanf("%d", &left[i]);
		left[i] %= 42;
	}

	int count = 0;
	for (int i = 0; i < 10; i++) {
		count++;
		for (int j = i+1; j < 10; j++) {
			if (left[i] == left[j]) {
				count--;
				break;
			}
			else;
		}
	}

	printf("%d", count);


	return 0;
}