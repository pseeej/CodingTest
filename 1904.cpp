#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int N;
	cin >> N;
	int* arr = new int[N+1];

	arr[0] = 1;
	arr[1] = 2;

	for (int i = 2; i < N; i++) {
		arr[i] = (arr[i - 1] + arr[i - 2])%15746;
	}

	cout << arr[N-1];

	delete[] arr;

	return 0;
}