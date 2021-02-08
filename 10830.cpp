#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int N, B;
long long c[6][6];
long long arr[6][6];
long long res[6][6];

void zegob(long long arr[6][6], long long b[6][6]) {
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			c[i][j] = 0;
			for (int k = 0; k < N; k++) {
				c[i][j] += arr[i][k] * b[k][j];
			}
			c[i][j] %= 1000;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			arr[i][j] = c[i][j];
		}
	}

}

int main() {

	cin >> N >> B;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
		}
		res[i][i] = 1;
	}

	while (B > 0) {
		if (B % 2 == 1) {	//지수가 홀수면
			zegob(res, arr);
		}
		zegob(arr, arr);
		B /= 2;
	}
	

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << res[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}