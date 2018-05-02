#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;

	string s(n, 'a');

	if (n == 1) cout << "a";
	else if (n == 2) cout << "aa";
	else {
		s[0] = 'a';
		s[1] = 'a';

		for(int i = 2; i < n; i++) {
	        if(s[i-2] == 'a') s[i]= 'b';
	        else s[i]= 'a';
	    }

	    cout << s;
	}

	return 0;
}