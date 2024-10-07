def main():
    w, m, n = map(int, input().split())
    
    m -= 1
    n -= 1
    
    p1, p2 = divmod(m, w)
    p3, p4 = divmod(n, w)
    
    if p1 & 1:
        p2 = w - 1 - p2
    
    if p3 & 1:
        p4 = w - 1 - p4
        
    print(abs(p1 - p3) + abs(p2 - p4))


if __name__ == "__main__":
    main()
