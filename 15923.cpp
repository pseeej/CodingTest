#pragma warning(disable:4996)
#include <iostream>
#include <cmath>
using namespace std;

int main() {

	int N;
	cin >> N;

	double sum = 0;

	int firstx, firsty;
	int oldx, oldy;
	cin >> firstx >>  firsty;
	oldx = firstx;
	oldy = firsty;

	int newx, newy;

	while (--N) {
		cin >> newx >> newy;
		sum += sqrt(pow(newx - oldx, 2) + pow(newy - oldy, 2));

		oldx = newx;
		oldy = newy;
	}

	sum += sqrt(pow(firstx - oldx, 2) + pow(firsty - oldy, 2));

	cout << sum;


	return 0;
}