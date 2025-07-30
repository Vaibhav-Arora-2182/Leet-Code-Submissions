from typing import List
import time

class Solution:
    """
    You are given an integer array nums of size n.
    Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

    In other words, let k be the maximum value of the bitwise AND of any subarray of nums.
    Then, only subarrays with a bitwise AND equal to k should be considered.
    Return the length of the longest such subarray.

    The bitwise AND of an array is the bitwise AND of all the numbers in it.
    A subarray is a contiguous sequence of elements within an array.

    Constraints:
        - 1 <= nums.length <= 10^5
        - 1 <= nums[i] <= 10^6
    """

    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_len = cur_len = 0
        for num in nums:
            if num == max_val:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
        return max_len

if __name__ == "__main__":
    t0 = time.time()
    solution = Solution()
    testcases = [
        {
            "nums": [1, 2, 3, 3, 2, 2],
            "ans": 2,
        },
        {
            "nums": [1, 2, 3, 4],
            "ans": 1,
        },
    ]

    for i, tc in enumerate(testcases):
        params = {k: v for k, v in tc.items() if k != "ans"}
        got = solution.longestSubarray(**params)
        expect = tc["ans"]
        assert got == expect, f"Test case {i+1} failed: got {got}, expected {expect}"

    print(f"All test cases passed in {time.time() - t0:.6f} seconds.")
