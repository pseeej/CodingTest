#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* input_arr = new int[N];
	int* dp = new int[N];

	for (int i = 0; i < N; i++) {
		cin >> input_arr[i];
		dp[i] = 1;
	}

	for (int i = 0; i < N; i++) {
		int last = input_arr[i];
		for (int j = 0; j < i; j++) {
			int target = input_arr[j];
			if (last > target) {
				dp[i] = max(dp[i], dp[j] + 1);
			}
		}
	}

	int ans = 0;
	for (int i = 0; i < N; i++)
		ans = max(ans, dp[i]);

	cout << ans;

	delete[] input_arr;
	delete[] dp;

	return 0;
}