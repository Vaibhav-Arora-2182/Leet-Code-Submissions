import heapq
import time
from typing import List


class Solution:
    """
    You are given a 0-indexed integer array nums consisting of 3 * n elements.

    You are allowed to remove any subsequence of elements of size exactly n from nums.
    The remaining 2 * n elements will be divided into two equal parts:

    The first n elements belonging to the first part and their sum is sumfirst.
    The next n elements belonging to the second part and their sum is sumsecond.
    The difference in sums of the two parts is denoted as sumfirst - sumsecond.

    Return the minimum difference possible between the sums of the two parts after the removal of n elements.
    """

    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total = len(nums)

        # left[i] stores the minimum sum of n elements in nums[0:i+1]
        left = [0] * total
        max_heap = []
        curr_sum = 0

        for i in range(total):
            heapq.heappush(max_heap, -nums[i])
            curr_sum += nums[i]

            if len(max_heap) > n:
                curr_sum += heapq.heappop(max_heap)

            if len(max_heap) == n:
                left[i] = curr_sum

        # right[i] stores the maximum sum of n elements in nums[i:]
        right = [0] * total
        min_heap = []
        curr_sum = 0

        for i in range(total - 1, -1, -1):
            heapq.heappush(min_heap, nums[i])
            curr_sum += nums[i]

            if len(min_heap) > n:
                curr_sum -= heapq.heappop(min_heap)

            if len(min_heap) == n:
                right[i] = curr_sum

        # Try all valid splits where n elements are removed
        res = float("inf")
        for i in range(n - 1, 2 * n):
            res = min(res, left[i] - right[i + 1])

        return res


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        {"nums": [3, 1, 2], "ans": -1},
        {"nums": [7, 9, 5, 8, 1, 3], "ans": 1},
    ]

    for i, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        result = sol.minimumDifference(**params)
        end = time.time()
        elapsed = (end - start) * 1000
        if result == test_case["ans"]:
            print(f"Test Case {i + 1} Passed (Time: {elapsed:.2f} ms)")
        else:
            print(f"Test Case {i + 1} Failed (Time: {elapsed:.2f} ms)")
            print(f"Input: {params['nums']}")
            print(f"Expected: {test_case['ans']}, Got: {result}")
