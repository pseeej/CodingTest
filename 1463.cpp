#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int min(int a, int b) {
	return (a < b) ? a : b;
}

int main() {

	int N;
	cin >> N;

	int* cnts = new int[N + 1];
	cnts[N] = 0;
	for (int i = 0; i < N; i++)
		cnts[i] = 999999;

	for (int i = N; i > 0; i--) {
		int tmp;
		if (i % 3 == 0) {
			tmp = i / 3;
			cnts[tmp] = min(cnts[i] + 1, cnts[tmp]);
		}
		if (i % 2 == 0) {
			tmp = i / 2;
			cnts[tmp] = min(cnts[i] + 1, cnts[tmp]);
		}
		tmp = i - 1;
		cnts[tmp] = min(cnts[i] + 1, cnts[tmp]);
	}

	cout << cnts[1];

	return 0;
}