#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;
	
	int* wine = new int[N];
	for (int i = 0; i < N; i++)
		cin >> wine[i];

	int* res = new int[N];

	res[0] = wine[0];
	res[1] = res[0] + wine[1];

	for (int i = 2; i < N; i++) {
		int resa = res[i - 3] + wine[i - 1] + wine[i];
		int resb = res[i - 2] + wine[i];
		res[i] = max(resa, resb);
		res[i] = max(res[i], res[i - 1]);
	}

	cout << res[N - 1];

	delete[] wine;
	delete[] res;

	return 0;
}