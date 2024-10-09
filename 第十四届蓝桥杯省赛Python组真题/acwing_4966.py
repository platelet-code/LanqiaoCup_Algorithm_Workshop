def main():
    s = input()
    ans = 0
    i = 0
    
    while i < len(s) - 1:
        if s[i] == s[i + 1] or s[i] == "?" or s[i + 1] == "?":
            i += 2
            ans += 1
        else:
            i += 1
    
    print(ans)

if __name__ == "__main__":
    main()
