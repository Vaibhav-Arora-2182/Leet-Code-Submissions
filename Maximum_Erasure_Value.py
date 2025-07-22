import time
from typing import List


class Solution:
    """
    You are given an array of positive integers `nums` and want to erase a subarray containing only unique elements.

    The score you get by erasing the subarray is equal to the **sum of its elements**.

    Return the **maximum score** you can get by erasing exactly one subarray.

    A subarray is a contiguous part of the array.

    Example 1:
    Input: nums = [4,2,4,5,6]
    Output: 17
    Explanation: The optimal subarray is [2,4,5,6].

    Example 2:
    Input: nums = [5,2,1,2,5,2,1,2,5]
    Output: 8
    Explanation: The optimal subarray is [5,2,1] or [1,2,5].
    """

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)

        return max_sum


# Test cases and runner
if __name__ == "__main__":
    testcases = {
        "Example 1": {
            "nums": [4, 2, 4, 5, 6],
            "ans": 17,
        },
        "Example 2": {
            "nums": [5, 2, 1, 2, 5, 2, 1, 2, 5],
            "ans": 8,
        },
        "All Unique": {
            "nums": [1, 2, 3, 4, 5],
            "ans": 15,
        },
        "All Same": {
            "nums": [3, 3, 3],
            "ans": 3,
        },
        "Long Repeats": {
            "nums": [1, 2, 3, 4, 1, 2, 3, 4, 5],
            "ans": 15,
        },
        "Edge Single": {
            "nums": [10],
            "ans": 10,
        },
    }

    solution = Solution()
    for name, tc in testcases.items():
        start = time.perf_counter()
        params = {k: v for k, v in tc.items() if k != "ans"}
        result = solution.maximumUniqueSubarray(**params)
        end = time.perf_counter()

        expected = tc["ans"]
        assert (
            result == expected
        ), f"{name} failed:\nExpected: {expected}\nGot: {result}"
        print(f"{name} passed in {(end - start) * 1000:.3f} ms.")
