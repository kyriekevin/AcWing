#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int N = 150010;
int p[N], sz[N], d[N];
int n, m;

int find(int x) {
  if (p[x] != x)
    p[x] = find(p[x]);
  return p[x];
}

bool check() {
  for (int i = 1; i <= n; i++) {
    if (p[i] == i) {
      if (d[i] != (sz[i] - 1ll) * sz[i])
        return false;
    }
  }
  return true;
}

int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    p[i] = i;
    sz[i] = 1;
  }

  while (m--) {
    int a, b;
    cin >> a >> b;
    a = find(a), b = find(b);
    d[a]++, d[b]++;
    if (a != b) {
      d[b] += d[a];
      sz[b] += sz[a];
      p[a] = b;
    }
  }

  if (check())
    puts("YES");
  else
    puts("NO");

  return 0;
}
