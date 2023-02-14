#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1e5 + 10;
int g[N];
int n, res;
string str;

int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> str;
		int l = str[0] - '0', r = str[str.size() - 1] - '0';
		int f = max(1, g[l] + 1);
		g[r] = max(g[r], f);
		res = max(res, f);
	}

	cout << n - res << endl;

	return 0;
}
