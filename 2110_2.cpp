#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) {
	if (a.second > b.second)
		return true;
	return false;
}

int main() {

	int N, C;
	cin >> N >> C;
	
	vector<int> v;
	for (int i = 0; i < N; i++) {
		int n;
		cin >> n;
		v.push_back(n);
	}

	sort(v.begin(), v.end());

	vector<pair<int, int>> dist;
	for (int i = 0; i < N - 1; i++)
		dist.push_back(make_pair(i, v[i + 1] - v[i]));

	sort(dist.begin(), dist.end(), cmp);


	return 0;
}
