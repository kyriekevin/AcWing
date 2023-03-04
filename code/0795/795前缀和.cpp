#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int g[N];
int n, m;

int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    int x;
    cin >> x;
    g[i] = g[i - 1] + x;
  }
  while (m--) {
    int l, r;
    cin >> l >> r;
    cout << g[r] - g[l - 1] << endl;
  }

  return 0;
}
