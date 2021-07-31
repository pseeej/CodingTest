#include <iostream>
#include <vector>
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;

	vector<int> v;
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		v.push_back(num);
	}

	int start = 0, end = 0;
	int cnt = 0;
	while (1) {
		int sum = 0;

		// 합 구하기
		for (int i = start; i <= end; i++)
			sum += v[i];

		if (sum == M)
			cnt++;

		// 조건에 end==start 안 하면
		// 두 개 값이 같고 sum>M일 때 start가 end보다 앞으로 가서
		// 반복문 종료됨
		if (sum <= M || end==start)
			end++;	// 연속된 수열의 원소 개수 늘려주기 위함
		else
			start++;	// 수열 개수 줄여주기

		// 종료 조건
		if (end >= N || start > end)
			break;
	}

	cout << cnt;


	return 0;
}
