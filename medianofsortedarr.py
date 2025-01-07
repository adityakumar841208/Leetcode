class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merging two sorted arrays
        merged_array = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1

        # Add remaining elements from nums1 or nums2
        while i < len(nums1):
            merged_array.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged_array.append(nums2[j])
            j += 1
        
        # Finding the median
        n = len(merged_array)
        if n % 2 == 0:  # Even length
            median = (merged_array[n // 2] + merged_array[n // 2 - 1]) / 2
        else:  # Odd length
            median = merged_array[n // 2]
        
        return median

# Test the function
li1 = [3, 5]
li2 = [2, 4, 7]
solution = Solution()
median = solution.findMedianSortedArrays(li1, li2)
print("Median is:", median)
