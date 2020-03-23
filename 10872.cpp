#include <stdio.h>
#pragma warning(disable:4996)

int fact(int num);

int main() {

	int n;
	scanf("%d", &n);
	if (n == 0)
		printf("1");
	else
		printf("%d", fact(n));

	return 0;
}

int fact(int num) {
	if (num-1 > 1)
		num = num * fact(num - 1);
	else;

	return num;
}