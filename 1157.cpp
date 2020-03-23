#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

char getLarge(char alphabet);
char getSmall(char alphabet);

int main() {

	char word[1000000];
	scanf("%s", word);

	char alpha[26];
	int times[26] = { 0, };

	for (int i = 0; i < 26; i++)
		alpha[i] = 'a' + i;

	for (int i = 0; i < (int)strlen(word); i++) {
		for (int j = 0; j < 26; j++) {
			if (getSmall(word[i]) == alpha[j]) {
				times[j]++;
				break;
			}
		}
	}

	int max = 0;
	int max_index;

	for (int i = 0; i < 26; i++) {
		if (times[i] > max) {
			max = times[i];
			max_index = i;
		}
	}

	int count = 0;
	for (int i = 0; i < 26; i++) {
		if ((times[i] == max) && (count != 0)) {
			printf("?");
			count++;
			break;
		}
		else if (times[i] == max)
			count++;
	}

	if (count == 1)
		printf("%c", getLarge(alpha[max_index]));
	else;

	return 0;
}

char getLarge(char alphabet) {
	if (alphabet >= 'a' && alphabet <= 'z')
		alphabet -= 32;
	else;

	return alphabet;
}

char getSmall(char alphabet) {
	if (alphabet >= 'A' && alphabet <= 'Z')
		alphabet += 32;
	else;

	return alphabet;
}