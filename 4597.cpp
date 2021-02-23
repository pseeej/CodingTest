#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

int main() {

	string str;
	cin >> str;

	while (str != "#") {
		if (str[str.length() - 1] == 'e') {
			int cnt = 0;
			for (int i = 0; i < str.length()-1; i++) {
				if (str[i] == '1')
					cnt++;
			}
			if (cnt % 2 == 0)
				str[str.length() - 1] = '0';
			else
				str[str.length() - 1] = '1';
		}
		if (str[str.length() - 1] == 'o') {
			int cnt = 0;
			for (int i = 0; i < str.length() - 1; i++) {
				if (str[i] == '1')
					cnt++;
			}
			if (cnt % 2 == 0)
				str[str.length() - 1] = '1';
			else
				str[str.length() - 1] = '0';
		}

		cout << str << "\n";

		cin >> str;
	}


	return 0;
}