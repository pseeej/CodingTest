#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int toNum(char c);

int main() {

	char grandma[15];
	scanf("%s", grandma);

	int* numbers = (int*)malloc(sizeof(int)*strlen(grandma));

	int time = 0;

	for (int i = 0; i < (int)strlen(grandma); i++) {
		time += toNum(grandma[i]) + 1;
	}

	printf("%d\n", time);

	free(numbers);

	return 0;
}

int toNum(char c) {
	int num;

	switch (c) {
	case 'A':
	case 'B':
	case 'C':
		num = 2;
		break;
	case 'D':
	case 'E':
	case 'F':
		num = 3;
		break;
	case 'G':
	case 'H':
	case 'I':
		num = 4;
		break;
	case 'J':
	case 'K':
	case 'L':
		num = 5;
		break;
	case 'M':
	case 'N':
	case 'O':
		num = 6;
		break;
	case 'P':
	case 'Q':
	case 'R':
	case 'S':
		num = 7;
		break;
	case 'T':
	case 'U':
	case 'V':
		num = 8;
		break;
	default:
		num = 9;
		break;
	}

	return num;
}