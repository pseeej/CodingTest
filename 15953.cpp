#pragma warning(disable:4996)
#include <stdio.h>

int contest1(int first);
int contest2(int second = 0);

int main() {

	int tries;
	scanf("%d", &tries);
	int sums[tries];
	int count = 1;
	while (count <= tries) {
		int first = 0, second = 0;
		scanf("%d %d", &first, &second);

		int money1, money2;
		money1 = contest1(first);
		money2 = contest2(second);

		int sum = 0;
		sum = money1 + money2;
		sums[count] = sum;

		count++;
	}
	for (int i = 1; i <= tries; i++) {
		printf("%d\n", sums[i]);
	}

	return 0;
}

int contest1(int first) {
	if (first == 1)
		return 5000000;
	else if (first > 1 && first <= 3)
		return 3000000;
	else if (first > 3 && first <= 6)
		return 2000000;
	else if (first > 6 && first <= 10)
		return 500000;
	else if (first > 10 && first <= 16)
		return 300000;
	else if (first > 16 && first <= 22)
		return 100000;
	else
		return 0;
}

int contest2(int second) {
	if (second == 1)
		return 5120000;
	else if (second > 1 && second <= 3)
		return 2560000;
	else if (second > 3 && second <= 7)
		return 1280000;
	else if (second > 7 && second <= 15)
		return 640000;
	else if (second > 15 && second <= 31)
		return 320000;
	else return 0;
}