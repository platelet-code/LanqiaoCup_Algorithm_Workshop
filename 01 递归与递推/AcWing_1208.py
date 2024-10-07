def main():
    s1 = input()
    s2 = input()
    
    cnt = 0
    s2_list = list(s2)
    for i in range(len(s1) - 1):
        if s1[i] != s2_list[i]:
            s2_list[i] = s1[i]
            s2_list[i + 1] = '*' if s2_list[i + 1] == 'o' else 'o'
            cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    main()
