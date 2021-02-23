#pragma warning(disable:4996)
#include <iostream>
using namespace std;

typedef struct{
	int x, y;
}point;

point snail(int n) {
	point p{ 0, 0 };
	bool sign = true;	//부호 확인
	int len = 1;

	while (1) {
		if (sign) {
			for (int i = 0; i < len; i++) {
				p.y++;
				n--;
				if (n == 0)
					return p;
			}
			for (int i = 0; i < len; i++) {
				p.x++;
				n--;
				if (n == 0)
					return p;
			}
		}
		else {
			for (int i = 0; i < len; i++) {
				p.y--;
				n--;
				if (n == 0)
					return p;
			}
			for (int i = 0; i < len; i++) {
				p.x--;
				n--;
				if (n == 0)
					return p;
			}
		}

		sign = !sign;
		len++;
	}
}

int main() {

	int n;
	cin >> n;

	point res = snail(n);
	cout << res.x << " " << res.y;

	return 0;
}