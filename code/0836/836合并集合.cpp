#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1e5 + 10;
int p[N];
int n, m;

int find(int x) {
	if (p[x] != x)
		p[x] = find(p[x]);
	
	return p[x];
}

int main() {
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		p[i] = i;

	while (m--) {
		char op;
		int a, b;
		cin >> op >> a >> b;
		a = find(a), b = find(b);
		if (op == 'M') {
			if (a != b)
				p[a] = b;
		}
		else {
			if (a == b) puts("Yes");
			else puts("No");
		}
	}

	return 0;
}
