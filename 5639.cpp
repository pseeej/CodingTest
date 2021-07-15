#include <iostream>
#include <vector>
using namespace std;

struct Node {
	Node* left;
	Node* right;
	int value;
};

Node* preorder(Node* node, int key) {
	if (node == NULL) {	// NULL ������ node�� key�� ����
		node = new Node();
		node->value = key;
		node->left = NULL;	// ���� ������ NULL�� �ʱ�ȭ����.
		node->right = NULL;
	}
	if (node->value > key) {
		node->left = preorder(node->left, key);	// �� ĭ�� ���� �������鼭 key ������ ��ġ ã�Ƴ�
	}
	if (node->value < key) {
		node->right = preorder(node->right, key);	// �� ĭ�� �������鼭 key ������ ��ġ ã�Ƴ�
	}

	return node;
}

void postorder(Node* node) {
	// ���ʺ��� ���������� Ž�� ����
	if (node->left != NULL)
		postorder(node->left);
	// ���� �� ������ �� �������� ������ Ž��
	if (node->right != NULL)
		postorder(node->right);
	cout << node->value << "\n";
	// �̹� ����ߴٴ� �� �˷��ֱ� ���� NULLó������
	node = NULL;
}

int main() {

	Node* tree = NULL;
	while (true) {	// ����� ������,,,
		int n;
		cin >> n;
		if (cin.eof() == true)	// eof�� ctrl+z
			break;
		tree = preorder(tree, n);	// �Է� ��� Ʈ���� ����

	}

	postorder(tree);



	return 0;
}