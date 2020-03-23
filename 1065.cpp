#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)

int check(int num);

int main() {

	int number;
	scanf("%d", &number);
	int count = 0;

	for (int i = 1; i <= number; i++) {
		if (check(i) == 1) {
			count++;
		}
		else;
	}

	printf("%d", count);

	return 0;
}

int check(int num) {

	int mid = num;
	int place = 0;

	while (mid > 0) {
		mid /= (int)pow(10, 1);
		if (mid > 0)
			place++;
	}

	int one = 0, ten = 0, hun = 0;


	switch (place) {
	case 2:
		hun = num / 100;
		num %= 100;
	case 1:
		ten = num / 10;
		num %= 10;
	case 0:
		one = num;
	}

	if (place == 2 && ((hun - ten) == (ten - one)))
		return 1;
	else if (place == 1 || place == 0)
		return 1;
	else
		return 0;

}