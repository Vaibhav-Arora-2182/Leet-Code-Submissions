import time


class Solution:
    """
    You are given an integer array nums and an integer k.

    You are allowed to perform the following operation on each element of the array at most once:
        - Add an integer in the range [-k, k] (inclusive) to that element.

    Your task is to maximize the number of distinct elements in nums after performing these operations.

    Example 1:
        Input: nums = [1,2,2,3,3,4], k = 2
        Output: 6
        Explanation:
            We can transform nums to [-1, 0, 1, 2, 3, 4], all distinct.

    Example 2:
        Input: nums = [4,4,4,4], k = 1
        Output: 3
        Explanation:
            By adding -1, 0, and +1 to some 4s, we can create [3, 4, 5, 4],
            resulting in 3 distinct values.
    """

    def max_distinct_after_operations(self, nums: list[int], k: int) -> int:
        """
        Approach:
        1. Sort the array `nums` to process elements in increasing order.
        2. Maintain a variable `last_picked` to store the last distinct value assigned.
           - Initialize it to a very small number.
        3. For each element `num`:
             - Its allowed range is [num - k, num + k].
             - If `last_picked < num - k`, we can safely pick `num - k`.
             - Otherwise, move to `last_picked + 1` to ensure distinctness.
             - If that chosen value is within the allowed range, count it as a valid distinct element.
        4. Return the total count of distinct elements.

        This greedy approach ensures we always pick the smallest valid value for each number,
        maximizing distinctness globally.

        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1)
        """
        nums.sort()
        last_picked = -(10**18)
        distinct_count = 0

        for num in nums:
            lower_bound = num - k
            upper_bound = num + k
            if last_picked < lower_bound:
                last_picked = lower_bound
            else:
                last_picked += 1
            if last_picked <= upper_bound:
                distinct_count += 1
            else:
                last_picked -= 1

        return distinct_count


if __name__ == "__main__":

    sol = Solution()

    test_cases = [
        {"nums": [1, 2, 2, 3, 3, 4], "k": 2, "ans": 6},
        {"nums": [4, 4, 4, 4], "k": 1, "ans": 3},
        {"nums": [10, 10, 10, 10, 10], "k": 0, "ans": 1},
        {"nums": [1, 2, 3, 4, 5], "k": 10, "ans": 5},
        {"nums": [1, 1, 1, 2, 2, 2], "k": 3, "ans": 6},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.max_distinct_after_operations(**params)
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
