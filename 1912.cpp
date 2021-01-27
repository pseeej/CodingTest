#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int max(int a, int b) {
	return (a > b) ? a : b;
}

int main() {

	int N;
	cin >> N;

	int* nums = new int[N];
	int* sums = new int[N];
	for (int i = 0; i < N; i++)
		cin >> nums[i];

	sums[0] = nums[0];
	for (int i = 1; i < N; i++) {
		int temp = sums[i - 1] + nums[i];
		if (temp > nums[i])
			sums[i] = temp;
		else
			sums[i] = nums[i];
	}

	int maxnum = -8888444;
	for (int i = 0; i < N; i++) {
		maxnum = max(maxnum, sums[i]);
	//	cout << sums[i] << " ";
	}

	cout << maxnum;

	return 0;
}