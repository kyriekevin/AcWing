#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n, x;

int lowbit(int x) {
	return x & -x;
}

int main() {
	cin >> n;
	while (n--) {
		cin >> x;
		int res = 0;
		while (x) {
			x -= lowbit(x);
			res++;
		}
		cout << res << " ";
	}

	return 0;
}
