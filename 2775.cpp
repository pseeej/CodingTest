#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);

	int apt[15][15];
	for (int i = 1; i <= 14; i++) {
		apt[0][i] = i;
		apt[i][1] = 1;
	}

	for (int i = 1; i <= 14; i++) {
		for (int j = 2; j <= 14; j++) {
			apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
		}
	}

	int floor, room;
	for (int i = 0; i < times; i++) {
		scanf("%d", &floor);
		scanf("%d", &room);
		printf("%d\n", apt[floor][room]);
	}


	return 0;
}