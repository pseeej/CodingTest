#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int find;
	scanf("%d", &find);

	int count = 0;
	int up = 0, down = 0;

	for (int j = 1; j <= find; j++) {
		for (int i = 0; i < j; i++) {
			if (j % 2 == 1) {
				up = j - i;
				down = i + 1;
			}
			else {
				down = j - i;
				up = i + 1;
			}
			count++;
			if (count == find)
				break;
		}
		if (count == find)
			break;
	}

	printf("%d/%d", up, down);

	return 0;
}