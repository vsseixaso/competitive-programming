#include <bits/stdc++.h>

using namespace std;
 int main () {
   int n, count;
   int v[10001];

   while (cin >> n and n) {
     while (cin >> v[0] and v[0]) {
       for (int i=1; i<n; i++) {
         cin >> v[i];
       }

       stack<int> s;
       count = 0;

       for (int i=1; i<=n; i++) {
         s.push(i);

         while (s.size() > 0 && v[count] == s.top()) {
           count++;
           s.pop();
         }
       }

       cout << ((s.size() == 0) ? "Yes" : "No") << endl;
     }
     cout << endl;
   }

   return 0;
 }
