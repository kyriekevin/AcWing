n = int(input())

for _ in range(n):
    s = input()
    max_len, cur_len, last_ch, res = 0, 0, '', ''
    for ch in s:
        if ch == last_ch:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                res = last_ch
            cur_len = 1
            last_ch = ch
    if cur_len > max_len:
        max_len = cur_len
        res = last_ch

    print(res, max_len)

