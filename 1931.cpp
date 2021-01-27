#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {

	int N;
	cin >> N;

	int begin, end;
	vector<pair<int, int>> schedule;

	for (int i = 0; i < N; i++) {
		cin >> begin >> end;
		schedule.push_back(make_pair(end, begin));
	}
	
	//schedule 종료 시점에 대해 정렬
	sort(schedule.begin(), schedule.end());

	int time = schedule[0].first;
	int count = 1;
	for (int i = 1; i < N; i++) {
		// 두 번째 schedule 시작 시점이 종료 시점보다 크거나 같은지 확인
		if (time <= schedule[i].second) {
			count++;
			time = schedule[i].first;
		}
	}

	cout << count;


	return 0;
}