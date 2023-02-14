#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
  string str;
  int res = 0;
  cin >> str;

  for (int i = 0; i + 1 < str.size(); i++) {
    char a = str[i], b = str[i + 1];
    if (a == b || a == '?' || b == '?') {
      res++;
      i++;
    }
  }

  cout << res << endl;

  return 0;
}
