#pragma warning(disable:4996)
#include <iostream>
#include <cmath>
using namespace std;

int ones = 0;
int zeros = 0;

int divide(int** arr, int x, int y, int h) {
	if(h==1){	//색종이의 크기가 1X1일때
		if (arr[x][y]) ones++;	//1로 채워져있으면 1 개수 더하고
		else zeros++;	//0이면 0 개수에 추가
		return arr[x][y];
	}

	int num = 0;
	// 네 번의 재귀 필요. 상하좌우,,~
	num += divide(arr, x, y, h / 2);
	num += divide(arr, x + h / 2, y, h / 2);
	num += divide(arr, x, y + h / 2, h / 2);
	num += divide(arr, x + h / 2, y + h / 2, h / 2);

	if (num == 4) {	//네 칸이 모두 1이면 같은 색종이가 4개니깐
		ones -= 3;	//하나만 더하기 위해서 ones에서 3을 빼주고 최종적으로 1을 더하게 됨
		return 1;	//이건 1로 채워진 종이다!
	}
	if (num == 0) {	//네 칸이 모두 0
		zeros -= 3;	//하나만 count해주기 위해 zeros에서 3 빼줌
		return 0;	//이건 0으로 채워진 종이임을 알려줌
	}

	return -100;
}

int main() {

	int N;
	cin >> N;

	int** board = new int*[N];
	for (int i = 0; i < N; i++)
		board[i] = new int[N];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}

	divide(board, 0, 0, N);

	cout << zeros << "\n";
	cout << ones << "\n";

	for (int i = 0; i < N; i++)
		delete board[i];
	delete[] board;

	return 0;
}