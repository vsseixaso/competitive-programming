#include <bits/stdc++.h>
 
using namespace std;
 
#define INF 100000001
 
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
 
vector<vii> graph;
vi dist;
 
int dijkstra(int s, int d) {
	priority_queue<int> q;
	fill(dist.begin(), dist.end(), INF);
	dist[s] = 0;
	q.push(s);
 
	while(!q.empty()) {
		int node = q.top();
		q.pop();
 
		for(int i=0; i<graph[node].size(); i++) {
			int nNode = (graph[node][i]).first;
			int nNodeWeight = (graph[node][i]).second;
 
			if(dist[nNode] > dist[node] + nNodeWeight) {
				q.push(nNode);
				dist[nNode] = dist[node] + nNodeWeight;
			}
		}
	}
 
	return dist[d];
}
 
int main() {
	int t, n, m, s, d, x, y, w;
 
	scanf("%d", &t);
	while(t--) {
		scanf("%d %d", &n, &m);
		
		graph.clear();
		graph.resize(n);
		dist.clear();
		dist.resize(n);
		
		for(int i=0; i<m; i++) {
			scanf("%d %d %d", &x, &y, &w);
 
			graph[x-1].push_back(make_pair(y-1, w));
		}
 
		scanf("%d %d", &s, &d);
 
		int res = dijkstra(s-1, d-1);
		if(res == INF)
			printf("NO\n");
		else
			printf("%d\n", res);
	}
 
	return 0;
} 
