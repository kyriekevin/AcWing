#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 20;
bool st[N];
int T, n;

struct plane {
	int t, d, l;
} p[N];

bool dfs(int u, int last) {
	if (u == n) return true;

	for (int i = 0; i < n; i++) {
		int t = p[i].t, d = p[i].d, l = p[i].l;
		if (!st[i] && t + d >= last) {
			st[i] = true;
			if (dfs(u + 1, max(last, t) + l))
				return true;
			st[i] = false;
		}
	}

	return false;
}

int main() {
	cin >> T;
	while (T--) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			int t, d, l;
			cin >> t >> d >> l;
			p[i] = {t, d, l};
		}

		memset(st, 0, sizeof st);
		if (dfs(0, 0)) puts("YES");
		else puts("NO");
	}

	return 0;
}
