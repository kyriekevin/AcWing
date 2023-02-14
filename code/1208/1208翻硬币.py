if __name__ == "__main__":
    start = list(input())
    end = list(input())

    res = 0
    for i in range(len(start) - 1):
        if start[i] != end[i]:
            res += 1
            start[i] = '*' if start[i] == 'o' else 'o'
            start[i + 1] = '*' if start[i + 1] == 'o' else 'o'
    print(res)
