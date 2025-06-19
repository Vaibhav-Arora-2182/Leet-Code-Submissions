from typing import List


class Solution:
    """
    You are given an integer array nums and an integer k.
    You may partition nums into one or more subsequences such that,
    each element in nums appears in exactly one of the subsequences.

    Return the minimum number of subsequences needed such that,
    the difference between the maximum and minimum values in each subsequence is at most k.

    A subsequence is a sequence that can be derived from another sequence by,
    deleting some or no elements without changing the order of the remaining elements.
    """

    def partitionArray(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))
        nums = sorted(list(set(nums)))
        ans = 0
        prev = -1
        for num in nums:
            if num > prev:
                prev = num
                ans += 1
                prev += k
            else:
                continue
        return ans
