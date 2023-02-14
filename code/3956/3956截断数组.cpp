#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int g[N];

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    int x;
    cin >> x;
    g[i] = g[i - 1] + x;
  }

  if (g[n] % 3)
    puts("0");
  else {
    long long res = 0, cnt = 0;
    for (int i = 2; i < n; i++) {
      if (g[i - 1] == g[n] / 3)
        cnt++;
      if (g[i] == g[n] / 3 * 2)
        res += cnt;
    }
    cout << res << endl;
  }

  return 0;
}
