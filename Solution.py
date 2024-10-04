from typing import List

class Solution:
    def merge(self, 
                nums1: List[int],  # First sorted array
                m: int,            # Number of elements in nums1
                nums2: List[int],  # Second sorted array
                n: int):           # Number of elements in nums2
        
        # Create a temporary array to hold the merged elements
        temp_Array = [0] * (m + n)        
        ptr1 = ptr2 = index = 0  # Initialize pointers for both arrays and the index for temp_Array

        # Merge the two arrays until one is exhausted
        while ptr1 < m and ptr2 < n:
            # Compare elements from both arrays and add the smaller one to temp_Array
            if nums1[ptr1] <= nums2[ptr2]:
                temp_Array[index] = nums1[ptr1]  # Add from nums1
                ptr1 += 1  # Move the pointer in nums1
            else:
                temp_Array[index] = nums2[ptr2]  # Add from nums2
                ptr2 += 1  # Move the pointer in nums2
            index += 1  # Move the index in temp_Array
        
        # If there are remaining elements in nums1, add them to temp_Array
        while ptr1 < m:
            temp_Array[index] = nums1[ptr1]  # Add remaining elements from nums1
            ptr1 += 1  # Move the pointer in nums1
            index += 1  # Move the index in temp_Array

        # If there are remaining elements in nums2, add them to temp_Array
        while ptr2 < n:
            temp_Array[index] = nums2[ptr2]  # Add remaining elements from nums2
            ptr2 += 1  # Move the pointer in nums2
            index += 1  # Move the index in temp_Array

        # Copy the sorted elements back into nums1
        for index in range(m + n):
            nums1[index] = temp_Array[index]  # Update nums1 with merged results