#include <iostream>
using namespace std;

int main() {

	int T;
	cin >> T;

	int board[100][100] = { 0, };

	while (T--) {
		int a, b;
		cin >> a >> b;

		for (int i = a; i < a + 10; i++) {
			for (int j = b; j < b + 10; j++) {
				board[i][j] = 1;
			}
		}

	}
	
	int cnt = 0;
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			if (board[i][j] == 1)
				cnt++;
		}
	}

	cout << cnt;


	return 0;
}