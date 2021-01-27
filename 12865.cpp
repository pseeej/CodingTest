#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N, K;
	cin >> N >> K;

	int* W = new int[N+1];
	int* V = new int[N+1];
	int** dp = new int* [N + 1];
	for (int i = 0; i < N+1; i++) {
		dp[i] = new int[K+1];
	}

	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= K; j++)
			dp[i][j] = 0;
	}

	for (int i = 1; i <= N; i++)
		cin >> W[i] >> V[i];

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= K; j++) {
			if (j - W[i] >= 0)
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i]);
			else
				dp[i][j] = dp[i - 1][j];
		}
	}

	cout << dp[N][K];

	delete[] W;
	delete[] V;


	return 0;
}