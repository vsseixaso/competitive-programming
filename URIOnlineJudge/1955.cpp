#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vector<int>> vvi;

bool dfs(vvi &graph, vi &colors, int node, int color) {
  if (colors[node] != -1) {
    return colors[node] == color;
  }
  colors[node] = color;

  for (int i = 0; i < graph.size(); i++) {
    if (graph[node][i] == 0) {
      if (!dfs(graph, colors, i, (color+1)%2)) {
        return false;
      }
    }
  }
  return true;
}

int main() {
  int n;
  
  scanf("%d", &n);

  vvi graph(n, vi(n));
  vi colors(n, -1);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      scanf("%d", &graph[i][j]);
    }
  }

  for (int i = 0; i < n; i++) {
    if (colors[i] == -1) {
      if (!dfs(graph, colors, i, 0)) {
        cout << "Fail!" << endl;
        return 0;
      }
    }
  }

  cout << "Bazinga!" << endl;
  return 0;
}