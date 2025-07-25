import time
from typing import List


class Solution:
    """
    You are given an integer array nums.

    You can delete any number of elements from nums (without making it empty).
    After deletions, choose a subarray of nums such that:
        - All elements are unique
        - The sum is maximized

    Return the maximum sum of such a subarray.

    This is equivalent to finding the maximum sum of a subset of unique elements.

    Example:
    Input: nums = [4,2,4,5,6]
    Output: 17
    Constraints:
    1 <= nums.length <= 100
    -100 <= nums[i] <= 100
    """

    def maxSum(self, nums: List[int]) -> int:
        mn = float("-inf")
        seen = set()
        sum_ = 0

        for val in nums:
            if val not in seen:
                seen.add(val)
                if val >= 0:
                    sum_ += val
                else:
                    mn = max(mn, val)

        if sum_ == 0 and 0 not in seen:
            return mn

        return sum_


if __name__ == "__main__":
    testcases = {
        "test1": {"nums": [4, 2, 4, 5, 6], "ans": 17},
        "test2": {"nums": [-1, -2, -3], "ans": -1},
        "test3": {"nums": [-20, 20], "ans": 20},
        "test4": {"nums": [0, -5, -3], "ans": 0},
        "test5": {"nums": [1, 1, 1, 1], "ans": 1},
        "test6": {"nums": [1, 2, 3, 4, 5], "ans": 15},
        "test7": {"nums": [0, 0, 0], "ans": 0},
        "test8": {"nums": [-2, -2, -2], "ans": -2},
    }

    solution = Solution()
    for name, tc in testcases.items():
        start = time.perf_counter()
        params = {k: v for k, v in tc.items() if k != "ans"}

        result = solution.maxSum(**params)
        end = time.perf_counter()

        expected = tc["ans"]
        assert (
            result == expected
        ), f"{name} failed:\nExpected: {expected}\nGot: {result}"
        print(f"{name} passed in {(end - start) * 1000:.3f} ms.")
