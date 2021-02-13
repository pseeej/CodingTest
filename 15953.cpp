#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int first(int place) {
	if (place == 1)
		return 5000000;
	if (1 < place && place <= 3)
		return 3000000;
	if (3 < place && place <= 6)
		return 2000000;
	if (6 < place && place <= 10)
		return 500000;
	if (10 < place && place <= 15)
		return 300000;
	if (15 < place && place <= 21)
		return 100000;

	return 0;
}

int second(int place) {
	if (place == 1)
		return 5120000;
	if (1 < place && place <= 3)
		return 2560000;
	if (3 < place && place <= 7)
		return 1280000;
	if (7 < place && place <= 15)
		return 640000;
	if (15 < place && place <= 31)
		return 320000;

	return 0;
}

int main() {

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;
		cout << first(a)+second(b) << "\n";
	}



	return 0;
}