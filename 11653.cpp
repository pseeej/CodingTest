#define _CRT_SERCURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main() {

	int num;
	cin >> num;

	int div = 2;

	while (num != 1) {
		if (num % div == 0) {
			cout << div << "\n";
			num /= div;
			div = 2;
		}
		else {
			div++;
		}
	}


	return 0;
}