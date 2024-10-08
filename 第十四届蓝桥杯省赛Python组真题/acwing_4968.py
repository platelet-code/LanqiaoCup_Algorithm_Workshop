def phi(n: int) -> int:
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

def quick_mod(a: int, b: int, c: int) -> int:
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % c
        a = a * a % c
        b >>= 1
    return ans


def main():
    a, b = map(int, input().split())
    mod = 998244353
    ans = quick_mod(a, b - 1, mod) % mod * phi(a) % mod
    print(ans if a > 1 else 0)


if __name__ == "__main__":
    main()
