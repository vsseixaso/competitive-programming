#include <bits/stdc++.h>

using namespace std;

int main(){
	string s;
    while(cin >> s){
        list<char> t;
        auto i = t.begin();
        for(auto it = s.begin(); it != s.end(); it++){
            if(*it == '['){
                i = t.begin();
            }else if(*it == ']'){
                i = t.end();
            }else{
                t.insert(i,*it);
            }
        }
        for(auto it = t.begin(); it != t.end(); it++){
            cout << *it;
        }
        cout << endl;
    }
    return 0;
}