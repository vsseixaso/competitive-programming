#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, m, a, b;
    scanf("%d%d%d%d", &n, &m, &a, &b);

    if (m * a > b) {
        int count = (n % m) * a;
        if (count > b) {
          printf("%d\n", n / m * b + b);
        } else {
          printf("%d\n", n / m * b + count);
        }
    } else {
        printf("%d\n", n * a);
    }

    return 0;
}