import time
from typing import List


class Solution:
    """
    You are given a social network of m users with friendships.
    Each user knows some languages (1..n). Two users can communicate
    if they share a language. You can pick one language to teach to
    some users so that all friendships can communicate.
    Return the minimum number of users you need to teach.
    """

    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        """
        Approach:
        1. Identify friendships where users do NOT share a common language.
        2. Collect all users involved in such problematic friendships.
        3. For each language, count how many of these users already know it.
        4. Answer = len(need_teaching) - max(users who already know a language).
        """
        m = len(languages)

        lang_sets = [set(langs) for langs in languages]

        need_teaching = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            if lang_sets[u].isdisjoint(lang_sets[v]):
                need_teaching.add(u)
                need_teaching.add(v)

        if not need_teaching:
            return 0

        best = float("inf")
        for lang in range(1, n + 1):
            know_count = sum(1 for user in need_teaching if lang in lang_sets[user])
            best = min(best, len(need_teaching) - know_count)

        return best


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "n": 2,
            "languages": [[1], [2], [1, 2]],
            "friendships": [[1, 2], [1, 3], [2, 3]],
            "ans": 1,
        },
        {
            "n": 3,
            "languages": [[2], [1, 3], [1, 2], [3]],
            "friendships": [[1, 4], [1, 2], [3, 4], [2, 3]],
            "ans": 2,
        },
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.minimumTeachings(**params)
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
