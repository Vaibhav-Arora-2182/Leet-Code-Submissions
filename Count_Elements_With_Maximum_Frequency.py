import time
from collections import Counter
from typing import List


class Solution:
    """
    You are given an array nums consisting of positive integers.

    Return the total frequencies of elements in nums such that those elements
    all have the maximum frequency.

    The frequency of an element is the number of occurrences of that element in the array.

    Example 1:
    Input: nums = [1,2,2,3,1,4]
    Output: 4
    Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum
    frequency in the array. So the number of elements in the array with maximum frequency is 4.

    Example 2:
    Input: nums = [1,2,3,4,5]
    Output: 5
    Explanation: All elements of the array have a frequency of 1 which is the maximum.
    So the number of elements in the array with maximum frequency is 5.
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        Approach:
        - Use Counter to count the frequency of each element.
        - Find the maximum frequency value.
        - Sum all frequencies that are equal to this maximum.
        - Return the total sum.

        Time Complexity: O(n), where n = len(nums)
        Space Complexity: O(n) for the frequency map
        """
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(v for v in freq.values() if v == max_freq)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 2, 2, 3, 1, 4], "ans": 4},
        {"nums": [1, 2, 3, 4, 5], "ans": 5},
        {"nums": [7, 7, 7, 7], "ans": 4},
        {"nums": [5], "ans": 1},
        {"nums": [1, 1, 2, 2, 3, 3], "ans": 6},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.maxFrequencyElements(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
