#include <bits/stdc++.h>

using namespace std;

struct node {
	bool vis;
	node* left;
	node* right;
	int value;
	node() {}
	node(int value):
		value(value), vis(false), left(NULL), right(NULL){}
};

struct BST {
	node* root;

	BST(){}
	void add(node *current) {
		if(root == NULL) {
			root = current;
		} else {
			aux_add(root, current);
		}
	}

	void aux_add(node *parent, node *node_to_add) {
		if(parent -> value > node_to_add -> value) {
			if(parent -> left == NULL) {
				parent->left = node_to_add;
			} else {
				aux_add(parent->left, node_to_add);
			}
		} else {
			if(parent->right == NULL) {
				parent->right = node_to_add;
			} else {
				aux_add(parent->right, node_to_add);
			}
		}
	}

	vector<int> bfs() {
		vector<int> to_return;
		queue<node*> q;
		q.push(root);
		root -> vis = true;
		while(!q.empty()) {
			node* top = q.front();
			q.pop();
			if(top -> left != NULL && !top -> left -> vis) {
				q.push(top -> left);
				top -> left -> vis = true;
			}
			if(top -> right != NULL && !(top -> right -> vis)) {
				q.push(top -> right);
				top -> right -> vis = true;
			}
			to_return.push_back(top -> value);
		}
		return to_return;
	}
};

int main() {
	int tests;
	scanf("%d", &tests);
	int cases = 1;
	while(tests--) {
		BST bst;
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			int current;
			scanf("%d", &current);
			bst.add(new node(current));
		}
		vector<int> result = bst.bfs();
		printf("Case %d:\n", cases);
		for(int i = 0; i < result.size(); i++) {
			if(i == result.size() -1) {
				printf("%d", result[i]);
			} else {
				printf("%d ", result[i]);
			}
		}
		printf("\n");
		printf("\n");
		cases ++;
		bst.root = NULL;
	}
	return 0;
}