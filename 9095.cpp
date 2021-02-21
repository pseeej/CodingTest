#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	// 결과 배열 초기화
	int arr[12] = { 0, };
	arr[1] = 1;
	arr[2] = 2;
	arr[3] = 4;

	for (int i = 4; i <= 11; i++) {
		arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1];
	}

	int T;
	cin >> T;

	while (T--) {
		int num;
		cin >> num;
		
		cout << arr[num] << "\n";
	}


	return 0;
}