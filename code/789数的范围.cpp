#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int g[N];
int n, q;

int main() {
  cin >> n >> q;
  for (int i = 0; i < n; i++)
    cin >> g[i];
  while (q--) {
    int x;
    cin >> x;
    int l = 0, r = n - 1;
    while (l < r) {
      int mid = l + r >> 1;
      if (g[mid] >= x)
        r = mid;
      else
        l = mid + 1;
    }

    if (g[l] != x)
      puts("-1 -1");
    else {
      cout << l << " ";
      r = n - 1;
      while (l < r) {
        int mid = l + r + 1 >> 1;
        if (g[mid] <= x)
          l = mid;
        else
          r = mid - 1;
      }
      cout << l << endl;
    }
  }

  return 0;
}
