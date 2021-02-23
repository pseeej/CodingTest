#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;

	int* arr = new int[N+1];
	for (int i = 1; i < N+1; i++)
		arr[i] = i;

	int begin, end, mid;

	int* temp = new int[N+1];
	for (int i = 0; i < N + 1; i++)
		temp[i] = 0;
	

	while (M--) {
		cin >> begin >> end >> mid;

		int index = 1;
		for (int i = mid; i <= end; i++) {
			temp[index++] = arr[i];
		}
		for (int i = begin; i <= mid - 1; i++) {
			temp[index++] = arr[i];
		}

		index = 1;
		
		for (int i = begin; i <= end; i++)
			arr[i] = temp[index++];

		index = 1;
		
	}


	for (int i = 1; i <= N; i++)
		cout << arr[i] << " ";


	delete[] arr, temp;
	
	return 0;
}