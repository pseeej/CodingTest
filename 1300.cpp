#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;

ll N, K;

ll getIndex(ll mid) {
	ll cnt = 0;
	for (ll i = 1; i <= N; i++) {
		cnt += min(N, mid / i);
	}
	return cnt;
}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> K;

	ll left = 1;
	ll right = N * N;
	ll ans = 1;

	while (left <= right) {
		ll mid = (left + right) / 2;

		if (getIndex(mid) >= K) {
			ans = mid;
			right = mid - 1;
		}
		else
			left = mid + 1;
	}
	
	cout << ans;
	

	return 0;
}