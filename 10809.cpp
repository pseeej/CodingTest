#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main() {

	char alpha[26];

	int j = 0;

	for (char i = 'a'; j<26; i++, j++) {
		alpha[j] = i;
	}

	char s[100];

	scanf("%s", s);

	int res[26];

	for (int i = 0; i < 26; i++) res[i] = -1;

	for (int i = 0; i < strlen(s); i++) {
		for (int j = 0; j < 26; j++) {
			if ((s[i] == alpha[j]) && res[j] == -1) {
				res[j] = i;
			}
		}
	}

	for (int i = 0; i < 26; i++)
		printf("%d ", res[i]);

	return 0;
}