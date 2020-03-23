#include <stdio.h>
#pragma warning(disable:4996)

int main() {

	char sent[100];

	while(scanf("%[^\n]\n", sent)==1)
		printf("%s\n", sent);



	return 0;
}