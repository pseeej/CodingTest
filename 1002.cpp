#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)

int main() {

	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		int x1, y1, r1, x2, y2, r2;
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

		double d;
		int count;
		d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));

		int dist = r2 - r1;
		if (dist < 0)
			dist *= -1;

		if (dist < d && d < r1 + r2)
			count = 2;
		else if (d == r1 + r2)
			count = 1;
		else if (d == dist && d != 0)
			count = 1;
		else if (d < dist)
			count = 0;
		else if (d > r1 + r2)
			count = 0;
		else if (d == 0 && r1 == r2)
			count = -1;

		printf("%d\n", count);

	}



	return 0;
}