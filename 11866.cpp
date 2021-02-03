#pragma warning(disable:4996)
#include <iostream>
#include <queue>
using namespace std;

int main() {

	int N;
	cin >> N;
	int K;
	cin >> K;

	deque<int> q;

	for (int i = 1; i <= N; i++)
		q.push_back(i);

	int temp;
	cout << "<";

	while (!q.empty()) {
		for (int i = 0; i < K; i++) {
			temp = q.front();
			q.pop_front();
			q.push_back(temp);
		}
		cout << q.back();
		q.pop_back();
		if (q.empty())
			cout << ">";
		else
			cout << ", ";
	}


	return 0;
}