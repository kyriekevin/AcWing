#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int max(int x, int y) {
  return x > y ? x : y;
}

int main() {
  int a, b;
  cin >> a >> b;
  cout << max(a, b) << endl;

  return 0;
}
