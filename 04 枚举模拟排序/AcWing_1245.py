def main():
    n = int(input())
    
    def is_valid(x: int) -> bool:
        while x > 0:
            t = x % 10
            if t in (2, 0, 1, 9):
                return True
            x //= 10
        return False
    
    s = 0
    for i in range(1, n + 1):
        if is_valid(i):
            s += i
    
    print(s)
    

if __name__ == "__main__":
    main()
