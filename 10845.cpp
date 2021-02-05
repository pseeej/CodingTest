#pragma warning(disable:4996)
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {

	int N;
	cin >> N;

	queue<int> q;
	string str;
	int num;

	for (int i = 0; i < N; i++) {
		cin >> str;
		if (str == "push") {
			cin >> num;
			q.push(num);
		}
		if (str == "pop") {
			if (q.empty())
				cout << "-1\n";
			else {
				cout << q.front() << "\n";
				q.pop();
			}
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