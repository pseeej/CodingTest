#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int mod = 1000000000;

	int N;
	cin >> N;

	long** arr = new long*[101];
	for (int i = 0; i < 101; i++)
		arr[i] = new long[11];

	arr[1][0] = 0;
	for (int i = 1; i <= 9; i++)
		arr[1][i] = 1;

	for (int i = 2; i <= N; i++) {
		arr[i][0] = arr[i - 1][1] % mod;
		for (int j = 1; j <= 8; j++) {
			arr[i][j] = (arr[i - 1][j - 1] + arr[i - 1][j + 1]) % mod;
		}
		arr[i][9] = arr[i - 1][8] % mod;
	}

	long sum = 0;
	for (int i = 0; i < 10; i++)
		sum += (arr[N][i] % mod);

	sum %= mod;
	cout << sum;

	for (int i = 0; i < 101; i++)
		delete arr[i];
	delete[] arr;

	return 0;
}