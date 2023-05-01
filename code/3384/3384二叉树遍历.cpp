#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

string str;
int k;

void dfs() {
	if (str[k] == '#') {
		k++;
		return;
	}

	char ch = str[k++];
	dfs();
	cout << ch << " ";
	dfs();
}

int main() {
	cin >> str;
	dfs();

	return 0;
}
