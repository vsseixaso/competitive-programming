#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
	int t, n, m, x;
	queue<int> q;
 
	scanf("%d", &t);
	for (int i=0; i<t; ++i) {
		scanf("%d", &n);
		if (n == 1) {
			scanf("%d", &m);
			q.push(m);
		} else if (n == 2 && !q.empty()) {
			q.pop();
		} else if (n == 3) {
			if (q.empty()) {
				printf("%s\n", "Empty!");
			} else {
				x = q.front();
				printf("%d\n", x);
			}
		}
	}
 
	return 0;
} 