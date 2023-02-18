if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        b = [0] * (n + 10)
        arr = [0] + list(map(int, input().split()))
        for i in range(1, n + 1):
            x = min(arr[i], i)
            l, r = i - x + 1, i
            b[l] += 1
            b[r + 1] -= 1

        for i in range(1, n + 1):
            b[i] += b[i - 1]
            if b[i]:
                print(1, end=" ")
            else:
                print(0, end=" ")

        print()
        
