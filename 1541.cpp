#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

int main() {

	string shick;
	cin >> shick;
	string temp="";
	int res = 0;
	int minus = 0;

	for (int i = 0; i <= (int)shick.size(); i++) {
		if (shick[i] == '+' || shick[i] == '-' || shick[i]=='\0') {
			if (minus)
				res -= stoi(temp);
			else
				res += stoi(temp);

			temp = "";
			if (shick[i] == '-')
				minus = 1;
		}
		else
			temp += shick[i];
	}

	std::cout << res;


	return 0;
}
