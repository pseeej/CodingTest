#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)

int main() {

	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	while (a != 0 && b != 0 && c != 0) {
		int max;
		int othera, otherb;
		if (a > b && a > c) {
			max = a;
			othera = b;
			otherb = c;
		}
		else if (b > a && b > c) {
			max = b;
			othera = a;
			otherb = c;
		}
		else {
			max = c;
			othera = a;
			otherb = b;
		}

		if (pow(othera, 2) + pow(otherb, 2) == pow(max, 2))
			printf("right\n");
		else
			printf("wrong\n");

		scanf("%d %d %d", &a, &b, &c);
	}



	return 0;
}