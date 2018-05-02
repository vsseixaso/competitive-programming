#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int main() {
	int n, m, aux, out = 0;
	vi boys, girls;

	scanf("%d", &n);
	for (int i=0; i<n; i++) {
		scanf("%d", &aux);
		boys.push_back(aux);
	}

	scanf("%d", &m);
	for (int i=0; i<m; i++) {
		scanf("%d", &aux);
		girls.push_back(aux);
	}

	sort(boys.begin(), boys.end());
	sort(girls.begin(), girls.end());

	for (int i = 0; i < n; i++) {
	    for (int j = 0; j < m; j++) {
	        if (abs(boys[i] - girls[j]) <= 1) {
	            girls[j] = -1;
	            out++;
	            break;
	        }
	    }
	}

	printf("%d\n", out);

	return 0;
}
