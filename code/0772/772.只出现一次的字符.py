s = input()
cnt = [0] * 26

for ch in s:
    cnt[ord(ch) - ord('a')] += 1

for ch in s:
    if cnt[ord(ch) - ord('a')] == 1:
        print(ch)
        break
else:
    print('no')
