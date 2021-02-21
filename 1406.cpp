#pragma warning(disable:4996)
#include <iostream>
#include <string>
#include <stack>
#include <cstdio>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	string str;
	cin >> str;

	int N;
	cin >> N;

	stack<char> s1;
	stack<char> s2;	//보조 역할

	for (int i = 0; i < str.length(); i++) {
		s1.push(str[i]);
	}

	for (int i = 0; i < N; i++) {
		char in;
		cin >> in;

		if (in == 'L') {
			if (s1.empty())
				continue;
			//char temp = s1.top();
			s2.push(s1.top());
			s1.pop();
		}

		if (in == 'D') {
			if (s2.empty())
				continue;
			s1.push(s2.top());
			s2.pop();
		}

		if (in == 'B') {
			if (s1.empty())
				continue;
			s1.pop();
		}

		if (in == 'P') {
			char temp;
			cin >> temp;
			s1.push(temp);
		}
	}

	while (!s2.empty()) {
		s1.push(s2.top());
		s2.pop();
	}

	//while (!s1.empty()) {

	//	/*cout << s1.top();
	//	s1.pop();*/
	//}

	char* res = new char[s1.size()+1];
	int index = 0;
	while (!s1.empty()) {
		res[index++] = s1.top();
		s1.pop();
	}

	for (int i = index - 1; i >= 0; i--)
		cout << res[i];

	return 0;
}