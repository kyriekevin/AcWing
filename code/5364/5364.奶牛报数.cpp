#include <iostream>
using namespace std;

const int N = 2e5 + 10;
int s[N];

int main() {
  int n, l, r;

  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> s[i];
    s[i + n] = s[i];
  }

  for (int i = 1; i <= 2 * n; i++)
    s[i] += s[i - 1];

  cin >> l >> r;

  int len = r - l, sum = 0, res = 0;
  for (int i = len; i <= 2 * n; i++) {
    int x = s[i] - s[i - len], y = r - i;
    while (y < 1)
      y += n;
    if (x > sum || x == sum && y < res) {
      sum = x;
      res = y;
    }
  }

  cout << res << endl;

  return 0;
}
