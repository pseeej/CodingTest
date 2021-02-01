#pragma warning(disable:4996)
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int check(string str) {
	stack<char> s;
	int gwal = 0;

	for (int i = 0; i < (int)str.size(); i++) {
		if (str[i] == '(' || str[i] == '[') {
			s.push(str[i]);
			gwal = 1;
		}

		if (str[i] == ')') {
			if (!s.empty() && s.top() == '(') {
				s.pop();
			}
			else
				return 0;
		}
		if (str[i] == ']') {
			if (!s.empty() && s.top() == '[') {
				s.pop();
			}
			else
				return 0;
		}

	}

	//괄호가 분명히 쓰였는데 스택이 안 비어있을 경우
	if (gwal == 1 && !s.empty())
		return 0;

	return 1;
}

int main() {

	while (1) {

		string str;
		getline(cin, str);	//계속 str가 범위를 초과했다고 떠서 getline 이용

		if (str[0]=='.')
			break;

		if (check(str))
			cout << "yes\n";
		else
			cout << "no\n";
	}


	return 0;
}