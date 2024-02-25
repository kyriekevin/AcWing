#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

typedef long long ll;

int main() {
  ll n;
  cin >> n;

  int res = 0;
  for (ll i = 2; i * i <= n; i++) {
    if (n % i == 0) {
      while (n % i == 0)
        n /= i;
      res++;
    }
  }

  if (n > 1)
    res++;
  cout << res << endl;

  return 0;
}
