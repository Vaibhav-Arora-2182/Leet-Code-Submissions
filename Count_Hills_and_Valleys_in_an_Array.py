import time
from typing import List


class Solution:
    """
    You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest
    non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums
    if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of
    the same hill or valley if nums[i] == nums[j].

    Note: For an index to be part of a hill or valley, it must have a non-equal neighbor on both the left
    and right of the index.

    Return the number of hills and valleys in nums.
    """

    def countHillValley(self, nums: List[int]) -> int:
        filtered = [nums[0]]
        for num in nums[1:]:
            if num != filtered[-1]:
                filtered.append(num)

        count = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1  # Hill
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1  # Valley

        return count


if __name__ == "__main__":
    tcs = [
        {"nums": [2, 4, 1, 1, 6, 5], "ans": 3},
        {"nums": [6, 6, 5, 5, 4, 1], "ans": 0},
        {"nums": [1, 2, 2, 2, 1], "ans": 1},
        {"nums": [1, 2, 3, 2, 1, 2, 3], "ans": 2},
    ]

    sol = Solution()
    for i, tc in enumerate(tcs, 1):
        params = {k: v for k, v in tc.items() if k != "ans"}
        start = time.time()
        res = sol.countHillValley(**params)
        end = time.time()
        print(
            f"Test Case {i}: {'passed' if res == tc['ans'] else 'failed'} | Expected: {tc['ans']} | Got: {res} | Time: {end - start:.6f}s"
        )
