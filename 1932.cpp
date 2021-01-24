#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int N;
	cin >> N;

	int** board = new int* [N];
	int** sum = new int* [N];
	for (int i = 0; i < N; i++) {
		board[i] = new int[N];
		sum[i] = new int[N];
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			sum[i][j] = 0;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j <= i; j++) {
			cin >> board[i][j];
		}
	}

	sum[0][0] = board[0][0];
	for (int i = 1; i <= N-1; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0)
				sum[i][j] = sum[i - 1][j] + board[i][j];
			else if (j == i)
				sum[i][j] = sum[i - 1][j - 1] + board[i][j];
			else
				sum[i][j] = max(sum[i - 1][j - 1], sum[i - 1][j]) + board[i][j];
		}
	}

	int max = -30;

	for (int i = 0; i < N; i++)
		if (sum[N-1][i] > max)
			max = sum[N-1][i];
	cout << max;

	for (int i = 0; i < N; i++)
		delete board[i];
	delete[] board;

	return 0;
}