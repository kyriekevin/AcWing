#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 55, M = 210;
int w[N], cnt[M];
int T, n;

int main() {
  cin >> T;
  while (T--) {
    cin >> n;
    memset(cnt, 0, sizeof cnt);
    for (int i = 0; i < n; i++) {
      cin >> w[i];
      cnt[w[i]]++;
    }

    int res = 0;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        res += cnt[w[i] + w[j]];
    cout << res << endl;
  }

  return 0;
}
