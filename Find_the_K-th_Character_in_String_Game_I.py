import time


class Solution:
    """
    Alice and Bob are playing a game. Initially, Alice has a string word = "a".

    You are given a positive integer k.

    Now Bob will ask Alice to perform the following operation forever:

    Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
    For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

    Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

    Note that the character 'z' can be changed to 'a' in the operation.
    """

    def kthCharacter(self, k: int) -> str:
        def shift_char(c, shift):
            return chr((ord(c) - ord("a") + shift) % 26 + ord("a"))

        def get_kth(k, shift):
            if k == 1:
                return shift_char("a", shift)
            half = 1
            while half * 2 < k:
                half *= 2
            if k <= half:
                return get_kth(k, shift)
            else:
                return get_kth(k - half, shift + 1)

        return get_kth(k, 0)


if __name__ == "__main__":
    test_cases = [{"k": 5, "ans": "b"}, {"k": 10, "ans": "c"}]
    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        ans = sol.kthCharacter(test_case["k"])
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed, \nTest Case = {test_case} (Time: {elapsed_ms:.2f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.2f} ms)")
