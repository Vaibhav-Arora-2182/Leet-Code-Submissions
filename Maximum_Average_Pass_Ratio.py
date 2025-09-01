import heapq
import time
from typing import List


class Solution:
    """
    You are given `classes`, a list of [passi, totali] for each class, and `extraStudents`
    brilliant students who are guaranteed to pass.

    Goal:
    Assign the extra students to maximize the average pass ratio across all classes.

    The pass ratio of a class = passi / totali.
    The average pass ratio = (sum of all class pass ratios) / number of classes.

    Return the maximum possible average pass ratio after assigning all extraStudents.
    """

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        Approach:
        - Use a greedy strategy with a max-heap.
        - For each class, compute the "gain" in pass ratio if we add one more passing student:
            gain = (p+1)/(t+1) - p/t
        - Always assign the next extra student to the class with the maximum gain.
        - Repeat until all extraStudents are assigned.
        - Finally, compute the new average pass ratio.

        Complexity:
        - Heap push/pop is O(log n).
        - We assign `extraStudents` one by one.
        - Total complexity = O((n + extraStudents) * log n), which is efficient for constraints.
        """
        heap = []

        for p, t in classes:
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-gain, p, t))

        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-gain, p, t))

        total = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t

        return total / len(classes)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "classes": [[1, 2], [3, 5], [2, 2]],
            "extraStudents": 2,
            "ans": 0.78333,
        },
        {
            "classes": [[2, 4], [3, 9], [4, 5], [2, 10]],
            "extraStudents": 4,
            "ans": 0.53485,
        },
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}

        start = time.time()
        ans = sol.maxAverageRatio(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if abs(ans - test_case["ans"]) > 1e-5:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
