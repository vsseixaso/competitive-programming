#include <bits/stdc++.h>

#define INF 10000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;

vector<vii> graph;
vector<int> dist;

int n, m;

void dijkstra(int x) {
	dist.clear();
	dist.assign(m * m + 2, INF);
	dist[x] = 0;
	
	priority_queue<ii, vii, greater<ii>> pq;
	
	pq.push(ii(0, x));
	
	while(!pq.empty()) {
		ii v = pq.top();
		pq.pop();
				
		for (int i=0; i<graph[v.second].size(); i++) {
			if (dist[graph[v.second][i].second] > dist[v.second] + 1) {
				dist[graph[v.second][i].second] = dist[v.second] + 1;
				pq.push(ii(dist[graph[v.second][i].second], graph[v.second][i].second));
			}
		}
	}
}
int main() {
	vector<string> aux;
	string x;
	
	char c;
	ios_base :: sync_with_stdio(0); cin.tie(0);
	
	while(true) {
		cin >> n >> m;
		if (!n && !m) return 0;
		graph.assign(m * m + 2, vii ());
		
		for (int i=0; i<n; i++) {
			cin >> x;
			aux.push_back(x);
		}
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (aux[i][j] == '.') {
					if (i > 0) {
						if (aux[i-1][j] == '.') {
							graph[m * i + j].push_back(make_pair(1, m * (i - 1) + j));
						}
					}
					if (i < n-1) {
						if (aux[i+1][j] == '.') {
							graph[m * i + j].push_back(make_pair(1, m * (i + 1) + j));
						}
					}
					if (j > 0) {
						if (aux[i][j-1] == '.') {
							graph[m * i + j].push_back(make_pair(1, m * i + j - 1));
						}
					}
					if (j < m-1) {
						if (aux[i][j+1] == '.') {
							graph[m * i + j].push_back(make_pair(1, m * i + j + 1));
						}
					}
				}
			}
		}

		int p;
		
		for (p=0; p<graph.size(); p++) if (graph[p].size()) break;
		dijkstra(p);
		int max = INT_MIN;
		for (int i=0; i<dist.size(); i++) {
			if (dist[i] != INF && dist[i] > max) max = dist[i], p = i;
		}
		dijkstra(p);
		max = INT_MIN;
		for (int i=0; i<dist.size(); i++) {
			if (dist[i] != INF && dist[i] > max) max = dist[i];
		}
		
		cout << max << '\n';
		
		graph.clear();		
		aux.clear();
	}
	
}