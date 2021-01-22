#define _CRT_NO_SECURE_WARNINGS
#include <iostream>
using namespace std;

int arr[41] = { 0, 1, };

int fibonacci(int n) {
	if (n == 0 || n == 1)
		return arr[n];
	else if (arr[n] == 0)
		arr[n] = fibonacci(n - 1) + fibonacci(n - 2);
	return arr[n];
}

int main() {

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if (num == 0)
			cout << "1 0\n";
		else {
			cout << fibonacci(num-1) << " " << fibonacci(num) << "\n";
		}
	}


	return 0;

}