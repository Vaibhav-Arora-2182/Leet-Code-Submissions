import time
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    """
    Given head, a reference to the first node of a singly‑linked list whose node
    values are bits (0 or 1), the list represents a binary number with the most
    significant bit at the head.

    Return that number’s decimal (base‑10) value.
    """

    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num


def list_to_linked(bits: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for b in bits:
        cur.next = ListNode(b)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        {"head": [1, 0, 1], "ans": 5},
        {"head": [0], "ans": 0},
        {"head": [1, 1, 1, 1], "ans": 15},
        {"head": [1, 0, 0, 0, 0, 0], "ans": 32},
    ]

    for i, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        params["head"] = list_to_linked(params["head"])
        result = sol.getDecimalValue(**params)
        end = time.time()
        elapsed = (end - start) * 1000
        if result == test_case["ans"]:
            print(f"Test Case {i + 1} Passed (Time: {elapsed:.2f} ms)")
        else:
            print(f"Test Case {i + 1} Failed (Time: {elapsed:.2f} ms)")
            print(f"Expected: {test_case['ans']}, Got: {result}")
            print(f"Expected: {test_case['ans']}, Got: {result}")
