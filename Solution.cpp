#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
    public:
        void merge(vector<int>& nums1,   // First sorted array
                    int m,               // Number of elements in nums1
                    vector<int>& nums2,  // Second sorted array
                    int n) {            // Number of elements in nums2
            
            // Append elements from nums2 to the end of nums1
            for(int index = 0; index < n; ++index)
                nums1[m + index] = nums2[index];  // Fill nums1 with elements from nums2
            
            // Sort the merged array to ensure all elements are in non-decreasing order
            sort(nums1.begin(), nums1.end());  // Sort the entire nums1 array
        }
};

// Time Complexity: O((m + n) log(m + n)), where m is the number of elements in nums1 and n is the number of elements in nums2.
// This is due to the sorting operation on the combined array of size (m + n).

// Space Complexity: O(n), where n is the number of elements in nums2, as we are using additional space 
// for sorting the combined array. The effective space used for merging can be considered as O(m + n), 
// but auxiliary space is dominated by the sorting process.


int main() {
    vector<int> nums1 = {1,2,3,0,0,0}, nums2 = {2,5,6};
    int m = 3, n = 3;
    Solution obj;

    obj.merge(nums1, m, nums2, n);
    for(auto x: nums1) cout << x << " ";
    cout << endl;
}