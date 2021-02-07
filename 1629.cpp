#pragma warning(disable:4996)
#include <iostream>
using namespace std;

long long a, b, c;

long long pow(long long a, long long b) {
	if (b == 0)
		return 1;

	long long temp = pow(a, b / 2);

	if (b % 2)	// b°¡ È¦¼öÀÏ ¶§ (A^(B/2))*A
		return ((temp * temp) % c) * a % c;
	else    // b°¡ Â¦¼öÀÏ ¶§ (A^(B/2))*(A^(B/2))
		return (temp * temp) % c;
	
}

int main() {

	cin >> a >> b >> c;

	cout << pow(a, b);


	return 0;
}