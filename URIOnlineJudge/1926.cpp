#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define MAX 1000000

vector<ll> sieve_eratostenes() {
  vector<bool> is_prime(MAX, true);
  vector<ll> twin_prime(MAX, 0);
  is_prime[0] = false;
  is_prime[1] = false;

  for (ll i=2; i<=MAX; i++) {
    if (is_prime[i]) {
      for (ll j=i*i; j<=MAX; j+=i) {
        is_prime[j] = false;
      }
      if (is_prime[i-2]) {
        twin_prime[i] = 1;
        twin_prime[i-2] = 1;
      }
    }
  }
  return twin_prime;
}

vector<ll> cumulative_sum(vector<ll> const &v) {
  vector<ll> out(MAX, 0);
  out[0] = v[0];
  for (ll i=1; i<v.size(); i++) {
    out[i] = (v[i] + out[i-1]);
  }
  return out;
}

int main() {
  vector<ll> twin_primes = sieve_eratostenes();
  vector<ll> sum_primes = cumulative_sum(twin_primes);

  int q, x, y;
  scanf("%d", &q);
  for (int i=0; i<q; i++) {
    scanf("%d %d", &x, &y);

    if (y < x) {
      int aux = x;
      x = y;
      y = aux;
    }

    int n = sum_primes[y] - (sum_primes[x-1]);
    printf("%d\n", n);
  }

  return 0;
}