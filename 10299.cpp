#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

double checkWonso(char alpha);

int main() {

	char chem[100];

	int N;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%s", chem);
		double sum = 0;
		double wonso = 0;
		int check = 1;
		for (int j = 0; j < (int)strlen(chem); j++) {
			wonso = checkWonso(chem[j]);
			if (chem[j + 1] >= '0' && chem[j + 1] <= '9' && chem[j + 2] >= '0' && chem[j + 2] <= '9') {
				int mult = (chem[j + 1] - '0') * 10 + (chem[j + 2] - '0');
				sum += wonso * mult;
				j += 2;
			}
			else if (chem[j + 1] >= '0' && chem[j + 1] <= '9') {
				sum += wonso * (chem[j + 1] - '0');
				j++;
			}
			else {
				sum += wonso;
			}

			if (j + 1 < (int)strlen(chem) && checkWonso(chem[j + 1]) == 0) {
				printf("Invalid formula\n");
				check = 0;
				sum = 0;
				break;
			}

		}
		if (check == 1 && sum != 0)
			printf("%.4f\n", sum);
	}


	return 0;
}

double checkWonso(char alpha) {

	double wonsoNum[5] = { 15.9994, 12.011, 1.00794, 32.066, 14.00674 };
	char wonsoName[5] = { 'O', 'C', 'H', 'S', 'N' };

	double wonso = 0;

	for (int k = 0; k < 5; k++) {
		if (wonsoName[k] == alpha)
			wonso = wonsoNum[k];
	}

	return wonso;
}