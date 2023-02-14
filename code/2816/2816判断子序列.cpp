#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int a[N], b[N];
int n, m;

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    cin >> a[i];

  for (int i = 0; i < m; i++)
    cin >> b[i];

  int i = 0, j = 0;
  for (; i < n && j < m; j++) {
    if (a[i] == b[j])
      i++;
  }

  if (i == n)
    puts("Yes");
  else
    puts("No");

  return 0;
}
