#include <bits/stdc++.h>

using namespace std;

int main() {
	int r, g, b;
	int rmod, gmod, bmod;
	int count;
	
	scanf("%d %d %d", &r, &g, &b);
	
	rmod = r % 3;
	gmod = g % 3;
	bmod = b % 3;
	count += (r/3 + g/3 + b/3 + min(min(rmod, gmod), bmod));
	
	if (   rmod == 2 && gmod == 2 && bmod == 0 && b != 0
		|| gmod == 2 && bmod == 2 && rmod == 0 && r != 0
		|| bmod == 2 && rmod == 2 && gmod == 0 && g != 0) {
		count += 1;
	}
		
	printf("%d", count);
	
	return 0;
}