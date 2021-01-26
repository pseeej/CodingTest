#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int max(int a, int b) {
	return (a > b) ? a : b;
}

int min(int a, int b) {
	return (a < b) ? a : b;
}

int main() {

	int N;
	cin >> N;

	int arr[501] = { 0, };
	int dp[501] = { 0, };
	int index;

	int maxIdx = -1;
	int minIdx = 99999;

	for (int i = 0; i < N; i++) {
		cin >> index;
		maxIdx = max(maxIdx, index);
		minIdx = min(minIdx, index);
		cin >> arr[index];
	}


	for (int i = minIdx; i <= maxIdx; i++) {
		if (arr[i] != 0)
			dp[i] = 1;
		for (int j = minIdx; j < i; j++) {
			if (arr[i] > arr[j]) {
				if (dp[i] < dp[j] + 1)
					dp[i] = dp[j] + 1;
			}
		}
	}

	int ans = 0;
	for (int i = minIdx; i <= maxIdx; i++)
		ans = max(ans, dp[i]);
	cout << N - ans;


	return 0;
}