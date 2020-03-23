#include <iostream>
#include <stdlib.h>
using namespace std;

int* arr;
void backArr(int left, int right);

int main() {

	int num, times;
	cin >> num >> times;

	arr = (int*)malloc(sizeof(int)*num);

	for (int i = 0; i < num; i++) {
		*(arr+i) = i + 1;
	}

	int left, right;
	for (int i = 0; i < times; i++) {
		cin >> left >> right;
		backArr(left, right);
	}

	for (int i = 0; i < num; i++)
		cout << arr[i] << " ";

	return 0;
}

void backArr(int left, int right) {
	int i, j, space;
	space = right - left;
	int temp;
	for (i = left - 1, j = right - 1; i < j; i++, j--) {
		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
}