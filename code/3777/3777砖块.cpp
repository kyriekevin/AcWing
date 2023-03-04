#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

int T, n;
string s;

void update(char &c) {
  if (c == 'B')
    c = 'W';
  else
    c = 'B';
}

bool check(char c) {
  vector<int> res;
  string str = s;
  for (int i = 0; i + 1 < n; i++) {
    if (str[i] != c) {
      res.push_back(i);
      update(str[i]);
      update(str[i + 1]);
    }
  }

  if (str.back() != c)
    return false;

  cout << res.size() << endl;
  for (int x : res)
    cout << x + 1 << " ";
  if (res.size())
    cout << endl;

  return true;
}

int main() {
  cin >> T;
  while (T--) {
    cin >> n >> s;
    if (!check('B') && !check('W'))
      puts("-1");
  }

  return 0;
}
