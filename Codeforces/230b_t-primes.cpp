#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

#define MAX 1000000

int main() {
  // crivo de eratostenes
  vector<bool> eh_prime(MAX, true);
  eh_prime[0] = false;
  eh_prime[1] = false;

  for (ll i=0; i<=MAX; i++) {
    if (eh_prime[i]) {
      for (ll j=i*i; j<=MAX; j+=i) {
        eh_prime[j] = false;
      }
    }
  }

  // entrada e saida
  int n;
  ll x;
  cin >> n;

  for (int i=0; i<n; i++) {
    cin >> x;
    // verifica se raiz é inteiro
    if (x != 1000000000000) {
      ld raiz_d = sqrt(x);
      int raiz_l = raiz_d;
      ld dif = raiz_d - raiz_l;
      if (dif == 0 && eh_prime[raiz_l]) {
        cout << "YES" << endl;
      } else {
        cout << "NO" << endl;
      }
    } else {
      cout << "NO" << endl;
    }
  }

  return 0;
}