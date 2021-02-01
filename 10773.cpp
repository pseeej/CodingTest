#pragma warning(disable:4996)
#include <iostream>
#include <stack>
using namespace std;

int main() {

	int N;
	cin >> N;

	stack<int> s;
	int num;
	int sum = 0;

	for (int i = 0; i < N; i++) {
		cin >> num;
		if (num == 0) {
			sum -= s.top();
			s.pop();
		}
		else {
			s.push(num);
			sum += num;
		}
	}

	cout << sum;

	return 0;
}