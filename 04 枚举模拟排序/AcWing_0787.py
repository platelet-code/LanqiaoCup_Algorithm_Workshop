from typing import List

def merge_sort(l: int, r: int, q: List[int]) -> None:
    if l == r:
        return
    
    mid = (l + r) // 2
    merge_sort(l, mid, q)
    merge_sort(mid + 1, r, q)
    
    merged = []
    i, j = l, mid + 1
    for _ in range(l, r + 1):
        if j > r or (i <= mid and q[i] <= q[j]):
            merged.append(q[i])
            i += 1
        else:
            merged.append(q[j])
            j += 1
    
    q[l:r+1] = merged


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    merge_sort(0, n - 1, nums)
    print(" ".join(map(str, nums)))


if __name__ == "__main__":
    main()
