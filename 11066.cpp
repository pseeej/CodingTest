#pragma warning(disable:4996)
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int dp[501][501];
int arr[501];
int sum[501];
int t, k, i;

int func_dp(int x, int y) {
	if (dp[x][y] != 0x3f3f3f3f)
		return dp[x][y];

	if (x == y)
		return dp[x][y] = 0;
	
	if (x + 1 == y)
		return dp[x][y] = arr[x] + arr[y];

	for (int mid = x; mid < y; mid++) {
		int left = func_dp(x, mid);
		int right = func_dp(mid + 1, y);
		dp[x][y] = min(dp[x][y], left + right);
	}

	return dp[x][y] += sum[y] - sum[x - 1];
}

int main() {

	cin >> t;
	while (t--) {
		memset(dp, 0x3f, sizeof(dp));
		cin >> k;
		for (i = 1; i <= k; i++) {
			cin >> arr[i];
			sum[i] = sum[i - 1] + arr[i];
		}
		cout << func_dp(1, k) << "\n";
	}

	return 0;
}