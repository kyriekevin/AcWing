#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int b[N];
int n, m;

void insert(int l, int r, int c) {
  b[l] += c;
  b[r + 1] -= c;
}

int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    int x;
    cin >> x;
    insert(i, i, x);
  }

  while (m--) {
    int l, r, c;
    cin >> l >> r >> c;
    insert(l, r, c);
  }

  for (int i = 1; i <= n; i++) {
    b[i] += b[i - 1];
    cout << b[i] << " ";
  }

  return 0;
}
