from typing import List
from bisect import bisect_left

def lengthOfLIS(arr: List[int]) -> int:
    tails = []
    for x in arr:
        idx = bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(lengthOfLIS(nums))
