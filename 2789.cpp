#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	string kijun = "CAMBRIDGE";
	string str;
	cin >> str;

	for (int i = 0; i < kijun.length(); i++) {
		for (int j = 0; j < str.length(); j++) {
			if (kijun[i] == str[j])
				str[j] = '0';
		}
	}

	for (int i = 0; i < str.length(); i++)
		if (str[i] != '0')
			cout << str[i];


	return 0;
}