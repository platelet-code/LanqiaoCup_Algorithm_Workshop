def main():
    n = int(input())
    A = list(map(int, input().split()))
    
    first = {}
    pair = None
    
    for i in range(n):
        x = A[i]
        j = 2
        
        while j * j <= x:
            if x % j == 0:
                if j in first:
                    if pair is None or (first[j], i) < pair:
                        pair = first[j], i
                else:
                    first[j] = i
                
                while x % j == 0:
                    x //= j
            j += 1
        
        if x > 1:
            if x in first:
                if pair is None or (first[x], i) < pair:
                    pair = first[x], i
            else:
                first[x] = i
        
    print(pair[0] + 1, pair[1] + 1)
            
    
if __name__ == "__main__":
    main()
