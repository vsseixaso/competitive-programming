#include <bits/stdc++.h>
 
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main() {
	int x, y, ans = 0;

	scanf("%d %d", &x, &y);

	if (x < 2 && y < 2) {
		printf("%d\n", 0);
	} else {
		while (x > 0 && y > 0) {
			if (x > y) {
				y+=1;
				x-=2;
			} else {
				x+=1;
				y-=2;
			}
			ans++;
		}

		printf("%d\n", ans);
	}

	return 0;
}