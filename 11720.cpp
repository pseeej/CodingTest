#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int how;
	scanf("%d ", &how);

	char one;
	int sum=0;

	for (int i = 1; i <= how; i++) {
		scanf("%c", &one);
		sum += (one - '0');
	}

	printf("%d\n", sum);


	return 0;
}