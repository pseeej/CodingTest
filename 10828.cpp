#pragma warning(disable:4996)
#include <iostream>
#include <stack>
#include <cstring>
using namespace std;

int main() {

	int N;
	cin >> N;

	stack<int> s;

	for (int i = 0; i < N; i++) {
		char temp[10];
		cin >> temp;
		if (!strcmp(temp, "push")) {
			int num;
			cin >> num;
			s.push(num);
		}
		if (!strcmp(temp, "top")) {
			if (s.empty() == 1)
				cout << "-1" << "\n";
			else
				cout << s.top() << "\n";
		}
		if (!strcmp(temp, "size"))
			cout << s.size() << "\n";
		if (!strcmp(temp, "empty"))
			cout << s.empty() << "\n";
		if (!strcmp(temp, "pop")) {
			if (s.empty() == 1)
				cout << "-1" << "\n";
			else {
				cout << s.top() << "\n";
				s.pop();
			}
		}
	}



	return 0;
}