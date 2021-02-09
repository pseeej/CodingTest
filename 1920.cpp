#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

void bin_search(int* arr, int first, int last, int find) {

	int pivot = (first+last)/2;

	if (first > last) {
		cout << "0\n";
		return;
	}
	else {
		if (find == arr[pivot]) {
			cout << "1\n";
			return;
		}

		if (find > arr[pivot])
			return bin_search(arr, pivot + 1, last, find);
		if (find < arr[pivot])
			return bin_search(arr, first, pivot - 1, find);
	}

}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;

	int* arr = new int[N];

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	sort(arr, arr + N);

	int M;
	cin >> M;

	for (int i = 0; i < M; i++) {
		int num;
		cin >> num;

		//cout << binary_search(arr, arr + N, num) << "\n";

		bin_search(arr, 0, N, num);
	}


	delete[] arr;

	return 0;
}