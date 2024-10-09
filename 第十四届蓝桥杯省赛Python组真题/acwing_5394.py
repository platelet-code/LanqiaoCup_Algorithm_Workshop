import sys

def minimal_ones_manacher(s):
    n = len(s)
    m = n * 2 + 1
    
    p = ['!'] * (m + 2)
    Len = [0] * (m + 2)
    pre = [0] * (m + 2)
    
    for i in range(1, m, 2):
        p[i] = '#'
        p[i + 1] = s[i // 2]
    p[m] = '#'
    p[m + 1] = '@'
    
    center, right = 0, 0
    for i in range(1, m + 1):
        pre[i] = pre[i - 1] + (1 if p[i] == '1' else 0)
        Len[i] = min(right - i, Len[2 * center - i]) if right > i else 1
        while p[i + Len[i]] == p[i - Len[i]]:
            Len[i] += 1
        if Len[i] + i > right:
            right, center = Len[i] + i, i
    
    total_ones = pre[m]
    min_ones = 10 ** 9
    
    for i in range(1, m + 1):
        if p[i] == '1':
            continue
        palindrome_ones = pre[i + Len[i] - 1] - pre[i - Len[i]]
        min_ones = min(min_ones, total_ones - palindrome_ones // 2)
    return min_ones


def main():
    input_string = sys.stdin.readline().strip()
    result = minimal_ones_manacher(input_string)
    print(result)


if __name__ == "__main__":
    main()
