#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int hr, min;
	scanf("%d %d", &hr, &min);

	if (min >= 45)
		printf("%d %d", hr, min - 45);
	else if (hr > 0)
		printf("%d %d", hr - 1, min + 60 - 45);
	else
		printf("23 %d", min + 60 - 45);

	return 0;
}