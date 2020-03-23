#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main() {

	char N[10000];
	scanf("%s", N);

	for (int i = 0; i < (int)strlen(N); i++) {
		for (int j = 0; j < (int)strlen(N); j++) {
			char temp;
			if (N[i] > N[j]) {
				temp = N[i];
				N[i] = N[j];
				N[j] = temp;
			}
		}
	}

	for (int i = 0; i < (int)strlen(N); i++)
		printf("%c", N[i]);
	
	return 0;
}