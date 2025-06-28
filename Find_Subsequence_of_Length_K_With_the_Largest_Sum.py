import heapq
from typing import List


class Solution:
    """
    You are given an integer array nums and an integer k.
    You want to find a subsequence of nums of length k that has the largest sum.

    Return any such subsequence as an integer array of length k.

    A subsequence is an array that can be derived from another array by
        deleting some or no elements without changing the order of the remaining elements.
    """

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove smallest

        top_k = sorted(heap, key=lambda x: x[1])

        return [num for num, idx in top_k]
