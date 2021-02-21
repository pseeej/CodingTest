#pragma warning(disable:4996)
#include <iostream>
#include <queue>
using namespace std;

int main() {

	queue<int> q;

	int N, K;
	cin >> N >> K;

	for (int i = 1; i <= N; i++)
		q.push(i);

	cout << "<";

	int cnt = 1;
	while (!q.empty()) {
		if (cnt != K) {
			q.push(q.front());
			q.pop();
			cnt++;
		}
		else {	//cnt==K
			cout << q.front();
			q.pop();
			if (!q.empty())
				cout << ", ";
			cnt = 1;
		}
	}

	cout << ">";



	return 0;
}