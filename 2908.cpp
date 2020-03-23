#include <stdio.h>
#pragma warning(disable:4996)

int reverse(int num);

int main() {

	int num1, num2;
	scanf("%d %d", &num1, &num2);

	num1 = reverse(num1);
	num2 = reverse(num2);

	if (num1 > num2)
		printf("%d\n", num1);
	else
		printf("%d\n", num2);

	return 0;
}

int reverse(int num) {

	int one, ten, hund;
	hund = num % 10;
	ten = num / 10 % 10;
	one = num / 100;

	return (hund * 100 + ten * 10 + one);

}