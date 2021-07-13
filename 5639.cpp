#include <iostream>
#include <vector>
using namespace std;

struct node {
	node* left;
	node* right;
	int value;
};

int main() {

	vector<int> v;
	while (true) {	// 종료될 때까지,,,
		int n;
		cin >> n;
		v.push_back(n);
		if (cin.eof() == true)
			break;
	}

	node* tree;
	tree->value = v[0];
	for (int i = 0; i < v.size(); i++) {
		tree->left->value = v[i];
	}




	return 0;
}
