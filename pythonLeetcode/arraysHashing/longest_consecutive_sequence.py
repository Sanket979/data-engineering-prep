class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        longest = 0
        #hashset = {2,3,4,5,10,20}

        for n in nums:

            if (n-1) not in hashset:
                l=1

                while (n+l) in hashset:
                    l+=1
                longest = max(longest, l) 

        return longest


# Input: nums = [2,20,4,10,3,4,5]
# output = 4

# time complexity : O(n) where n in the number of elements in nums.
# space complexity : O(n) where n in the no. of elements stored inside set.
