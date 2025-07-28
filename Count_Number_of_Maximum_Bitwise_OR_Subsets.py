import time
from typing import List


class Solution:
    """
    Given an integer array nums, find the maximum possible bitwise OR of a subset of nums
    and return the number of different non-empty subsets with the maximum bitwise OR.

    An array a is a subset of an array b if a can be obtained from b by deleting some
    (possibly zero) elements of b. Two subsets are considered different if the indices
    of the elements chosen are different.

    The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        count = 0

        def dfs(i: int, curr: int):
            nonlocal count
            if i == len(nums):
                if curr == max_or:
                    count += 1
                return
            # Include nums[i]
            dfs(i + 1, curr | nums[i])
            # Exclude nums[i]
            dfs(i + 1, curr)

        dfs(0, 0)
        return count


# Test Runner
if __name__ == "__main__":
    tcs = [
        {"nums": [3, 1], "ans": 2},
        {"nums": [2, 2, 2], "ans": 7},
        {"nums": [1, 1, 1], "ans": 7},
        {"nums": [1, 2, 4, 8], "ans": 1},
    ]

    sol = Solution()
    for i, tc in enumerate(tcs, 1):
        params = {k: v for k, v in tc.items() if k != "ans"}
        start = time.time()
        res = sol.countMaxOrSubsets(**params)
        end = time.time()
        status = "Passed" if res == tc["ans"] else "Failed"
        print(
            f"Test Case {i}: {status} | Expected: {tc['ans']} | Got: {res} | Time: {end - start:.6f}s"
        )
