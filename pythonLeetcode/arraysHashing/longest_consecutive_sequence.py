#Descripton : Return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
# The elements do not have to be consecutive in the original array.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums) #create a hashset from the input
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
