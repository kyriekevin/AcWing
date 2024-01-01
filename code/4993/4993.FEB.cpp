#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  string str;
  cin >> str;

  if (str == string(n, 'F')) {
    cout << n << endl;
    for (int i = 0; i < n; i++)
      cout << i << endl;

    return 0;
  }

  int l = 0, r = n - 1;
  while (str[l] == 'F')
    l++;
  while (str[r] == 'F')
    r--;

  int low = 0, high = 0;
  auto s = str;

  for (int i = l; i <= r; i++) {
    if (s[i] == 'F') {
      if (s[i - 1] == 'B')
        s[i] = 'E';
      else
        s[i] = 'B';
    }
    if (i > l && s[i] == s[i - 1])
      low++;
  }

  s = str;
  for (int i = l; i <= r; i++) {
    if (s[i] == 'F')
      s[i] = s[i - 1];
    if (i > l && s[i] == s[i - 1])
      high++;
  }

  int ends = l + n - 1 - r, d = 2;
  if (ends) {
    high += ends;
    d = 1;
  }

  cout << (high - low) / d + 1 << endl;
  for (int i = low; i <= high; i += d)
    cout << i << endl;

  return 0;
}
