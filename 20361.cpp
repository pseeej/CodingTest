#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int N, X, K;
	cin >> N >> X >> K;

	int* arr = new int[N+1];
	for (int i = 0; i <= N; i++) {
		arr[i] = 0;
	}
	arr[X] = 1;

	for (int i = 0; i < K; i++) {
		int a, b;
		cin >> a >> b;
		if (arr[a] == 1) {
			arr[b] = 1;
			arr[a] = 0;
		}
		else if (arr[b] == 1) {
			arr[a] = 1;
			arr[b] = 0;
		}
		else;
	}

	for (int i = 0; i <= N; i++)
		if (arr[i] == 1)
			cout << i;

	delete[] arr;

	return 0;
}