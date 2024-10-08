from collections import defaultdict

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = defaultdict(int)
    
    for num in a:
        if num <= 10 ** 5:
            freq[num] += 1
    
    for i in range(1, 10**5 + 1):
        if freq[i] % (i + 1) != 0:
            print(i)
            break
        freq[i + 1] += freq[i] // (i + 1)
        
    else:
        print(min(a))

if __name__ == "__main__":
    main()
