#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int v, a, b;
	scanf("%d %d %d", &a, &b, &v);
	int day;
	day = (v - b - 1) / (a - b) + 1;

	printf("%d", day);


	return 0;
}