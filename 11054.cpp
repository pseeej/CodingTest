#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[N];
	int* dp = new int[N];
	int* dp2 = new int[N];

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	for (int i = 0; i < N; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (arr[i] > arr[j]) {
				if (dp[i] < dp[j] + 1)
					dp[i] = dp[j] + 1;
			}
		}
	}

	for (int i = N - 1; i >= 0; i--) {
		dp2[i] = 1;
		for (int j = N - 1; j > i; j--) {
			if (arr[i] > arr[j]) {
				if (dp2[i] < dp2[j] + 1)
					dp2[i] = dp2[j] + 1;
			}
		}
	}

	int ans = 0;
	for (int i = 0; i < N; i++)
		ans = max(ans, dp[i] + dp2[i]);

	cout << ans-1;

	delete[] arr;
	delete[] dp;
	delete[] dp2;


	return 0;
}