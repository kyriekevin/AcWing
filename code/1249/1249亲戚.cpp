#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 2e4 + 10;
int p[N];

int find(int x) {
  if (p[x] != x)
    p[x] = find(p[x]);

  return p[x];
}

int main() {
  int n, m, q, a, b;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++)
    p[i] = i;

  while (m--) {
    scanf("%d%d", &a, &b);
    int pa = find(a), pb = find(b);
    if (pa != pb)
      p[pa] = pb;
  }

  scanf("%d", &q);
  while (q--) {
    scanf("%d%d", &a, &b);
    int pa = find(a), pb = find(b);
    if (pa != pb)
      puts("No");
    else
      puts("Yes");
  }

  return 0;
}
