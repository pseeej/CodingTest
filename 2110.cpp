#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int N, C;
int* home;

bool possible(int dist) {
	int cnt = 1;
	int prev = home[0];

	for (int i = 1; i < N; i++) {
		if (home[i] - prev = dist) {
			cnt++;
			prev = home[i];
		}
	}
	if (cnt >= C)
		return true;
	else
		return false;
}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> C;

	home = new int[N];

	for (int i = 0; i < N; i++)
		cin >> home[i];
	
	sort(home, home + N);

	int low = 1;
	int high = home[N - 1] - home[0];
	int res = 0;

	while (low <= high) {
		int mid = (low + high) / 2;
		if (possible(mid)) {
			res = max(res, mid);
			low = mid + 1;
		}
		else
			high = mid - 1;
	}

	cout << res;

	return 0;
}