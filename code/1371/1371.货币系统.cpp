#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

const int N = 10010, M = 30;
long long f[M][N];

int main() {
  int n, m;
  cin >> n >> m;

  f[0][0] = 1;
  for (int i = 1; i <= n; i++) {
    int v;
    cin >> v;
    for (int j = 0; j <= m; j++) {
      f[i][j] = f[i - 1][j];
      if (j >= v) f[i][j] += f[i][j - v];
    }
  }

  cout << f[n][m] << endl;

  return 0;
}
