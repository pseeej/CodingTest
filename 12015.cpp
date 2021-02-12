#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;

	vector <int> v;
	v.push_back(0);

	int cnt = 0;

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		if (temp > v.back()) {
			v.push_back(temp);
			cnt++;
		}
		else {
			auto iter = lower_bound(v.begin(), v.end(), temp);
			*iter = temp;
		}
	}

	cout << cnt;


	return 0;
}