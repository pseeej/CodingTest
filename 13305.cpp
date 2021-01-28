#pragma warning(disable:4996)
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	long long N;
	cin >> N;

	long long* dist = new long long[N - 1];
	long long* oil = new long long[N];

	for (int i = 0; i < N; i++) {
		dist[i] = 0;
		if(i<N-1)
			oil[i] = 0;
	}

	long long mini = 999999;

	for (int i = 0; i < N - 1; i++)
		cin >> dist[i];
	for (int i = 0; i < N; i++)
		cin >> oil[i];

	long long sum = 0;

	for (int i = 0; i < N-1; i++) {
		mini = min(oil[i], mini);
		sum += mini * dist[i];
	}

	cout << sum;

	return 0;
}