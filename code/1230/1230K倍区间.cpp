#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

typedef long long LL;

const int N = 1e5 + 10;
LL g[N], cnt[N];
int n, k;

int main() {
  cin >> n >> k;
  for (int i = 1; i <= n; i++) {
    cin >> g[i];
    g[i] += g[i - 1];
  }

  LL res = 0;
  cnt[0] = 1;
  for (int i = 1; i <= n; i++) {
    res += cnt[g[i] % k];
    cnt[g[i] % k]++;
  }

  cout << res << endl;

  return 0;
}
