#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {

	string S;
	cin >> S;

	vector<string> v;
	for (int i = 0; i < S.size(); i++) {
		string temp;
		for (int j = i; j < S.size(); j++) {
			temp += S[j];
		}
		v.push_back(temp);
	}

	sort(v.begin(), v.end());
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << "\n";
	}


	return 0;
}