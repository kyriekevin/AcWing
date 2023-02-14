# quick sort
## AcWing 785

[785.快速排序](https://www.acwing.com/problem/content/787/)
---
```
cpp
```

```cpp
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int g[N];
int n;

void quick_sort(int s, int e) {
  if (s >= e)
    return;
  int x = g[(s + e) / 2], l = s - 1, r = e + 1;
  while (l < r) {
    while (g[++l] < x)
      ;
    while (g[--r] > x)
      ;
    if (l < r)
      swap(g[l], g[r]);
  }

  quick_sort(s, r);
  quick_sort(r + 1, e);
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> g[i];

  quick_sort(0, n - 1);

  for (int i = 0; i < n; i++)
    cout << g[i] << " ";

  return 0;
}
```

```
python3
```

```python3
def quick_sort(g, s, e):
    if s >= e:
        return
    x, l, r = g[(s + e) // 2], s - 1, e + 1
    while l < r:
        while True:
            l += 1
            if g[l] >= x:
                break
        while True:
            r -= 1
            if g[r] <= x:
                break
        if l < r:
            g[l], g[r] = g[r], g[l]

    quick_sort(g, s, r)
    quick_sort(g, r + 1, e)

if __name__ == "__main__":
    n = int(input())
    g = list(map(int, input().split()))
    quick_sort(g, 0, n - 1)
    print(" ".join(map(str, g)))
```

## AcWing 786

[786第k个数](https://www.acwing.com/problem/content/description/788/)---

```
cpp
```

```cpp
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
```

```
python3
```

```python3
def quick_select(g, s, e, k):
    if s >= e:
        return g[s]
    x, l, r = g[s], s - 1, e + 1
    while l < r:
        while True:
            l += 1
            if g[l] >= x:
                break
        while True:
            r -= 1
            if g[r] <= x:
                break
        if l < r:
            g[l], g[r] = g[r], g[l]

    if r - s + 1 >= k:
        return quick_select(g, s, r, k)
    else:
        return quick_select(g, r + 1, e, k - (r - s + 1))

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = list(map(int, input().split()))
    print(quick_select(g, 0, n - 1, m))
```
