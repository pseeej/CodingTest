#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int a, b;
	cin >> a >> b;

	int** dp = new int*[a+1];
	for (int i = 0; i < a+1; i++)
		dp[i] = new int[a+1];

	for (int i = 1; i <= a; i++) {
		for (int j = 0; j <= a; j++) {
			if (i == j || j == 0)	//양쪽 끝의 값은 1
				dp[i][j] = 1;
			else    //파스칼의 삼각형 이용함. 위에 거 두 개 더한 게 아래 값
				dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007;
		}
	}
	
	cout << dp[a][b];

	return 0;
}