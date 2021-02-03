#pragma warning(disable:4996)
#include <iostream>
#include <queue>
using namespace std;

int main() {

	int T;
	cin >> T;

	int N, M;
	
	for (int i = 0; i < T; i++) {
		int cnt = 0;
		cin >> N >> M;
		priority_queue<int> pq;
		queue <pair<int, int>> q;

		for (int j = 0; j < N; j++) {
			int temp;
			cin >> temp;
			pq.push(temp);
			q.push({ j, temp });
		}

		while (!q.empty()) {
			int nowIdx = q.front().first;
			int nowPri = q.front().second;
			q.pop();
			if (pq.top() == nowPri) {
				pq.pop();
				cnt++;
				if (nowIdx == M) {
					cout << cnt << "\n";
					break;
				}
			}
			else
				q.push({ nowIdx, nowPri });
		}
	}



	return 0;
}