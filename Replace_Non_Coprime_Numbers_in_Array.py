import math
import time
from typing import List


class Solution:
    """

    Problem:
    - Given an array nums, repeatedly replace adjacent non-coprime numbers with their LCM
      until no more replacements are possible.
    - Return the final modified array.

    Approach:
    - Maintain a result list `ans` and a `curr` pointer.
    - Iterate through nums:
        - If curr and next number are non-coprime, merge them into LCM.
        - Keep merging with the last element of ans if still non-coprime.
        - Otherwise, push curr to ans and move on.
    - At the end, push final curr to ans.
    - This avoids unnecessary stack growth and is very efficient.

    Complexity:
    - Time: O(n log M) where M = max(nums[i]) due to gcd/lcm computations.
    - Space: O(n) for ans list.
    """

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        curr = nums[0]
        for x in nums[1:]:
            if math.gcd(curr, x) > 1:
                curr = curr * x // math.gcd(curr, x)
                while ans:
                    g = math.gcd(curr, ans[-1])
                    if g == 1:
                        break
                    curr = curr * ans.pop() // g
            else:
                ans.append(curr)
                curr = x
        ans.append(curr)
        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [6, 4, 3, 2, 7, 6, 2], "ans": [12, 7, 6]},
        {"nums": [2, 2, 1, 1, 3, 3, 3], "ans": [2, 1, 1, 3]},
        {"nums": [5, 10, 15], "ans": [30]},
        {"nums": [7, 13, 19], "ans": [7, 13, 19]},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.replaceNonCoprimes(**params)
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
