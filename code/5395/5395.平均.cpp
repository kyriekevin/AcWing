#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

typedef long long LL;

const int N = 1e5 + 10;
vector<int> w[N];

int main() {
  int n;
  cin >> n;

  for (int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    w[a].push_back(b);
  }

  LL res = 0;
  int avg = n / 10;
  for (int i = 0; i < 10; i++) {
    if (w[i].size() > avg) {
      sort(w[i].begin(), w[i].end());
      for (int j = 0; j < w[i].size() - avg; j++)
        res += w[i][j];
    }
  }

  cout << res << endl;

  return 0;
}
