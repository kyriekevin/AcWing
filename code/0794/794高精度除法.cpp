#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> div(vector<int> &A, int b, int &r) {
	vector<int> C;
	r = 0;
	for (int i = A.size() - 1; i >= 0; i--) {
		r = r * 10 + A[i];
		C.push_back(r / b);
		r %= b;
	}

	reverse(C.begin(), C.end());
	while (C.size() > 1 && C.back() == 0)
		C.pop_back();
	
	return C;
}

int main() {
	string a;
	int B, r;
	cin >> a >> B;

	vector<int> A, C;
	for (int i = a.size() - 1; i >= 0; i--)
		A.push_back(a[i] - '0');

	C = div(A, B, r);
	for (int i = C.size() - 1; i >= 0; i--)
		cout << C[i];

	cout << endl << r << endl;

	return 0;
}
