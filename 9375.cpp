#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

int main() {

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int wearings;
		cin >> wearings;

		string* types = new string[wearings];
		int* cntType = new int[wearings];
		for (int i = 0; i < wearings; i++)
			cntType[i] = 0;

		int index = 0;
		for (int j = 0; j < wearings; j++) {
			string temp;
			cin >> temp;	//이름

			string type;
			cin >> type;	//종류

			int check = 0;	//그냥 확인용

			for (int k = 0; k < index; k++) {
				if (type == types[k]) {	//입력받은 게 types에 있을 경우
					cntType[k]++;	//해당 type의 개수++
					check = 1;
					break;
				}
			}
			if (check == 0) {	//입력받은 게 types에 없을 경우
				types[index] = type;	//types에 추가해줌
				cntType[index] += 1;	//cntType에 값 새로 넣어줌
				index++;
			}
		}

		int res = 1;
		for (int i = 0; i < index; i++)
			res *= (cntType[i] + 1);

		cout << res - 1 << "\n";

	}


	return 0;
}