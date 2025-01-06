class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of both arrays
        i, j, k = m - 1, n - 1, m + n - 1

        # Compare elements from the back and place the larger one in nums1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements are left in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Test the function
solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]  # Example nums1 with enough space for nums2
m = 3  # Number of initialized elements in nums1
nums2 = [2, 5, 6]  # Example nums2
n = 3  # Number of elements in nums2

solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
