#pragma warning(disable:4996)
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int checkVPS(string input) {
	stack<char> s;

	for (int i = 0; i < (int)input.size(); i++) {
		if (input[i] == '(')
			s.push('(');
		if (input[i] == ')') {
			if (s.empty())
				return 0;
			s.pop();
		}
	}

	if (!s.empty())
		return 0;

	return 1;
}

int main() {

	int N;
	cin >> N;

	string gwalho;

	for (int i = 0; i < N; i++) {
		cin >> gwalho;
		if (checkVPS(gwalho))
			cout << "YES" << "\n";
		else
			cout << "NO" << "\n";
	}


	return 0;
}