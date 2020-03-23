#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);
	
	int one, two;
	for (int i = 0; i < times; i++) {
		scanf("%d %d", &one, &two);
		printf("%d\n", one + two);
	}

	return 0;
}