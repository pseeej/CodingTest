#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

int b[65][65];

void divide(int x, int y, int size) {
	if (size == 1) {	//칸 사이즈가 1x1
		cout << b[x][y];
		return;
	}

	int onlyOne = 1;
	int onlyZero = 1;
	for (int i = x; i < x + size; i++) {
		for (int j = y; j < y + size; j++) {
			if (b[i][j] == 0) onlyOne = 0;	//하나라도 0이 있으면 1이 안되잖앙
			if (b[i][j] == 1) onlyZero = 0;
		}
	}

	if (onlyOne == 1) {	// 다 1이면
		cout << 1;
		return;
	}
	if (onlyZero == 1) {	//다 0이면
		cout << 0;
		return;
	}

	cout << "(";
	divide(x, y, size / 2);	//왼쪽 위
	divide(x, y + size / 2, size / 2);	//오른쪽 위
	divide(x + size / 2, y, size / 2);	//왼쪽 아래
	divide(x + size / 2, y + size / 2, size / 2);	//오른쪽 아래
	cout << ")";

}

int main() {

	int N;
	cin >> N;

	char temp;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> temp;
			b[i][j] = temp - '0';
		}
	}


	divide(0, 0, N);


	return 0;
}