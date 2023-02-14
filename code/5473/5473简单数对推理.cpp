#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
  unordered_map<int, int> cnt;
  for (int i = 0; i < 4; i++) {
    int x;
    cin >> x;
    if (++cnt[x] == 2) {
      cout << x << endl;
      break;
    }
  }

  return 0;
}
