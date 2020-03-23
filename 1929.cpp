#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	int m, n;

	scanf("%d %d", &m, &n);

	int arr[1000001] = { 0,1 };

	for (int i = 2; i <= n; i++)
		for (int j = 2; i*j <= n; j++)
			arr[i*j] = 1;
	
	for (int i = m; i < n + 1; i++) {
		if (arr[i] != 1)
			printf("%d\n", i);
	}
	
	return 0;
}