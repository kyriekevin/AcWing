#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int g[N], temp[N];
int n;

void merge_sort(int s, int e) {
  if (s >= e)
    return;
  int mid = s + e >> 1;
  merge_sort(s, mid);
  merge_sort(mid + 1, e);

  int i = s, j = mid + 1, k = 0;
  while (i <= mid && j <= e) {
    if (g[i] < g[j])
      temp[k++] = g[i++];
    else
      temp[k++] = g[j++];
  }

  while (i <= mid)
    temp[k++] = g[i++];
  while (j <= e)
    temp[k++] = g[j++];

  for (int i = s, j = 0; i <= e && j <= k; i++, j++)
    g[i] = temp[j];
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> g[i];
  merge_sort(0, n - 1);
  for (int i = 0; i < n; i++)
    cout << g[i] << " ";

  return 0;
}
