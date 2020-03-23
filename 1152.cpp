#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main() {

	char sent[1000001];
	fgets(sent, sizeof(sent), stdin);

	int count = 0;
	for (int i = 0; i < (int)strlen(sent); i++) {
		if (i == 0 && sent[i] == ' ')
			count--;
		if (i == strlen(sent) - 2 && sent[i] == ' ')
			count--;
		if (sent[i] == ' ')
			count++;
	}

	count++;

	printf("%d\n", count);

	return 0;
}