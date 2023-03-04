#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int n;
string str;

bool check(int m) {
  unordered_map<string, int> cnt;
  for (int i = 0; i + m <= n; i++) {
    string cur = str.substr(i, m);
    if (++cnt[cur] > 1)
      return false;
  }

  return true;
}

int main() {
  cin >> n >> str;
  int l = 1, r = n;
  while (l < r) {
    int mid = l + r >> 1;
    if (check(mid))
      r = mid;
    else
      l = mid + 1;
  }

  cout << l << endl;

  return 0;
}
