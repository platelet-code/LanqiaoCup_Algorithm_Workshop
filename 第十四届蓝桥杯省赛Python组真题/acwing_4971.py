def count_nodes(n: int, m: int, k: int) -> int:
    count = 0
    current_start = k
    current_end = k

    while current_start <= n:
        count += min(current_end, n) - current_start + 1
        
        next_start = m * (current_start - 1) + 2
        next_end = m * current_end + 1

        current_start = next_start
        current_end = next_end

    return count


def main():
    T = int(input())
    for _ in range(T):
        n, m, k = map(int, input().split())
        print(count_nodes(n, m, k))


if __name__ == "__main__":
    main()
