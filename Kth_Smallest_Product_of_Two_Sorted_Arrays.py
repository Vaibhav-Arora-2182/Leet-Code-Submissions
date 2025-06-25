from typing import List


class Solution:
    """
    Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k,
    return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
    """

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1.sort()
        nums2.sort()

        negatives1 = [x for x in nums1 if x < 0]
        positives1 = [x for x in nums1 if x > 0]
        zero_count1 = len(nums1) - len(negatives1) - len(positives1)

        negatives2 = [x for x in nums2 if x < 0]
        positives2 = [x for x in nums2 if x > 0]
        zero_count2 = len(nums2) - len(negatives2) - len(positives2)

        # Search range based on min and max possible products
        min_product = min(
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        )
        max_product = max(
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        )

        def count_pairs_leq(target, arr1, arr2):
            """Count pairs (a,b) with a in arr1, b in arr2 and a*b <= target."""
            count = 0
            j = len(arr2) - 1
            for a in arr1:
                while j >= 0 and a * arr2[j] > target:
                    j -= 1
                count += j + 1
            return count

        def count_products_leq(x):
            count = 0
            if x < 0:
                # Only negative products can be <= x (negative threshold)
                # Count negative1 * positive2 pairs <= x
                count += count_pairs_leq(x, negatives1, positives2[::-1])
                # Count positive1 * negative2 pairs <= x
                count += count_pairs_leq(x, positives1[::-1], negatives2)
            else:
                # All negative * positive products are <= x since x >= 0
                count += len(negatives1) * len(positives2) + len(positives1) * len(
                    negatives2
                )

                # Products with zeros (zero * anything = 0 <= x if x >= 0)
                count += zero_count1 * (len(negatives2) + len(positives2) + zero_count2)
                count += zero_count2 * (len(negatives1) + len(positives1))

                # For positive products (negative*negative and positive*positive)
                if x > 0:
                    count += count_pairs_leq(x, negatives1[::-1], negatives2[::-1])
                    count += count_pairs_leq(x, positives1, positives2)
            return count

        low, high = min_product, max_product
        while low < high:
            mid = (low + high) // 2
            if count_products_leq(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low
