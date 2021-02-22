#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

int main() {

	string str;
	cin >> str;

	while (str != "0") {

		char temp1[5];
		char temp2[5];

		int len = str.length();
		int checkif = 1;

		if (len % 2) {
			for (int i = 0; i < len / 2 + 1; i++) {
				if (str[i] == str[len - 1 - i]);
				else {
					checkif = 0;
					break;
				}
			}
		}
		else {
			for (int i = 0; i < len / 2; i++) {
				if (str[i] == str[len - 1 - i]);
				else {
					checkif = 0;
					break;
				}
			}
		}

//		cout << temp1 << endl;

		if (checkif)
			cout << "yes\n";
		else
			cout << "no\n";

		cin >> str;
	}

	return 0;
}