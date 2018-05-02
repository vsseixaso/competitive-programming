#include <bits/stdc++.h>

using namespace std;
 
typedef vector<int> vi;

int counter = 0;
 
void dfs(int x, vi graph[], bool visited[]) {
    visited[x] = true;
     counter++;
    for(auto i = 0; i < graph[x].size(); i++) {
        if(!visited[graph[x][i]]) {
            dfs(graph[x][i], graph, visited);
        }
    }
}
 
int main() {
    int n, m, a, b, e;
 
    while (scanf("%d %d", &n, &m) != EOF) {
        counter = 0;
        vi graph[1001];
        bool visited[1001];

        for(int i = 0; i < n; i++) {
            visited[i] = false;
        }
 
        for (int i = 0; i < m; i++) {
            scanf("%d %d", &a, &b);
            graph[a-1].push_back(b-1);
            graph[b-1].push_back(a-1);
        }
 
        scanf("%d", &e);
        dfs(e-1, graph, visited);
        printf("%d\n", counter);
    }

    return 0;
}
