#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int binarySearch(vi &v, int x){

    int beg, mid, end;
    beg = 0;
    end = v.size()-1;

    while (beg <= end) {
        mid = (beg+end)/2;
        if (v[mid] == x) {
            break;
        } else if (v[mid]>x) {
            end = mid - 1;
        } else {
            beg = mid + 1;
        }
    }

    if (v[mid] == x) {
        int out = mid;
        while(out-1 >= 0 && v[out-1] == x) {
            out--;
        }
        return out;
    }
    return -1;
}

int main(){
    int n, q, x, t=1;

    while(true){
    	cin >> n >> q;
    	if (n+q == 0) break;

        cout << "CASE# " << t++ << ":" << endl;

        vi v;
        for (int i=0; i<n; i++) {
            cin >> x;
            v.push_back(x);
        }

        sort(v.begin(), v.end());

        for (int i=0; i<q; i++) {
            cin >> x;
            int y = binarySearch(v,x);

            if(y >= 0)
                cout << x << " found at " << y+1 << endl;
            else
                cout << x << " not found" << endl;
        }
    }

    return 0;
}