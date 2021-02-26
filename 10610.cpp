#pragma warning(disable:4996)
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	string N;
	cin >> N;	

	int sum = 0;
	int checkif = 0;
	for (int i = 0; i < N.length(); i++) {
		sum += (N[i] - '0');
		if (N[i] == '0')
			checkif = 1;
	}

	if (checkif == 0 || sum % 3 != 0) {
		cout << "-1";
		return 0;
	}

	int len = N.length();

	vector<char> v;

	for (int i = 0; i < len; i++)
		v.push_back(N[i]);
	
	sort(v.begin(), v.end());

	for (int i = len-1; i >=0; i--)
		cout << v[i];


	return 0;
}