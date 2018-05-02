#include <bits/stdc++.h>

using namespace std;
 
int n, m, x, y, parent[100];
 
int find(int x) {
	if (parent[x] != x)	parent[x] = find(parent[x]);
	return parent[x];
}
 
int main() {
	scanf("%d %d", &n, &m);

	for (int i = 1; i <= n; i++) {
		parent[i] = i;
	}

	while (m--) {
		scanf("%d%d", &x, &y);
		parent[find(x)] = find(y);
	}

	long long ans = (1LL << n);
	
	for (int i = 1; i <= n; i++) {
		if (find(i) == i) {
			ans /= 2;
		}
	}
	
	cout << ans << endl;
}