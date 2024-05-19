#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

void work(set<int> &S, multiset<int> &M, int x) {
  auto i = S.lower_bound(x), j = i;
  j--;
  M.erase(M.find(*i - *j)), M.insert(*i - x), M.insert(x - *j);
  S.insert(x);
}

int main() {
  set<int> S1, S2;
  multiset<int> M1, M2;

  int w, h, n;
  cin >> w >> h >> n;

  S1.insert(0), S1.insert(w);
  S2.insert(0), S2.insert(h);
  M1.insert(w), M2.insert(h);

  while (n--) {
    string op;
    int x;
    cin >> op >> x;
    if (op == "X")
      work(S1, M1, x);
    else
      work(S2, M2, x);
    cout << (ll)*M1.rbegin() * *M2.rbegin() << endl;
  }

  return 0;
}
