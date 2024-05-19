#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int l, r, x;
  cin >> l >> r >> x;
  if (l <= x && x <= r)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;

  return 0;
}
