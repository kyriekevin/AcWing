if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(" ".join([str(x) for x in sorted([i for i in arr if i % 2], reverse=True)] + [str(x) for x in sorted([i for i in arr if i % 2 == 0])]))
