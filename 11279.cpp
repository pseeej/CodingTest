#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	priority_queue<int> pq;

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		if (temp == 0) {
			if (pq.empty())
				cout << "0\n";
			else {
				cout << pq.top() << "\n";
				pq.pop();
			}
		}
		else
			pq.push(temp);
	}



	return 0;
}
