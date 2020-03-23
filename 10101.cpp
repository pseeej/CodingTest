#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int a, b, c;
	int sum = 0;

	scanf("%d %d %d", &a, &b, &c);
	sum = a + b + c;

	if (a == 60 && b == 60 && c == 60)
		printf("Equilateral");
	else if (sum == 180 && ((a == b) || (b == c) || (a == c)))
		printf("Isosceles");
	else if (sum == 180 && a != b && b != c && a != c)
		printf("Scalene");
	else if (sum != 180)
		printf("Error");
	else;


	return 0;
}