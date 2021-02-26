#pragma warning(disable:4996)
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {

	string s;
	cin >> s;

	int arr[10] = { 0, };

	for (int i = 0; i < (int)s.length(); i++) {
		arr[s[i] - '0']++;
	}

	int cnt = 0;
	for (int i = 0; i <= 9; i++) {
		if (i != 9 && i != 6)
			cnt = max(cnt, arr[i]);
	}

	cout << max(cnt, (arr[6] + arr[9] + 1) / 2);

	return 0;
}