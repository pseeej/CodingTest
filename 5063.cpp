#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int T;
	cin >> T;

	while (T--) {
		int r, e, c;
		cin >> r >> e >> c;

		if (r + c < e)
			cout << "advertise\n";
		else if (r + c == e)
			cout << "does not matter\n";
		else
			cout << "do not advertise\n";
	}



	return 0;
}