#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;
int N, K;
ll* base;

bool possible(ll len) {
	int cnt = 0;
	for (int i = 0; i < N; i++)
		cnt += base[i] / len;

	if (cnt >= K)
		return true;
	return false;
}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> K;

	base = new ll[N];
	ll high = 0;
	for (int i = 0; i < N; i++) {
		cin >> base[i];
		high = max(high, base[i]);
	}

	ll result = 0;
	ll low = 1;

	while (low <= high) {
		ll mid = (low + high) / 2;
		if (possible(mid)) {
			if (result < mid)
				result = mid;
			low = mid + 1;
		}
		else
			high = mid - 1;
	}

	cout << result;

	return 0;
}