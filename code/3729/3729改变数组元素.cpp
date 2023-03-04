#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 2e5 + 10;
int b[N];
int n, T;

int main() {
  cin >> T;
  while (T--) {
    cin >> n;
    memset(b, 0, (n + 1) * 4);
    for (int i = 1; i <= n; i++) {
      int x;
      cin >> x;
      x = min(x, i);
      int l = i - x + 1, r = i;
      b[l]++, b[r + 1]--;
    }
    for (int i = 1; i <= n; i++) {
      b[i] += b[i - 1];
      cout << !!b[i] << " ";
    }
    puts("");
  }

  return 0;
}
