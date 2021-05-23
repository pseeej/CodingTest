#include <iostream>
#include <vector>
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;

	vector<int> arr;
	for (int i = 0; i < N; i++)
		arr.push_back(i + 1);

	while (M--) {
		int a, b;
		cin >> a >> b;
		int temp;
		temp = arr[a-1];
		arr[a-1] = arr[b-1];
		arr[b-1] = temp;
	}

	for (int i = 0; i < arr.size(); i++)
		cout << arr[i] << " ";

	return 0;
}