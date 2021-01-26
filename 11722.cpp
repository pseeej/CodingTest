#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[N];
	int* dp = new int[N];

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	for (int i = N - 1; i >= 0; i--) {
		dp[i] = 1;
		for (int j = N - 1; j > i; j--) {
			if (arr[i] > arr[j]) {
				if (dp[j] + 1 > dp[i])
					dp[i] = dp[j] + 1;
			}
		}
	}

	int ans = 0;
	for (int i = 0; i < N; i++)
		ans = max(ans, dp[i]);

	cout << ans;

	delete[] arr;
	delete[] dp;


	return 0;
}