#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;

	int arr[21] = { 0, };

	while (N--) {
		string str;
		cin >> str;

		int n;

		if (str == "add") {
			cin >> n;

			arr[n] = 1;
		}
		if (str == "remove") {
			cin >> n;

			arr[n] = 0;
		}
		if (str == "check") {
			cin >> n;

			cout << arr[n]<<"\n";
		}
		if (str == "toggle") {
			cin >> n;

			arr[n]=!arr[n];
		}
		if (str == "all") {
			for (int i = 0; i < 21; i++) {
				arr[i] = 1;
			}
		}
		if (str == "empty") {
			for (int i = 0; i < 21; i++)
				arr[i] = 0;
		}
	}



	return 0;
}