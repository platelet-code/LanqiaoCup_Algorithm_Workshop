def find_missing_and_duplicate(numbers):
    n = len(numbers)
    number_set = set()
    duplicate = None
    total = 0

    for num in numbers:
        if num in number_set:
            duplicate = num
        else:
            number_set.add(num)
        total += num

    min_num = min(numbers)
    expected_sum = (min_num + min_num + n - 1) * n // 2
    missing = expected_sum - (total - duplicate)

    return missing, duplicate


if __name__ == "__main__":
    N = int(input())
    all_numbers = []
    for _ in range(N):
        all_numbers.extend(map(int, input().split()))
    
    missing, duplicate = find_missing_and_duplicate(all_numbers)
    print(missing, duplicate)
