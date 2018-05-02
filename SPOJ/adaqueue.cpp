#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
	int x, q;
	bool flag = true;
	deque<int> deq;
	string s;
 
	scanf("%d", &q);
	for (int i=0; i<q; i++) {
		cin >> s;
		
		if (s == "back") {
			if (deq.empty())	{
				cout << "No job for Ada?" << endl;
			} else if (flag) {
				cout << deq.back() << endl;
				deq.pop_back();
			} else {
				cout << deq.front() << endl;
				deq.pop_front();
			}
		} else if (s == "front") {
			if (deq.empty())	{
				cout << "No job for Ada?" << endl;
			} else if (flag) {
				cout << deq.front() << endl;
				deq.pop_front();
			} else {
				cout << deq.back() << endl;
				deq.pop_back();
			}
		} else if (s == "push_back") {
			cin >> x;
			if(flag) {
				deq.push_back(x);
			} else {
				deq.push_front(x);
			}
		} else if (s == "toFront") {
			cin >> x;
			if(flag) {
				deq.push_front(x);
			} else {
				deq.push_back(x);
			}
		} else if (s == "reverse") {
			flag = !flag;
		}
	}
 
	return 0;
} 