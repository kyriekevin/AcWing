#include <iostream>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

const int N = 10;
int dx[] = {-1, 0, 1, 0}, dy[] = {0, -1, 0, 1};
int g[N][N];
int n, m, k;
set<int> res;

void dfs(int x, int y, int u, int cur) {
	if (u > k) {
		res.insert(cur);
		return;
	}
	cur = 10 * cur + g[x][y];
	for (int i = 0; i < 4; i++) {
		int a = x + dx[i], b = y + dy[i];
		if (a < 0 || a >= n || b < 0 || b >= m)
			continue;
		dfs(a, b, u + 1, cur);
	}
}

int main() {
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> g[i][j];

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			dfs(i, j, 0, 0);

	cout << res.size() << endl;

	return 0;
}
