#define _CRT_NO_SECURE_WARNINGS
#include <iostream>
using namespace std;

int board[9][9] = { 0, };

void input(void) {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> board[i][j];
		}
	}
}

void printBoard() {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cout << board[i][j] << " ";
		}
		cout << "\n";
	}
}

void giveNum(int row, int col) {
	int used_num[9] = { 0, };

	//가로세로
	for (int i = 0; i < 9; i++) {
		if (board[i][col])
			used_num[board[i][col] - 1] = 1;
		if (board[row][i])
			used_num[board[row][i] - 1] = 1;
	}

	//박스 check
	int temp_row = row / 3;
	int temp_col = col / 3;
	temp_row *= 3;
	temp_col *= 3;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (board[temp_row + i][temp_col + j])
				used_num[board[temp_row + i][temp_col + j] - 1] = 1;
		}
	}

	int stack[9] = { 0, };
	int top = -1;

	for (int i = 0; i < 9; i++) {
		if (!used_num[i])
			stack[++top] = i+1;
	}

	if (top == -1)
		return;

	int nextR = row, nextC = col;
	
	while (1) {
		if ((++nextC) == 9) {
			nextR++;
			nextC = 0;

			if (nextR == 9) {
				board[row][col] = stack[0];
				printBoard();
				exit(0);
			}
		}
		if (nextR == 9)
			break;
		if (board[nextR][nextC] == 0)
			break;
	}

	for (int i = 0; i < top+1; i++) {
		board[row][col] = stack[i];
		giveNum(nextR, nextC);
		board[row][col] = 0;
	}

}

int main() {

	input();
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (board[i][j] == 0)
				giveNum(i, j);
		}
	}

	return 0;
}