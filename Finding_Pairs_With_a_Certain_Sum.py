import collections
import time
from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = collections.Counter(nums2)
        self.freq1 = collections.Counter(nums1)
        self.keys = sorted(self.freq1.keys())  

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]
        self.freq2[new_val] += 1
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        ans = 0
        for num1 in self.freq1:
            num2 = tot - num1
            ans += self.freq1[num1] * self.freq2.get(num2, 0)
        return ans


if __name__ == "__main__":
    # Leetcode style input simulation
    methods = ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
    args = [
        [[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]],
        [7],
        [3, 2],
        [8],
        [4],
        [0, 1],
        [1, 1],
        [7],
    ]
    expected_outputs = [None, 8, None, 2, 1, None, None, 11]

    obj = None
    for i, (method, arg) in enumerate(zip(methods, args)):
        start = time.time()

        if method == "FindSumPairs":
            obj = FindSumPairs(*arg)
            output = None
        elif method == "add":
            obj.add(*arg)
            output = None
        elif method == "count":
            output = obj.count(*arg)

        end = time.time()
        elapsed = (end - start) * 1000

        if output != expected_outputs[i]:
            print(
                f"Test {i+1} failed: Method = {method}, Args = {arg}, "
                f"Expected = {expected_outputs[i]}, Got = {output} (Time: {elapsed:.2f} ms)"
            )
        else:
            print(
                f"Test {i+1} passed: Method = {method}, Output = {output} (Time: {elapsed:.2f} ms)"
            )
