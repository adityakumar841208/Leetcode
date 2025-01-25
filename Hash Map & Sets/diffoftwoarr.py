# class Solution:
#     def findDifference(self, nums1, nums2):
#         ans1 = []
#         ans2 = []
        
#         for i in nums1:
#             if i not in nums2:
#                 ans1.append(i)
#         for i in nums2:
#             if i not in nums1:
#                 ans2.append(i)
#         return list([ans1, ans2])
        
    
# solution = Solution()
# print(solution.findDifference([1,2,3,4,5], [1,2,3,4]))

# optimised solution

def findDifference(nums1, nums2):
    # Create dictionaries to track presence
    nums1_dict = {}
    nums2_dict = {}

    # Populate dictionaries
    for num in nums1:
        nums1_dict[num] = True
    for num in nums2:
        nums2_dict[num] = True

    # Find unique elements using dictionary keys
    only_in_nums1 = [num for num in nums1_dict if num not in nums2_dict]
    only_in_nums2 = [num for num in nums2_dict if num not in nums1_dict]

    return [only_in_nums1, only_in_nums2]

# Example usage
nums1 = [1, 2, 3, 3]
nums2 = [3, 4, 5, 5]
print(findDifference(nums1, nums2))
