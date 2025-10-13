import time
from typing import List


class Solution:
    """
    You are given a list of words.
    Repeatedly remove any word that is an anagram of the previous one until no more can be removed.

    Approach:
    - Use a stack to simulate the process:
        • For each word, compute its sorted form.
        • If the top of the stack has the same sorted form (anagram), pop it and push current only once.
        • Otherwise, push the current word.
    - This ensures that only non-anagram-adjacent words remain.
    - Time complexity: O(n * k log k), where k = average word length.
    """

    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        prev_sorted = ""
        for word in words:
            curr_sorted = "".join(sorted(word))
            if curr_sorted != prev_sorted:
                stack.append(word)
                prev_sorted = curr_sorted
        return stack


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "words": ["abba", "baba", "bbaa", "cd", "cd"],
            "ans": ["abba", "cd"],
        },
        {
            "words": ["a", "b", "c", "d", "e"],
            "ans": ["a", "b", "c", "d", "e"],
        },
        {
            "words": ["ab", "ba", "abc", "cab", "cba", "xyz"],
            "ans": ["ab", "abc", "xyz"],
        },
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.removeAnagrams(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        expected = test_case["ans"]
        if ans != expected:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {expected}, Got: {ans}\n"
                f"Input: {test_case['words']} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
