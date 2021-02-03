#pragma warning(disable:4996)
#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
using namespace std;

int main() {

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		string op;
		cin >> op;

		int n;
		cin >> n;

		deque<int> dq;

		string nums;
		cin >> nums;
		char temp[3];
		int index = 0;

		for (int j = 0; j < nums.size(); j++) {
			if (nums[j] >= '0' && nums[j] <= '9') {
				temp[index++] = nums[j];
			}
			else {
				if(index!=0)
					dq.push_back(stoi(temp));
				for (int k = 0; k < index; k++)
					temp[k] = '\0';
				index = 0;
			}
		}

		int reverse = 0;	//0일 때가 정방향. 1일 때가 역방향
		int check = 1;

		for (int j = 0; j < op.size(); j++) {
			if (op[j] == 'R') {
				reverse = !reverse;
			}
			if (op[j] == 'D') {
				if (dq.empty()) {
					check = 0;
					cout << "error\n";
					break;
				}
				if (reverse == 1) {
					dq.pop_back();
				}
				else
					dq.pop_front();
			}
		}

		if (check == 0)
			continue;
		cout << "[";

		if (reverse) {
			while (!dq.empty()) {
				cout << dq.back();
				dq.pop_back();
				if (!dq.empty())
					cout << ",";
			}
		}
		else {
			while (!dq.empty()) {
				cout << dq.front();
				dq.pop_front();
				if (!dq.empty())
					cout << ",";
			}
		}
		cout << "]\n";

	}



	return 0;
}