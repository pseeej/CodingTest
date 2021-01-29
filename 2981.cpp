#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b) {
	if (b == 0)
		return a;
	else
		return gcd(b, a % b);
}

int main() {

	int N;
	cin >> N;

	int* arr = new int[N];
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	sort(arr, arr + N);

	//arr[n] - arr[n-1] = M * ((arr[n]/M)-(arr[n-1]/M))
	int minus = arr[1] - arr[0];
	for (int i = 2; i < N; i++)
		minus = gcd(minus, arr[i] - arr[i - 1]);

	//약수 구하기
	int res[500];
	int index = 0;
	for (int i = 1; i * i <= minus; i++) {
		if (minus % i == 0) {
			res[index++] = i;
			if (i != minus / i)
				res[index++] = minus / i;
		}
	}

	sort(res, res + index);
	for (int i = 0; i < index; i++)
		if(res[i]!=1)
			cout << res[i] << " ";


	return 0;
}