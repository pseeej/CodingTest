#include <iostream>
#pragma warning(disable:4996)
using namespace std;

int board[2200][2200];
int ans[3];

bool sameNumbers(int x, int y, int size) {
	int check = board[x][y];
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			if (board[x + i][y + j] != check)
				return false;
		}
	}
	return true;
}

void dfs(int x, int y, int size) {

	if (sameNumbers(x, y, size)) {
		int num = board[x][y];
		ans[num + 1]++;
		return;
	}

	int next = size / 3;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			dfs(x + i * next, y + j * next, next);
		}
	}
	

}

int main() {


	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}

	dfs(0, 0, N);

	for (int i = 0; i < 3; i++)
		cout << ans[i] << "\n";

	return 0;
}