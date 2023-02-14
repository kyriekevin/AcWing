#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 10;
int g[N];
bool st[N];
int n;

void dfs(int u) {
  if (u == n) {
    for (int i = 0; i < n; i++)
      cout << g[i] << " ";
    puts("");
    return;
  }

  for (int i = 1; i <= n; i++) {
    if (!st[i]) {
      g[u] = i;
      st[i] = true;
      dfs(u + 1);
      st[i] = false;
    }
  }
}

int main() {
  cin >> n;
  dfs(0);

  return 0;
}
