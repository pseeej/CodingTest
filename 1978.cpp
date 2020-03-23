#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);

	int number;
	int count = 0;
	for (int i = 0; i < times; i++) {
		int check = 1;
		scanf("%d", &number);
		if (number == 1)
			check = 0;
		for (int j = 2; j < number; j++) {
			if (number%j == 0) {
				check = 0;
				break;
			}
		}
		if (check == 1)
			count++;
	}

	printf("%d", count);



	return 0;
}