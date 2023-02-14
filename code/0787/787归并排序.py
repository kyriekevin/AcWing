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
