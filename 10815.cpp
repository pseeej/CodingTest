#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);	// 시간 초과 처리 위함

	int N;
	cin >> N;

	int* arr = new int[N];
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	sort(arr, arr + N);

	int M;
	cin >> M;

	for (int i = 0; i < M; i++) {
		int num;
		cin >> num;

		// num보다 큰 숫자가 처음으로 나오는 위치 - num 이상의 숫자가 처음으로 나오는 위치
		if (upper_bound(arr, arr + N, num) - lower_bound(arr, arr + N, num))
			cout << "1 ";
		else
			cout << "0 ";
	}


	return 0;
}