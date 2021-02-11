#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;
	int** arr = new int* [N];
	for (int i = 0; i < N; i++)
		arr[i] = new int[M];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
		}
	}

	int K;
	cin >> K;
	for (int i = 0; i < K; i++) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		int sum = 0;
		for (int j = a - 1; j < c; j++) {
			for (int k = b - 1; k < d; k++) {
				sum += arr[j][k];
			}
		}
		cout << sum << "\n";
	}


	return 0;
}