#define _CRT_NO_SECURE_WARNINGS
#include <iostream>
#include <cmath>
using namespace std;

int board[21][21];
int visited[21] = { 0, };

int ans = 99999999;
int n;

void combination(int cnt, int before) {
	if (cnt == n / 2) {
		int sum1 = 0;
		int sum2 = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (visited[i] == 1 && visited[j] == 1) {
					sum1 = sum1 + board[i][j] + board[j][i];
				}
				else if (visited[i] == 0 && visited[j] == 0) {
					sum2 = sum2 + board[i][j] + board[j][i];
				}
				else;
			}
		}
		int temp = abs(sum1 - sum2);
		if (temp < ans)
			ans = temp;
	}
	for (int i = 0; i < n; i++) {
		if (visited[i] == 0 && i > before) {
			visited[i] = true;
			combination(cnt + 1, i);
			visited[i] = false;
		}
	}
}

int main() {

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> board[i][j];
		}
	}

	combination(0, -1);

	cout << ans;


	return 0;
}