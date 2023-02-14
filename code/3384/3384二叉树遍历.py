def dfs():
    global k 
    if s[k] == '#':
        k += 1
        return

    ch = s[k]
    k += 1

    dfs()
    print(ch, end=" ")
    dfs()

if __name__ == "__main__":
    k = 0
    s = input()
    dfs()
