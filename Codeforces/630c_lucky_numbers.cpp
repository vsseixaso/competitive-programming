#include <bits/stdc++.h>

using namespace std;

int main(){
	int n;
	scanf("%d",&n);

  unsigned long long int ans;
	ans = pow(2, (n+1)) - 2;

	printf("%llu\n", ans);

  return 0;
}