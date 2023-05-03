#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	vector<int> odd, even;
	for (int i = 0; i < 10; i++) {
		int x;
		cin >> x;
		if (x % 2) odd.push_back(x);
		else even.push_back(x);
	}

	sort(odd.begin(), odd.end());
	sort(even.begin(), even.end());

	for (int i = odd.size() - 1; i >= 0; i--)
		cout << odd[i] << " ";

	for (int i = 0; i < even.size(); i++)
		cout << even[i] << " ";

	return 0;
}
