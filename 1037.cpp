#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int n;
	cin >> n;

	int arr[50] = { 0, };
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	sort(arr, arr + n);

	int res = 1;
	if (n % 2 == 0) {
		res = arr[n / 2] * arr[(n / 2) -1];
	}
	else {
		res = arr[n / 2] * arr[n / 2];
	}

	cout << res;


	return 0;
}