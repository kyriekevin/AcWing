#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int g[N], cnt[N];
int n;

int main() {
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> g[i];

  int res = 0;
  for (int i = 0, j = 0; i < n; i++) {
    cnt[g[i]]++;
    while (cnt[g[i]] > 1)
      cnt[g[j++]]--;
    res = max(i - j + 1, res);
  }

  cout << res << endl;

  return 0;
}
