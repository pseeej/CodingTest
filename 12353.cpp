#pragma warning(disable:4996)
#include <iostream>
#include <string>
using namespace std;

int main() {

	int T;
	cin >> T;

	for (int k = 1; k <= T; k++) {
		char type;
		cin >> type;

		string dheight, mheight;
		cin >> dheight >> mheight;

		int dad = 0;
		int mom = 0;

		dad += (dheight[0] - '0') * 12;
		mom += (mheight[0] - '0') * 12;

		if (dheight.length() == 5) {
			dad += (dheight[2] - '0') * 10;
			dad += (dheight[3] - '0');
		}
		else
			dad += (dheight[2] - '0');

		if (mheight.length() == 5) {
			mom += (mheight[2] - '0') * 10;
			mom += (mheight[3] - '0');
		}
		else
			mom += (mheight[2] - '0');

		int res = 0;
		res = dad + mom;

		if (type == 'B')
			res += 5;
		if (type == 'G')
			res -= 5;

		int less, more;
		if (res % 2 == 0) {
			res /= 2;
			less = res - 4;
			more = res + 4;
		}
		else {
			float temp = res;
			temp /= 2;
			less = temp - 3.5;
			more = temp + 3.5;
		}

		cout << "Case #" << k << ": ";
		cout << less / 12 << "'" << less % 12 << "\" to ";
		cout << more / 12 << "'" << more % 12 << "\"\n";

	}


	return 0;
}