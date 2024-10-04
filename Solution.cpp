#include <vector>
#include <iostream>
using namespace std;

class Solution {
    public:
        void merge(vector<int>& nums1,   // First sorted array
                    int m,               // Number of elements in nums1
                    vector<int>& nums2,  // Second sorted array
                    int n) {            // Number of elements in nums2
            
            // Create a temporary vector to hold the merged elements
            vector<int> temp_Vector(m + n, 0); 
            int ptr1 = 0, ptr2 = 0, index = 0; // Initialize pointers for both arrays and the index for temp_Vector

            // Merge the two arrays until one is exhausted
            while (ptr1 < m && ptr2 < n) {
                // Compare elements from both arrays and add the smaller one to temp_Vector
                if (nums1[ptr1] <= nums2[ptr2]) 
                    temp_Vector[index++] = nums1[ptr1++]; // Add from nums1 and move pointer
                else 
                    temp_Vector[index++] = nums2[ptr2++]; // Add from nums2 and move pointer
            }

            // If there are remaining elements in nums1, add them to temp_Vector
            while (ptr1 < m) 
                temp_Vector[index++] = nums1[ptr1++]; // Add remaining elements from nums1
            
            // If there are remaining elements in nums2, add them to temp_Vector
            while (ptr2 < n) 
                temp_Vector[index++] = nums2[ptr2++]; // Add remaining elements from nums2

            // Copy the sorted elements back into nums1
            for (index = 0; index < m + n; ++index) 
                nums1[index] = temp_Vector[index]; // Update nums1 with merged results
        }
};

int main() {
    vector<int> nums1 = {1,2,3,0,0,0}, nums2 = {2,5,6};
    int m = 3, n = 3;
    Solution obj;

    obj.merge(nums1, m, nums2, n);
    for(auto x: nums1) cout << x << " ";
    cout << endl;
}