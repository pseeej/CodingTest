#pragma warning(disable:4996)
#include <iostream>
#include <stack>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<pair<int, int>> v;
map<pair<int, int>, int> m;

typedef long long ll;

ll getDist(pair<int, int> a, pair<int, int> b) {
	int x1 = a.first;
	int y1 = a.second;
	int x2 = b.first;
	int y2 = b.second;

	return pow((x1 - x2), 2) + pow((y1 - y2), 2);
}

int main() {

	int max = 100000;

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		v.push_back({ x, y });
	}
	
	// x축 정렬 통해 x의 축 차이만으로 최대값 후보에서 여러 점들 제외 가능
	sort(v.begin(), v.end());

	// map에 남아있는 점들 중에서 y축으로 lower_bound, upper_bound 하기 위함
	// 첫 번째 점과 두 번째 점 사이의 거리를 기준으로 잡음.
	m[{v[0].second, v[0].first}] = 0;
	m[{v[1].second, v[1].first}] = 0;
	ll ans = getDist(v[0], v[1]);

	int pos = 0;
	for (int i = 2; i < n; i++) {
		while (pos < i) {
			// x축간의 거리 차이
			int dx = v[i].first - v[pos].first;

			// pos랑 i번째 점 x축 사이의 거리가 더 작으면
			// pos점은 가장 작은 간격을 구할 때 필요로 한 것 확인 가능
			if (dx * dx <= ans)
				break;

			// pos랑 i번째 점 x축 사이의 거리가 더 크면
			// pos점 더 이상 사용 불가.
			m.erase({ v[pos].second, v[pos].first });
			pos++;
		}

		// 실제 거리 계산 위해 sqrt
		ll dis = sqrt(ans);

		// map에 남아 있는 점들 중에서 현재 ans보다 작아질 수 있는 후보 점들 찾기 위해 left, right 구함
		// 이 때 auto는 선언의 초기화 식에서 형식이 추론되는 변수 선언 역할.
		auto left = m.lower_bound({ v[i].second - dis, -max });
		auto right = m.upper_bound({ v[i].second + dis, max });

		// ans 갱신.
		for (auto l = left; l != right; l++) {
			ans = min(ans, getDist({ l->first.second, l->first.first }, v[i]));
		}

		// i번째 점은 당연히 뒤에 확인할 게 있을 거니깐 후보 점이 됨.
		m[{v[i].second, v[i].first}] = 0;
	}

	cout << ans;

	return 0;
}