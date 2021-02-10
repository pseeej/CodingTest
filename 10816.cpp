#pragma warning(disable:4996)
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);	// 시간 초과 처리 위함

	int N;
	cin >> N;

	vector<int> v(N);	// v의 최대 크기 지정
	for (int i = 0; i < N; i++)
		cin >> v[i];

	sort(v.begin(), v.end());
	int M;
	cin >> M;

	for (int i = 0; i < M; i++) {
		int num;
		cin >> num;

		// num보다 큰 숫자가 처음으로 나오는 위치 - num 이상의 숫자가 처음으로 나오는 위치
		cout << upper_bound(v.begin(), v.end(), num) - lower_bound(v.begin(), v.end(), num) << " ";
	}


	return 0;
}