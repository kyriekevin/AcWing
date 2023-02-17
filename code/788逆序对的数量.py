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
