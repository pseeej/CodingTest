#pragma warning(disable:4996)
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {

	string a, b;
	cin >> a >> b;

	a = '0' + a;
	b = '0' + b;

	int** lcs = new int* [a.size()];
	for (int i = 0; i < a.size(); i++)
		lcs[i] = new int[b.size()];

	for (int i = 0; i < a.size(); i++) {
		for (int j = 0; j < b.size(); j++) {
			if (i == 0 || j == 0) {
				lcs[i][j] = 0;
				continue;
			}
			if (a[i] == b[j])
				lcs[i][j] = lcs[i - 1][j - 1] + 1;
			else
				lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
		}
	}

	cout << lcs[a.size() - 1][b.size() - 1];

	for (int i = 0; i < a.size(); i++)
		delete lcs[i];
	delete[] lcs;

	return 0;
}