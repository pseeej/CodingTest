#pragma warning(disable:4996)
#include <iostream>
#include <cmath>
using namespace std;

int main() {

	int N;
	cin >> N;

	if (N % 2 == 0)
		cout << pow((N / 2) + 1, 2);
	else
		cout << pow((N / 2) + 1, 2) + (N / 2) + 1;

	return 0;
}