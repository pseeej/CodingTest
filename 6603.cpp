#pragma warning(disable:4996)
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	int k;
	cin >> k;

	while (k != 0) {

		vector<int> v;	// 배열 S 넣을 vector
		for (int i = 0; i < k; i++) {
			int temp;
			cin >> temp;
			v.push_back(temp);
		}

		vector<int> temp;	// 썼는지 안 썼는지 체크할 vector
		for (int i = 0; i < 6; i++)	// 써야 할 개수만큼
			temp.push_back(1);
		for (int i = 0; i < k - 6; i++)	// 입력받은 개수-쓸 개수
			temp.push_back(0);

		//sort(temp.begin(), temp.end());

		do {
			for (int i = 0; i < temp.size(); i++) {
				if (temp[i] == 1)
					cout << v[i] << " ";
			}
			cout << "\n";
		} while (prev_permutation(temp.begin(), temp.end()));

		cout << "\n";

		cin >> k;

	}

	return 0;
}