#pragma warning(disable:4996)
#include <iostream>
#include <queue>
using namespace std;

int main() {

	int N;
	cin >> N;

	queue<int> q;
	for (int i = 1; i <= N; i++) {
		q.push(i);
	}
	
	int i = q.front();
	while (q.size()!=1) {
		q.pop();
		i = q.front();
		if (q.size() == 1)
			break;
		else {
			q.pop();
			q.push(i);
		}
	}

	cout << i;


	return 0;
}