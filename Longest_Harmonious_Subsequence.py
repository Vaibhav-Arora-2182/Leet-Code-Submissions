from collections import Counter
from typing import List


class Solution:
    """
    We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

    Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

    """

    def __init__(self):
        pass

    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])

        return max_len


if __name__ == "__main__":
    test_cases = [
        {"nums": [1, 3, 2, 2, 5, 2, 3, 7], "ans": 5},
        {"nums": [1, 2, 3, 4], "ans": 2},
        {"nums": [1, 1, 1, 1], "ans": 0},
    ]
    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        ans = sol.findLHS(test_case["nums"])
        if ans != test_case["ans"]:
            print(f"Test Case - {ind + 1} failed, \nTest Case = {test_case}")
        else:
            print(f"Test Case - {ind + 1} passed")
            print(f"Test Case - {ind + 1} passed")
