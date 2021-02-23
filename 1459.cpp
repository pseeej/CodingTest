#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	long long x, y;
	int w, s;
	cin >> x >> y >> w >> s;

	long long mod = (x + y) % 2;
	if (x < y) swap(x, y);	//x에 더 큰 수가 오도록 함

	// 방법은 총 세 가지

	// 평행선으로만 가기
	// 대각선으로만 가기
	// 대각선으로 갈 수 있는 만큼 가다가 평행선으로 가기

	// 이 때 대각선은 /랑 \ 두 방향 모두 존재.
	// 대각선으로만 가려면 x+y가 짝수여야 함

	cout << min((x + y) * w, min((x - mod) * s + mod * w, y * s + (x - y) * w));

	return 0;
}