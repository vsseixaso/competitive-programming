#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef set<int> si;

int main() {
    int n, x, y, count = 0, sum[2000] = {}, sub[2000] = {};
    cin >> n;
    
    for(int i = 0; i < n; i++) {
        cin >> x >> y;
        sum[x + y]++;
        sub[x - y + 1000]++;
    }
    
    for(int i = 0; i < 2000; i++) {
            count += (sum[i] * (sum[i] - 1) / 2);
            count += (sub[i] * (sub[i] - 1) / 2);
    }
    
    cout << count << endl;
    
    return 0;
}