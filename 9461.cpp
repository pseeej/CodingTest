#pragma warning(disable:4996)
#include <iostream>
using namespace std;

long long arr[101] = { 1, 1, 1, };

void init() {
	for (int i = 3; i <= 100; i++) {
		arr[i] = arr[i - 2] + arr[i - 3];
	}
}

int main() {

	int T;
	cin >> T;
	init();
	for (int i = 0; i < T; i++) {
		int nth;
		cin >> nth;
		cout << arr[nth-1] << "\n";
	}


	return 0;
}