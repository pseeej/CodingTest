#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	int** rgb = new int*[N];
	int** calc = new int*[N];
	for (int i = 0; i < N; i++) {
		rgb[i] = new int[3];
		calc[i] = new int[3];
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> rgb[i][j];
		}
	}

	calc[0][0] = rgb[0][0];
	calc[0][1] = rgb[0][1];
	calc[0][2] = rgb[0][2];

	for (int i = 1; i < N; i++) {
		calc[i][0] = min(calc[i - 1][1], calc[i - 1][2]) + rgb[i][0];
		calc[i][1] = min(calc[i - 1][0], calc[i - 1][2]) + rgb[i][1];
		calc[i][2] = min(calc[i - 1][0], calc[i - 1][1]) + rgb[i][2];
	}

	int minimum = min(calc[N - 1][0], calc[N - 1][1]);
	minimum = min(minimum, calc[N - 1][2]);
	cout << minimum;


	for (int i = 0; i < N; i++) {
		delete[] rgb[i];
		delete[] calc[i];
	}
	delete[] rgb;
	delete[] calc;

	return 0;
}