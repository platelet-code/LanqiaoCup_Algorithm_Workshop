def main():
    n = int(input())
    
    ret = n
    while n >= 3:
        ret += n // 3
        n = n // 3 + n % 3
    
    print(ret)


if __name__ == "__main__":
    main()
