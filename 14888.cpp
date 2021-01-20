#define _CRT_NO_SECURE_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findMin(int a, int b) {
	if (a > b)
		return b;
	else
		return a;
}

int findMax(int a, int b) {
	if (a > b)
		return a;
	else
		return b;
}

int main() {

	int N;
	cin >> N;

	int nums[11] = { 0, };
	for (int i = 0; i < N; i++)
		cin >> nums[i];

	int temp;
	vector<int> op;
	for (int i = 0; i < 4; i++) {
		cin >> temp;
		for (int j = 0; j < temp; j++) {
			op.push_back(i);
		}
	}

	int min = 1000000000;
	int max = -100000000;

	// 이 때 next_permutation은 순열 구하는 거
	while (next_permutation(op.begin(), op.end())) {
		int res = nums[0];
		for (int i = 0; i < N - 1; i++) {
			if (op[i] == 0)
				res += nums[i + 1];
			else if (op[i] == 1)
				res -= nums[i + 1];
			else if (op[i] == 2)
				res *= nums[i + 1];
			else if (op[i] == 3)
				res /= nums[i + 1];
		}
		min = findMin(min, res);
		max = findMax(max, res);
	};

	cout << max << "\n" << min;


	return 0;
}