def main():
    n, capacity = map(int, input().split())
    f = [0] * (capacity + 1)
    
    items = []
    for _ in range(n):
        v, w = map(int, input().split())
        items.append((v, w))
    
    for v, w in items:
        for j in range(capacity, v - 1, -1):
            f[j] = max(f[j], f[j - v] + w)
    
    print(max(f))


if __name__ == "__main__":
    main()
