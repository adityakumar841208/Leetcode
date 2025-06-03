class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        
        # Pointer for nums1 and nums2
        p1, p2 = m - 1, n - 1
        # Pointer for the end of nums1
        p = m + n - 1
        
        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
            
        # No need to copy remaining elements from nums1, they are already in place
    
solution = Solution()
print(solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))  # Example input to test the function
        