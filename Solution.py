from typing import List

class Solution:
    def merge(self, 
                nums1: List[int],  # First sorted array
                m: int,            # Number of elements in nums1
                nums2: List[int],  # Second sorted array
                n: int):           # Number of elements in nums2
        
        # Append elements from nums2 to the end of nums1
        for index in range(n): 
            nums1[m + index] = nums2[index]  # Fill nums1 with elements from nums2
        
        # Sort the merged array
        nums1.sort()  # Sort the combined elements to ensure they are in non-decreasing order

# Time Complexity: O((m + n) log(m + n)), where m is the number of elements in nums1 and n is the number of elements in nums2.
# Space Complexity: O(n), due to the space used by the sort function for temporary storage.