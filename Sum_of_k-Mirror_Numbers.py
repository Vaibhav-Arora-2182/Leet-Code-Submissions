class Solution:
    """
    A k-mirror number is a positive integer without leading zeros that
    reads the same both forward and backward in base-10 as well as in base-k.

    For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively,
    which read the same both forward and backward.
    On the contrary, 4 is not a 2-mirror number.
    The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
    Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
    """

    def kMirror(self, k: int, n: int) -> int:

        def to_base_k(x: int) -> str:
            # Convert number to base k string
            digits = []
            while x > 0:
                digits.append(str(x % k))
                x //= k
            return "".join(digits[::-1]) if digits else "0"

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        result = []
        length = 1

        while len(result) < n:
            # Generate palindromes of length `length`
            # Half length for building palindrome
            half_len = (length + 1) // 2

            start = 10 ** (half_len - 1)
            end = 10**half_len

            for half in range(start, end):
                half_str = str(half)
                if length % 2 == 0:
                    # even length palindrome: mirror entire half
                    pal_str = half_str + half_str[::-1]
                else:
                    # odd length palindrome: mirror all but last char
                    pal_str = half_str + half_str[-2::-1]

                pal_num = int(pal_str)
                base_k_str = to_base_k(pal_num)

                if is_palindrome(base_k_str):
                    result.append(pal_num)
                    if len(result) == n:
                        break

            length += 1

        return sum(result)
