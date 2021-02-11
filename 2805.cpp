#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int N;
	ll M;
	ll* trees;

	cin >> N >> M;

	trees = new ll[N];
	ll high = 0;
	for (int i = 0; i < N; i++) {
		cin >> trees[i];
		high = max(high, trees[i]);
	}

	ll res = 0;
	ll low = 1;

	while (low<=high) {
		ll mid = (low + high) / 2;
		ll tot = 0;
		
		for (int i = 0; i < N; i++) {
			if (mid < trees[i])
				tot += trees[i] - mid;
		}
		if (tot >= M) {
			if (res < mid)
				res = mid;
			low = mid + 1;
		}
		else
			high = mid - 1;
	}

	cout << res;

	return 0;
}