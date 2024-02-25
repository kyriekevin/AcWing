#include <algorithm>
#include <iostream>
using namespace std;

const int N = 110;
int g[N], n;

int main() {
  cin >> n;
  double tot = 4.5 * n;
  int s = 0, res = 0;
  for (int i = 0; i < n; i++) {
    cin >> g[i];
    s += g[i];
  }

  sort(g, g + n);
  for (int i = 0; s < tot; i++) {
    res += 1;
    s += 5 - g[i];
  }

  cout << res << endl;

  return 0;
}
