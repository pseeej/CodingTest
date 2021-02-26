#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int E, S, M;
	cin >> E >> S >> M;

	int res = 1;

	while (1) {
		if ((res - E) % 15 == 0 && (res - S) % 28 == 0 && (res - M) % 19 == 0)
			break;
		else
			res++;
	}

	cout << res;

	return 0;
}