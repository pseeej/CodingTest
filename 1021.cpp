#pragma warning(disable:4996)
#include <iostream>
#include <queue>
using namespace std;

int main() {
	
	int N, M;
	cin >> N >> M;

	int num;

	deque<int> dq;
	for (int i = 1; i <= N; i++)
		dq.push_back(i);

	int cnt = 0;

	for (int i = 0; i < M; i++) {

		cin >> num;
		int index = 0;
		for (int j = 0; j < dq.size(); j++) {
			if (dq[j] == num) {
				index = j;
				break;
			}
		}
		if (index < dq.size() - index) {
			while (1) {
				if (dq.front() == num) {
					dq.pop_front();
					break;
				}
				else {
					cnt++;
					dq.push_back(dq.front());
					dq.pop_front();
				}
			}
		}
		else {
			while (1) {
				if (dq.front() == num) {
					dq.pop_front();
					break;
				}
				else {
					cnt++;
					dq.push_front(dq.back());
					dq.pop_back();
				}
			}
		}
	}

	cout << cnt;
		



	return 0;
}