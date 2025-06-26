class Solution:
    """
    You are given a binary string s and a positive integer k.

    Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

    Note:

    - The subsequence can contain leading zeroes.
    - The empty string is considered to be equal to 0.
    - A subsequence is a string that can be derived from another string by
        deleting some or no characters without changing the order of the remaining characters.
    """

    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        value = 0
        power = 0
        count = 0

        # Start from the right (least significant bit)
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                count += 1  # always include '0'
            else:
                # try to include '1' if within bounds
                if power < 32 and value + (1 << power) <= k:
                    value += 1 << power
                    count += 1
                # else, skip this '1'
            power += 1

        return count
