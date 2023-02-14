#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
  int n, res = 0, cnt = 0;
  string str;

  cin >> n >> str;

  for (int i = 0; i < str.size(); i++) {
    if (str[i] == 'x')
      cnt++;
    else
      cnt = 0;
    if (cnt >= 3)
      cnt -= 1, res += 1;
  }

  cout << res << endl;

  return 0;
}
