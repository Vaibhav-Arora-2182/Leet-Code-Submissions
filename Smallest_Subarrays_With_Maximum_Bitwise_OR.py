# git add . && git commit -m "Smallest Subarrays With Maximum Bitwise OR" && git push
from typing import List
import time

class Solution:
    """
    You are given a 0-indexed array nums of length n, consisting of non-negative integers. 
    For each index i from 0 to n - 1, determine the size of the minimum sized non-empty subarray 
    of nums starting at i (inclusive) that has the maximum possible bitwise OR.

    In other words, let Bij be the bitwise OR of the subarray nums[i...j]. 
    You need to find the smallest subarray starting at i, such that bitwise OR of this subarray 
    is equal to max(Bik) where i <= k <= n - 1.

    The bitwise OR of an array is the bitwise OR of all the numbers in it.

    Return an integer array answer of size n where answer[i] is the length of the minimum sized 
    subarray starting at i with maximum bitwise OR.

    Constraints:
        - n == nums.length
        - 1 <= n <= 10^5
        - 0 <= nums[i] <= 10^9
    """

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        last = [0] * 32  # store the last index where bit i is seen
        for i in range(n - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    last[b] = i
            max_len = 1
            for idx in last:
                if idx != 0:
                    max_len = max(max_len, idx - i + 1)
            answer[i] = max_len
        return answer

# Sample test runner with timing and param unpacking
if __name__ == "__main__":
    t0 = time.time()
    solution = Solution()
    testcases = [
        {
            "nums": [1, 0, 2, 1, 3],
            "ans": [3, 3, 2, 2, 1],
        },
        {
            "nums": [1, 2],
            "ans": [2, 1],
        },
        {
            "nums": [0, 0, 0, 0],
            "ans": [1, 1, 1, 1],
        },
        {
            "nums": [7, 7, 7],
            "ans": [1, 1, 1],
        },
    ]

    for i, tc in enumerate(testcases):
        params = {k: v for k, v in tc.items() if k != "ans"}
        got = solution.smallestSubarrays(**params)
        expect = tc["ans"]
        assert got == expect, f"Test case {i+1} failed: got {got}, expected {expect}"

    print(f"All test cases passed in {time.time() - t0:.6f} seconds.")

