#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	if (c <= b)
		printf("-1\n");
	else
		printf("%d", a / (c - b) + 1);


	return 0;
}