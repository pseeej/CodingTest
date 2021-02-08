#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int res[100][100] = { 0, };

int main() {

	int N, M;
	cin >> N >> M;

	int** arrA = new int*[N];
	for (int i = 0; i < N; i++)
		arrA[i] = new int[M];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arrA[i][j];
		}
	}
	
	int temp, K;
	cin >> temp >> K;

	int** arrB = new int* [M];
	for (int i = 0; i < M; i++)
		arrB[i] = new int[K];

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < K; j++) {
			cin >> arrB[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			for (int k = 0; k < K; k++) {
				res[i][k] += (arrA[i][j] * arrB[j][k]);
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < K; j++) {
			cout << res[i][j] << " ";
		}
		cout << "\n";
	}

	for (int i = 0; i < N; i++)
		delete arrA[i];
	delete[] arrA;
	for (int i = 0; i < M; i++)
		delete arrB[i];
	delete[] arrB;
	

	return 0;
}