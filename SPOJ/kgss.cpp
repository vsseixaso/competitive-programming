#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
 
#define N 100000
 
struct s {
	long long int max_sum;
	long long int maxx;
};
 
s st[4*N + 1];
int a[N + 1];
 
s merge(s l, s r) {
	int max_sum = max(l.max_sum, max(r.max_sum, (l.maxx + r.maxx)));
	int maxx = max(l.maxx, r.maxx);
	return ((s) {max_sum, maxx});
}
 
void build(int id, int l, int r) {
	if (l == r) {
		st[id] = ((s) {a[l], a[l]});
	} else {
		int m = (l+r)/2;
		build(id*2, l, m);
		build(id*2 + 1, m+1, r);
		st[id] = merge(st[id*2], st[id*2 + 1]);
	}
}
 
void update(int id, int l, int r, int p, int v) {
	if (l == r && l == p) {
		st[id] = ((s) {v, v});
		return;
	} 
	int m = (l+r)/2;
	if (p <= m) update(id*2, l, m, p, v);
	else update (id*2 + 1, m+1, r, p, v);
	st[id] = merge(st[id*2], st[id*2 + 1]);
}
 
s query(int id, int l, int r, int x, int y) {
	if (l > r || l > y || r < x) return ((s) {0, 0});
	else if (l >= x && r <= y) return st[id];
	int m = (l+r)/2;
	return merge(query(id*2, l, m, x, y), query(id*2 + 1, m+1, r, x, y));
}
 
int main() {
	int n, q, l, r;
	char c;
 
	scanf("%d", &n);
	for (int i = 0; i < n; i++)	{
		scanf("%d", a+i);
	}
 
	build(1, 0, n-1);
 
	scanf("%d", &q);
	for (int i = 0; i < q; i++)	{
		scanf("%*c%c%d%d", &c, &l, &r);
		if (c == 'U') update(1, 0, n-1, l-1, r);
		else printf("%lld\n", query(1, 0, n-1, l-1, r-1).max_sum);
	}
 
	return 0;
} 