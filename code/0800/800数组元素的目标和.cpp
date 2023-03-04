#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int a[N], b[N];
int n, m, x;

int main() {
  cin >> n >> m >> x;
  for (int i = 0; i < n; i++)
    cin >> a[i];

  for (int i = 0; i < m; i++)
    cin >> b[i];

  for (int i = 0, j = m - 1; i < n && j >= 0;) {
    if (a[i] + b[j] == x) {
      cout << i << " " << j << endl;
      break;
    } else if (a[i] + b[j] > x)
      j--;
    else
      i++;
  }

  return 0;
}
