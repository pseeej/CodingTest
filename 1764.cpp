#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int N, M;
	cin >> N >> M;

	vector<string> first;
	for (int i = 0; i < N; i++) {
		string temp;
		cin >> temp;
		first.push_back(temp);
	}

	sort(first.begin(), first.end());

	vector<string> second;
	for (int i = 0; i < M; i++) {
		string temp;
		cin >> temp;
		second.push_back(temp);
	}

	sort(second.begin(), second.end());

	vector<string> third;

	for(int i=0;i<N;i++)
		if (binary_search(second.begin(), second.end(), first[i])) {
			third.push_back(first[i]);
		}

	sort(third.begin(), third.end());
	cout << third.size() << "\n";
	for (int i = 0; i < third.size(); i++)
		cout << third[i] << "\n";


	return 0;
}