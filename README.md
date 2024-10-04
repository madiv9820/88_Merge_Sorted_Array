# 88. Merge Sorted Array

__Type:__ Easy <br>
__Topics:__ Array, Two Pointers, Sorting <br>
__Companies:__ Google, Amazon, Meta, Microsoft, Bloomberg, Accenture, Infosys, Oracle, Yandex, Apple, TikTok, Hubspot, Adobe, Uber, Yahoo, tcs, PayPal, IBM, LinkedIn, EPAM Systems, Zoho, Squarespace <br>
<hr>

You are given two integer arrays `nums1` and `nums2`, sorted in __non-decreasing order__, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

__Merge__ `nums1` and `nums2` into a single array sorted in __non-decreasing order__.

The final sorted array should not be returned by the function, but instead be _stored inside the array_ `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.
<hr>

### Examples:

__Example 1:__

__Input:__ nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 <br>
__Output:__ [1,2,2,3,5,6]<br>
__Explanation:__ The arrays we are merging are [1,2,3] and [2,5,6].<br>
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

__Example 2:__

__Input:__ nums1 = [1], m = 1, nums2 = [], n = 0 <br>
__Output:__ [1] <br>
__Explanation:__ The arrays we are merging are [1] and []. <br>
The result of the merge is [1].

__Example 3:__

__Input:__ nums1 = [0], m = 0, nums2 = [1], n = 1 <br>
__Output:__ [1] <br>
__Explanation:__ The arrays we are merging are [] and [1]. <br>
The result of the merge is [1].<br>
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
<hr>

### Constraints:

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- <code>-10<sup>9</sup> <= nums1[i], nums2[j] <= 10<sup>9</sup></code>
<hr>

### Follow up:
Can you come up with an algorithm that runs in `O(m + n)` time?
<hr>

### Hints
- You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?
- If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.