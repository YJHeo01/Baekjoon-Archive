#include <stdio.h>
#include <stdlib.h>
struct node {
	int i;
	struct node* left;
	struct node* right;
};

struct node* root = 0;

void BST(int n) {
	struct node* cur = (struct node*)malloc(sizeof(struct node));
	cur->i = n;
	cur->left = 0;
	cur->right = 0;
	if (root == 0) {
		root = cur;
	}
	else {
		struct node* tmp = root;
		while (1) {
			if (tmp->i > n) {
				if (tmp->left == 0) {
					tmp->left = cur;
					return;
				}
				else {
					tmp = tmp->left;
				}
			}
			else {
				if(tmp->right == 0) {
					tmp->right = cur;
					return;
				}
				else {
				tmp = tmp->right;
				}
			}
			if (tmp == 0) {
				tmp = cur;
				return;
			}
		}
	}
}

void Postorder(struct node* node) {
	if (node == 0) {
		return;
	}
	Postorder(node->left);
	Postorder(node->right);
	printf("%d\n", node->i);
}
int main() {
	int n;
	int cnt = 0;
	while (scanf("%d", &n) != EOF) {
		BST(n);
	}
	Postorder(root);
}