#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[N];
	int* dp = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		dp[i] = 0;
	}

	sort(arr, arr + N);

	int max = 0;

	for (int i = 0; i < N; i++) {
		dp[i] = arr[i] * (N - i);
		if (max < dp[i])
			max = dp[i];
	}

	cout << max;

	delete[] arr;

	return 0;
}