#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;
	int* arr = new int[N];
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	sort(arr, arr + N);

	int temp = 0;
	int res = 0;
	for (int i = 0; i < N; i++) {
		temp += arr[i];
		res += temp;
	}

	cout << res;


	return 0;
}