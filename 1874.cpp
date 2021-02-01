#pragma warning(disable:4996)
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {

	stack<int> s;
	vector<char> op;
	int index = 1;

	int N;
	cin >> N;

	while (N--) {
		int num;
		cin >> num;

		if (s.empty()) {
			s.push(index++);
			op.push_back('+');
		}

		if (!s.empty() && s.top() > num) {
			cout << "NO";
			return 0;
		}

		while (!s.empty() && s.top() < num) {
			s.push(index++);
			op.push_back('+');
		}

		if (!s.empty() && s.top() == num) {
			s.pop();
			op.push_back('-');
		}
	}

	for (int i = 0; i < op.size(); i++)
		cout << op[i] << "\n";

	
	return 0;
}