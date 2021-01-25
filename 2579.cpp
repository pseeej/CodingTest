#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[N];
	int* res = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		res[i] = 0;
	}

	res[0] = arr[0];
	res[1] = max(arr[0] + arr[1], arr[1]);
	res[2] = max(arr[0] + arr[2], arr[1]+arr[2]);

	for (int i = 3; i < N; i++) {
		int resa = res[i - 3] + arr[i - 1] + arr[i];
		int resb = res[i - 2] + arr[i];
		res[i] = max(resa, resb);
	}

	cout << res[N - 1];
	
	delete[] arr;
	delete[] res;

	return 0;
}