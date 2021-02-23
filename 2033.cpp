#pragma warning(disable:4996)
#include <iostream>
#include <cmath>
using namespace std;

int main() {


	int N;
	cin >> N;

	int index = 1;

	while (1) {
		int power = pow(10, index);
		if (N > power) {
			int temp = N;
			temp = temp % power;
			if (temp >= power / 2) {
				N = N - temp + power;
			}
			else {
				N -= temp;
			}
			index++;
		}
		else
			break;
	}

	cout << N;

	return 0;
}