#pragma warning(disable:4996)
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {

	int N;
	cin >> N;

	deque<int> dq;
	string str;
	int num;
	
	for (int i = 0; i < N; i++) {
		cin >> str;

		if (str == "push_front") {
			cin >> num;
			dq.push_front(num);
		}
		if (str == "push_back") {
			cin >> num;
			dq.push_back(num);
		}
		if (str == "pop_front") {
			if (dq.empty())
				cout << "-1\n";
			else {
				cout << dq.front() << "\n";
				dq.pop_front();
			}
		}
		if (str == "pop_back") {
			if (dq.empty())
				cout << "-1\n";
			else {
				cout << dq.back() << "\n";
				dq.pop_back();
			}
		}

		if (str == "size")
			cout << dq.size() << "\n";
		if (str == "empty")
			cout << dq.empty() << "\n";
		
		if (str == "front") {
			if (dq.empty())
				cout << "-1\n";
			else
				cout << dq.front() << "\n";
		}

		if (str == "back") {
			if (dq.empty())
				cout << "-1\n";
			else
				cout << dq.back() << "\n";
		}
	}


	return 0;
}