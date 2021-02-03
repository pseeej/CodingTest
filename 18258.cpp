#pragma warning(disable:4996)
#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {

	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int N;
	cin >> N;
	string str;
	queue<int> q;
	int num;


	for (int i = 0; i < N; i++) {
		cin >> str;
		if (str == "push") {
			cin >> num;
			q.push(num);
		}
		if (str == "pop") {
			if (q.empty()) {
				cout << "-1\n";
				continue;
			}
			cout << q.front() << "\n";
			q.pop();
		}
		if (str == "size")
			cout << q.size() << "\n";
		if (str == "empty")
			cout << q.empty() << "\n";
		if (str == "front") {
			if (q.empty())
				cout << "-1\n";
			else
				cout << q.front() << "\n";
		}
		if (str == "back") {
			if (q.empty())
				cout << "-1\n";
			else
				cout << q.back() << "\n";
		}
	}



	return 0;
}