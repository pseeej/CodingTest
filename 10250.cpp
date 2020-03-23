#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main() {

	int times;
	scanf("%d", &times);

	int h, w, n;
	int floor, room;
	for (int i = 0; i < times; i++) {
		scanf("%d %d %d", &h, &w, &n);

		if (n%h == 0) {
			floor = h;
			room = n / h;
		}
		else {
			floor = n % h;
			room = (n / h) + 1;
		}

		if (room >= 10)
			printf("%d%d\n", floor, room);
		else
			printf("%d0%d\n", floor, room);
	}


	return 0;
}