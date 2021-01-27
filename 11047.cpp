#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int N, K;
	cin >> N >> K;

	int* coins = new int[N];
	for (int i = 0; i < N; i++)
		cin >> coins[i];

	int cnt = 0;

	for (int i = N - 1; i >= 0; i--) {
		int tmp = 0;
		if (K >= coins[i]) {
			 tmp += (K / coins[i]);
			 cnt += tmp;
			 K -= coins[i] * tmp;
		}
		if (K == 0)
			break;
	}

	cout << cnt;

	return 0;
}