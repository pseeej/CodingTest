#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int resArr[21][21][21];

void calc() {

	for (int i = 0; i < 21; i++) {
		for (int j = 0; j < 21; j++) {
			for (int k = 0; k < 21; k++) {
				if (i == 0 || j == 0 || k == 0)
					resArr[i][j][k] = 1;
				else if (i < j && j < k)
					resArr[i][j][k] = resArr[i][j][k - 1] + resArr[i][j - 1][k - 1] - resArr[i][j - 1][k];
				else
					resArr[i][j][k] = resArr[i - 1][j][k] + resArr[i - 1][j - 1][k] + resArr[i - 1][j][k - 1] - resArr[i - 1][j - 1][k - 1];
			}
		}
	}

}


int main() {

	calc();

	while (1) {
		int a, b, c;
		cin >> a >> b >> c;
		if (a == -1 && b == -1 && c == -1)
			break;
		cout << "w(" << a << ", " << b << ", " << c << ") = ";
		if (a <= 0 || b <= 0 || c <= 0)
			cout << "1\n";
		else if (a > 20 || b > 20 || c > 20)
			cout << resArr[20][20][20] << "\n";
		else
			cout << resArr[a][b][c] << "\n";
	}

	return 0;
}