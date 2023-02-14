#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int h[N], w[N];
int n, k;

bool check(int x) {
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    cnt += (h[i] / x) * (w[i] / x);
    if (cnt >= k)
      return true;
  }

  return false;
}

int main() {
  cin >> n >> k;
  for (int i = 0; i < n; i++)
    cin >> h[i] >> w[i];

  int l = 1, r = 1e5;
  while (l < r) {
    int mid = l + r + 1 >> 1;
    if (check(mid))
      l = mid;
    else
      r = mid - 1;
  }

  cout << l << endl;

  return 0;
}
