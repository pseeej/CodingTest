#pragma warning(disable:4996)
#include <iostream>
#include <queue>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	priority_queue<int> maxpq;
	priority_queue<int, vector<int>, greater<int>> minpq;

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;

		// maxpq의 size는 min의 size보다 같거나 커야함
		if (maxpq.size() == minpq.size())
			maxpq.push(temp);
		else    // 개수 맞춰주기 위함
			minpq.push(temp);

		// min에 있는 값이 max보다 더 작으면
		// 서로 top에 있는 값 swap함
		if (!minpq.empty() && !maxpq.empty() && minpq.top() < maxpq.top()) {
			int a = maxpq.top();
			int b = minpq.top();

			maxpq.pop();
			minpq.pop();
			maxpq.push(b);
			minpq.push(a);
		}

		// 이게 가운데값이 됨
		cout << maxpq.top() << "\n";
	}



	return 0;
}