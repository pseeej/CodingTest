#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main() {

	string a, b;
	cin >> a >> b;

	if (a.size() < b.size()) {
		string temp;
		temp = a;
		a = b;
		b = temp;
	}

	int numa[10001] = { 0, };
	int numb[10001] = { 0, };

	for (int i = 0; i < a.size(); i++) {
		numa[i + 1] = a[i] - '0';
	}
	for (int i = 0; i < b.size(); i++) {
		numb[i + 1] = b[i] - '0';
	}

	int ans[10001] = { 0, };

	for (int i = a.size(); i > 0; i--) {
		int sum = numa[i] + numb[i];
		if (sum >= 10) {
			ans[i] += sum - 10;
			ans[i - 1] += 1;
		}
		else {
			ans[i] += sum;
		}
	}

	for (int i = 0; i <= a.size(); i++) {
		cout << ans[i];
	}

	return 0;
}

/*
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int main() {

	unsigned long long a, b;
	scanf("%llu %llu", &a, &b);
	printf("%llu", a + b);



	return 0;
}
¿Ã∞Õµµ µ 
*/