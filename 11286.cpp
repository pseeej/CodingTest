#pragma warning(disable:4996)
#include <iostream>
#include <queue>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	priority_queue<int, vector<int>, greater<int>> pq;
	priority_queue<int> mq;

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		if (temp == 0) {
			if (pq.empty() && mq.empty())
				cout << "0\n";
			else {
				if (pq.empty()) {
					cout << mq.top() << "\n";
					mq.pop();
				}
				else if (mq.empty()) {
					cout << pq.top() << "\n";
					pq.pop();
				}
				else {
					if (pq.top() < (mq.top()*-1)) {
						cout << pq.top() << "\n";
						pq.pop();
					}
					else {
						cout << mq.top() << "\n";
						mq.pop();
					}
				}
			}
		}
		else {
			if (temp > 0)
				pq.push(temp);
			else
				mq.push(temp);
		}
	}



	return 0;
}