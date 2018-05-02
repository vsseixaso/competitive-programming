#include<bits/stdc++.h>

using namespace std;

typedef long long LL;

int main(){
  int a[105];
	int n;
	cin>>n;
	for(int i=1 ;i<=n; i++) {
    cin>>a[i];
  }

	LL cnt = 1, ans = 1;
	int l = -1, r = -1;
	for(int i=1; i<=n; i++) {
		if (a[i]) {
			l = i;
			break;
		}
	}
	for(int i=n; i>0; i--) {
		if (a[i]) {
			r = i;
			break;
		}
	}

	if (l == -1 and r == -1) {
		cout<<0<<endl;
		return 0;
	}
	for(int i=l; i<=r; i++) {
		if (a[i]) {
			ans *= cnt;
		 	cnt = 1;
		}
		else cnt++;
	}
	cout<<ans<<endl;
	return 0;
}