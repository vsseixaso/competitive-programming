#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

vvi graph;
vi visited;
bool is_circuit;

void dfs(int n) {
	visited[n] = 1;
	if (is_circuit) return;
	for (int i=0; i<graph[n].size(); i++) {
		if (visited[graph[n][i]] == 1) {
			is_circuit = true;
			return;
		} else if (visited[graph[n][i]] == 0) {
			dfs(graph[n][i]);
		}
	}	
	visited[n] = 2;
}

int main ()
{
	int t, n, m, a, b;
	
	cin >> t;

	while (t--) {
		cin >> n >> m;
		graph.assign(n, vi ());
		visited.assign(n, 0);
		
		for (int i=0; i<m; i++) {
			cin >> a >> b;
			graph[a-1].push_back(b-1);
		}

		is_circuit = false;
		
		for (int i=0; i<n; i++) {
			if (!visited[i])
				dfs(i);
			if (is_circuit) break;
		}

		if (is_circuit) cout << "SIM" << endl;
		else cout << "NAO" << endl;

		visited.clear();
		graph.clear();
	}
}