#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<vi> vvi;
 
#define N 100000
 
lli st[4*N + 1], flag[4*N + 1];
 
lli merge(lli l, lli r) {
	return l + r;
}
 
void build(lli id, lli l, lli r) {
	if (l == r) {
		st[id] = flag[id] = 0;
	} else {
		lli m = (l+r)/2;
		build(id*2, l, m);
		build(id*2 + 1, m+1, r);
		st[id] = flag[id] = 0;
	}
}
 
void refresh(lli id, lli l, lli r) {
	if (flag[id]) {
		st[id] += (r-l + 1) * flag[id];
		if (l != r) {
			flag[id*2] += flag[id];
			flag[id*2 + 1] += flag[id];
		}
		flag[id] = 0;
	}
}
 
void update(lli id, lli l, lli r, lli x, lli y, lli v) {
	if (l > r || l > y || r < x) {
		refresh(id, l, r);
		return;
	} else if (l >= x && r <= y) {
		flag[id] += v;
		refresh(id, l, r);
		return;
	}
	refresh(id, l, r);
	lli m = (l+r)/2;
	update(id*2, l, m, x, y, v);
	update(id*2 + 1, m+1, r, x, y, v);
	st[id] = merge(st[id*2], st[id*2 + 1]);
}
 
lli query(lli id, lli l, lli r, lli x, lli y) {
	if (l > r || l > y || r < x) {
		return 0;
	} else if (l >= x && r <= y) {
		refresh(id, l, r);
		return st[id];
	}
	lli m = (l+r)/2;
	refresh(id, l, r);
	return merge(query(id*2, l, m, x, y), query(id*2 + 1, m+1, r, x, y));
}
 
int main() {
	lli t, n, c, l, r, v, q;
 
	scanf("%lld", &t);
	while(t--) {
		scanf("%lld%lld", &n, &c);
		build(1, 0, n-1);
		for (int i = 0; i < c; i++) {
			scanf("%lld", &q);
			if (!q) {
				scanf("%lld%lld%lld", &l, &r, &v);
				update(1, 0, n-1, l-1, r-1, v);
			} else {
				scanf("%lld%lld", &l, &r);
				printf("%lld\n", query(1, 0, n-1, l-1, r-1));
			}
		}
	}
 
	return 0;
} 