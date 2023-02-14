#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  int days = 0, date = 0;
  while (n) {
    days++;
    if (!date && n % 3 == 1)
      date = days;
    n -= (n + 2) / 3;
  }

  cout << days << " " << date << endl;

  return 0;
}
