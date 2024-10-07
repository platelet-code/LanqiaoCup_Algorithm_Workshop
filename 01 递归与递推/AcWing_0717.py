from functools import lru_cache

def main():
    @lru_cache(None)
    def fib(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)
    
    n = int(input())
    result = (fib(i) for i in range(n))
    
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
