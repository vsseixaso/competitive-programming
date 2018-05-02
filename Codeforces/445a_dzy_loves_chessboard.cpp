#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m;
    char aux;

    cin >> n >> m;

    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            cin >> aux;
            if(aux == '.') {
                if ((i+j)%2 == 0)
                    cout << 'W';
                else
                    cout << 'B';
            } else {
                cout << aux;
            }
        }
        cout << "\n";
    }

    return 0;
}