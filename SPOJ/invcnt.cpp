#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
 
const ll MAX = 200001;
 
ll n, bit[MAX], temp[MAX], aux[MAX];
 
void update(int index, int x) {
	while (index <= n) {
		bit[index] += x;
		index += (index & (-index));
	}
}
 
ll get_sum(int index) {
	ll sum = 0;
	while (index >= 1) {
		sum += bit[index];
		index -= (index & (-index));
	}
	return sum;
}
 
ll binary_search(int l, int r, ll x) {
   if (r >= l) {
        int mid = l + (r - l)/2;
        if (temp[mid] == x) return mid;
        if (temp[mid] > x) return binary_search(l, mid-1, x);
        return binary_search(mid+1, r, x);
   }
   return -1;
}
 
int main() {
	ll t, sum;
	scanf("%lld", &t);
 
	while (t--) {
		scanf("%lld", &n);
		for (int i = 1; i <= n; i++) bit[i] = 0;
		for (int i = 1; i <= n; i++) {
			scanf("%lld", &aux[i]);
			temp[i] = aux[i];
		}
 
		sum = 0;
		sort(temp + 1, temp + n + 1);
 		for (ll i = 1; i <= n; i++) {
	 		ll index = binary_search(1, n, aux[i]);
	 		sum += get_sum(n) - get_sum(index);
	 		update(index, 1);
 		}
 		printf("%lld\n", sum);
	}
 
	return 0;
} 