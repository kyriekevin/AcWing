# merge sort
[##](##) AcWing 787
[787归并排序](https://www.acwing.com/problem/content/description/789/)
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
int g[N], temp[N];
int n;

void merge_sort(int s, int e) {
  if (s >= e)
    return;
  int mid = s + e >> 1;
  merge_sort(s, mid);
  merge_sort(mid + 1, e);

  int i = s, j = mid + 1, k = 0;
  while (i <= mid && j <= e) {
    if (g[i] < g[j])
      temp[k++] = g[i++];
    else
      temp[k++] = g[j++];
  }

  while (i <= mid)
    temp[k++] = g[i++];
  while (j <= e)
    temp[k++] = g[j++];

  for (int i = s, j = 0; i <= e && j <= k; i++, j++)
    g[i] = temp[j];
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> g[i];
  merge_sort(0, n - 1);
  for (int i = 0; i < n; i++)
    cout << g[i] << " ";

  return 0;
}
```

```
python3
```

```python3
def merge_sort(g, s, e):
    if s >= e:
        return
    mid = s + e >> 1
    merge_sort(g, s, mid)
    merge_sort(g, mid + 1, e)
    i, j = s, mid + 1
    temp = []
    while i <= mid and j <= e:
        if g[i] < g[j]:
            temp.append(g[i])
            i += 1
        else:
            temp.append(g[j])
            j += 1

    temp += g[i: mid + 1]
    temp += g[j: e + 1]
    g[s: e + 1] = temp

if __name__ == "__main__":
    n = int(input())
    g = list(map(int, input().split()))
    merge_sort(g, 0, n - 1)
    print(" ".join(map(str, g)))
```

## AcWing 788

[788逆序对的数量](https://www.acwing.com/problem/content/790/)
---

```
cpp
```

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

const int N = 1e5 + 10;
int g[N], temp[N];
int n;

LL msort(int s, int e) {
	if (s >= e) return 0;
	int mid = s + e >> 1;
	LL res = msort(s, mid) + msort(mid + 1, e);

	int i = s, j = mid + 1, k = 0;
	while (i <= mid && j <= e) {
		if (g[i] <= g[j])
			temp[k++] = g[i++];
		else {
			res += mid - i + 1;
			temp[k++] = g[j++];
		}
	}

	while (i <= mid) temp[k++] = g[i++];
	while (j <= e) temp[k++] = g[j++];

	for (int i = s; i <= e; i++)
		g[i] = temp[i - s];	

	return res;
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> g[i];
	
	cout << msort(0, n - 1) << endl;

	return 0;
}
```

```
python3
```

```python3
def msort(g, s, e):
    if s >= e:
        return 0
    
    mid = s + e >> 1
    res = msort(g, s, mid) + msort(g, mid + 1, e)

    i, j = s, mid + 1
    temp = []
    while i <= mid and j <= e:
        if g[i] <= g[j]:
            temp.append(g[i])
            i += 1
        else:
            res += mid - i + 1
            temp.append(g[j])
            j += 1 

    temp += g[i: mid + 1]
    temp += g[j: e + 1]
    g[s: e + 1] = temp

    return res

if __name__ == "__main__":
    n = int(input())
    g = list(map(int, input().split()))
    print(msort(g, 0, n -1))
```
