#pragma warning(disable:4996)
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main() {

	int N;
	cin >> N;

	vector<int> data(N);
	vector<int> res(N);

	for (int i = 0; i < N; i++)
		cin >> data[i];

	stack<int> index;
	index.push(0);

	for (int i = 1; i < N; i++) {
		if (index.empty())
			index.push(i);
		while (!index.empty() && (data[index.top()] < data[i])) {
			res[index.top()] = data[i];
			index.pop();
		}
		index.push(i);
	}

	while (!index.empty()) {
		res[index.top()] = -1;
		index.pop();
	}

	for (int i = 0; i < N; i++)
		cout << res[i] << " ";




	return 0;
}