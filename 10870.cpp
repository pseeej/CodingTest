#include <stdio.h>
#pragma warning(disable:4996)

int fib(int num);

int main() {

	int n;
	scanf("%d", &n);

	printf("%d", fib(n));

	return 0;
}

int fib(int num) {
	if (num == 0)
		return 0;
	if (num == 1)
		return 1;
	else
		return fib(num - 1) + fib(num - 2);
}