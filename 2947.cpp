#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int arr[5];

void print() {
	for (int i = 0; i < 5; i++)
		cout << arr[i] << " ";
	cout << "\n";
}

int check() {
	int res[5] = { 1, 2, 3, 4, 5 };
	for (int i = 0; i < 5; i++) {
		if (arr[i] != res[i])
			return 0;
	}
	return 1;
}

int main() {

	for (int i = 0; i < 5; i++)
		cin >> arr[i];

	while (1) {
		for (int i = 0; i < 4; i++) {
			if (arr[i] > arr[i + 1]) {
				int temp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = temp;
				print();
			}
			else;
		}
		if (check())
			break;
	}



	return 0;
}