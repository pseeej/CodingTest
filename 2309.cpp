#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int sum = 0;
	int* arr = new int[9];
	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i < 9; i++)
		sum += arr[i];

	sort(arr, arr + 9);


	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (sum - (arr[i] + arr[j]) == 100) {
				for (int k = 0; k < 9; k++) {
					if (k == i || k == j)
						continue;
					cout << arr[k] << "\n";
				}
				return 0;
			}
		}
	}


	delete[] arr;

	return 0;
}