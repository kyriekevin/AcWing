#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1e5 + 10;
int g[N], n, m;

int quick_select(int s, int e, int k) {
	if (s >= e)
		return g[s];
	
	int x = g[s], l = s - 1, r = e + 1;
	while (l < r) {
		while (g[++l] < x);
		while (g[--r] > x);
		if (l < r)
			swap(g[l], g[r]);
	}

	if (r - s + 1 >= k)
		return quick_select(s, r, k);
	else return quick_select(r + 1, e, k - (r - s + 1));
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> g[i];
	cout << quick_select(0, n - 1, m) << endl;

	return 0;
}
