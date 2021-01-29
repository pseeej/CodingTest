#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;
	else
		return gcd(b, a % b);
}

int lcm(int a, int b) {
	return (a * b) / gcd(a, b);
}

int max(int a, int b) {
	return (a > b) ? a : b;
}

int min(int a, int b) {
	return (a < b) ? a : b;
}

int main() {

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;
		cout << lcm(max(a, b), min(a, b)) << "\n";
	}


	return 0;
}