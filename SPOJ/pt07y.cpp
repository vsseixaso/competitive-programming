#include <bits/stdc++.h>
 
using namespace std;
 
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
 
vi graph[10001];
bool visited[10001];
bool is_circuit = false;
int counter = 0;
 
void dfs(int current, int previous) {
	visited[current] = true;
	counter++;
	for (int i=0; i<graph[current].size(); i++) {
		if(!visited[graph[current][i]]) {
			dfs(graph[current][i], current);
		} else if (graph[current][i] != previous) {
			is_circuit = true;
		}
	}
}
 
int main() {
	int n, m, u, v = 0;
	
	scanf("%d %d", &n, &m);
 
	for (int i=0; i<m; i++) {
		scanf("%d %d", &u, &v);
		graph[u].push_back(v);
        graph[v].push_back(u);
	}
 
	dfs(u, -1);
 
	if (counter != n || is_circuit) {
		printf("%s\n", "NO");
	} else {
		printf("%s\n", "YES");
	}
 
	return 0;
} 