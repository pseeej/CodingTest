#pragma warning(disable:4996)
#include <iostream>
#include <cmath>
using namespace std;

long long min(long long a, long long b) {
	return (a < b) ? a : b;
}

int main() {

	long long a, b;
	cin >> a >> b;

	long long cnt2 = 0;
	long long cnt5 = 0;

	for (long long i = 2; i <= a; i *= 2)
		cnt2 += a / i;
	for (long long i = 2; i <= a - b; i *= 2)
		cnt2 -= (a - b) / i;
	for (long long i = 2; i <= b; i *= 2)
		cnt2 -= b / i;

	for (long long i = 5; i <= a; i *= 5)
		cnt5 += a / i;
	for (long long i = 5; i <= (a - b); i *= 5)
		cnt5 -= (a - b) / i;
	for (long long i = 5; i <= b; i *= 5)
		cnt5 -= b / i;


	cout << min(cnt2, cnt5);

	return 0;
}