#include <stdio.h>
#include <math.h>

#define NUMBER 10000

int check(int num);

int main() {


	for (int i = 1; i < NUMBER; i++) {
		int result = 1;
		for (int j = 1; j < NUMBER; j++) {
			if (check(j) == i) {
				result = 0;
				break;
			}
			else;
		}
		if (result == 1)
			printf("%d\n", i);
	}

	return 0;
}

int check(int num) {

	int ten = 1;
	int mid = num;
	while (mid > 0) {
		mid /= (int)pow(10, 1);
		if (mid > 0)
			ten++;
	}

	int res = num;
	switch (ten) {
	case 4:
		res += (num / (int)pow(10, 3));
		num %= (int)pow(10, 3);
	case 3:
		res += (num / (int)pow(10, 2));
		num %= (int)pow(10, 2);
	case 2:
		res += (num / (int)pow(10, 1));
		num %= (int)pow(10, 1);
	case 1:
		res += (num / (int)pow(10, 0));
	}

	return res;
}