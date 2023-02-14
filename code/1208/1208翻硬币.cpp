#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

void change(char &ch) {
	if (ch == '*') ch = 'o';
	else ch = '*';
}

int main() {
	string start, end;
	cin >> start >> end;

	int res = 0;
	for (int i = 0; i + 1 < start.size(); i++) {
		if (start[i] != end[i]) {
			res++;
			change(start[i]);
			change(start[i + 1]);
		}
	}

	cout << res << endl;
		
	return 0;
}
