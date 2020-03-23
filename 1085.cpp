#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)

int main() {

	int x, y, w, h;
	scanf("%d %d %d %d", &x, &y, &w, &h);

	int distx, disty;
	
	if (x > w - x)
		distx = w - x;
	else
		distx = x;

	if (y > h - y)
		disty = h - y;
	else
		disty = y;

	
	if (distx < disty)
		printf("%d\n", distx);
	else
		printf("%d\n", disty);


	return 0;
}