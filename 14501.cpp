#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int delays[17] = { 0, };
	int prices[17] = { 0, };

	int N;
	cin >> N;

	for (int i = 1; i <= N; i++) {
		cin >> delays[i] >> prices[i];
	}

	int dp[17] = { 0, };

	int res = -1;
	
	for (int i = 1; i <= N+1; i++) {
		for (int j = 1; j < i; j++) {
			dp[i] = max(dp[i], dp[j]);

			if (j + delays[j] == i)
				dp[i] = max(dp[i], dp[j] + prices[j]);
		}
		res = max(res, dp[i]);
	}

	cout << res;

	return 0;
}