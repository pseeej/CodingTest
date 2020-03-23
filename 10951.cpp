#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int one, two;

	while (scanf("%d %d", &one, &two)!=EOF) {
		printf("%d\n", one + two);
	}

	return 0;
}