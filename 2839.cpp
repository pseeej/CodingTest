#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int n;
	scanf("%d", &n);

	int count = 0;

	while (n > 0) {
		if (n % 5 == 0) {
			count++;
			n -= 5;
		}
		else if (n % 3 == 0) {
			count++;
			n -= 3;
		}
		else if (n > 5) {
			count++;
			n -= 5;
		}
		else {
			count = -1;
			break;
		}
	}

	printf("%d", count);

	return 0;
}