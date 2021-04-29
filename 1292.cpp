#include <iostream>
using namespace std;

int main() {

	int a = 1;
	int cnt = 0;

	int A, B;
	cin >> A >> B;
	int sum = 0;

	while (cnt<1000) {
		for (int i = 0; i < a; i++) {
			cnt++;
			if (cnt >= A && cnt <= B)
				sum += a;
		}
		a++;
	}

	cout << sum;

	return 0;
}