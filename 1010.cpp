#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;

		int res = 1;
		for (int i = 0; i < a; i++) {
			res *= (b - i);
			res /= (i + 1);
		}

		cout << res << "\n";
	}



	return 0;
}