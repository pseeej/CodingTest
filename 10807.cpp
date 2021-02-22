#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[N];
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	int v;
	cin >> v;

	int cnt = 0;

	for (int i = 0; i < N; i++) {
		if (arr[i] == v)
			cnt++;
	}

	cout << cnt;

	delete[] arr;

	return 0;
}