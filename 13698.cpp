#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

void swap(int* a, int* b) {
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

int main() {

	// 작은 공 1 큰 공 2
	int arr[4] = { 1, 0, 0, 2 };

	string str;
	cin >> str;

	for (int i = 0; i < str.length(); i++) {
		switch (str[i]) {
		case 'A':
			swap(arr[0], arr[1]);
			break;
		case 'B':
			swap(arr[0], arr[2]);
			break;
		case 'C':
			swap(arr[0], arr[3]);
			break;
		case 'D':
			swap(arr[1], arr[2]);
			break;
		case 'E':
			swap(arr[1], arr[3]);
			break;
		case 'F':
			swap(arr[2], arr[3]);
			break;

		}
	}

	int s, l;

	for (int i = 0; i < 4; i++) {
		if (arr[i] == 1)
			s = i+1;
		if (arr[i] == 2)
			l = i+1;
	}

	cout << s << "\n" << l;

	return 0;
}