import time
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        You are given an integer array nums and a positive integer k.

        A subsequence `sub` of `nums` with length x is called **valid** if it satisfies:
            (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.

        Return the length of the longest valid subsequence of nums.

        Example 1:
        Input: nums = [1,2,3,4,5], k = 2
        Output: 5
        Explanation: The longest valid subsequence is [1, 2, 3, 4, 5].

        Example 2:
        Input: nums = [1,4,2,3,1,4], k = 3
        Output: 4
        Explanation: The longest valid subsequence is [1, 4, 1, 4].

        Constraints:
        - 2 <= nums.length <= 10^3
        - 1 <= nums[i] <= 10^7
        - 1 <= k <= 10^3
        """
        n = len(nums)
        max_len = 1

        for val in range(k):
            dp = [0] * k
            for x in nums:
                mod_x = x % k
                target = (val - mod_x + k) % k
                dp[mod_x] = max(dp[mod_x], dp[target] + 1)
            max_len = max(max_len, max(dp))

        return max_len


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 2, 3, 4, 5], "k": 2, "expected": 5},
        {"nums": [1, 4, 2, 3, 1, 4], "k": 3, "expected": 4},
        {"nums": [1, 3], "k": 5, "expected": 2},
        {"nums": [1, 1, 1, 1], "k": 2, "expected": 4},
        {"nums": [1, 2, 1, 2, 1, 2], "k": 3, "expected": 6},
    ]

    for i, tc in enumerate(test_cases, 1):
        start = time.time()
        result = sol.maximumLength(tc["nums"], tc["k"])
        elapsed = (time.time() - start) * 1000
        status = "Passed" if result == tc["expected"] else "Failed"
        print(f"Test Case {i}: {status} (Time: {elapsed:.2f} ms)")
        if status == "Failed":
            print(f"  Input nums : {tc['nums']}")
            print(f"  Input k    : {tc['k']}")
            print(f"  Expected   : {tc['expected']}")
            print(f"  Got        : {result}")
            print(f"  Got        : {result}")
