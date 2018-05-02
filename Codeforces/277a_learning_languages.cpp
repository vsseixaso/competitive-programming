#include<bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

bool visited[100];
bool graph[100][100];
bool flag = true;
int n, m, k, a, ans = 0;

void tdo(int start) {
	visited[start] = true;
	for (int i=0; i<n; i++) {
		if (!visited[i]) {
			for (int j=0; j<m; j++) {
				if (graph[i][j] && graph[start][j]) {
					tdo(i);
				}
			}
		}
	}
}

int main() {
	scanf("%d %d", &n, &m);

	for (int i=0; i<n; i++) {
		scanf("%d", &k);
		for (int j=0; j<k; j++) {
			scanf("%d", &a);
			graph[i][a-1] = true;
			flag = false;
		}
	}

	for (int i=0; i<n; i++) {
		if (!visited[i]) {
			tdo(i);
			ans++;
		}
	}

	if (flag) printf("%d\n", ans);
	else printf("%d\n", ans-1);

	return 0;
}