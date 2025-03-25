#Question Description: Given an integer array nums and an integer k, return the k most frequent elements within the array.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
                    
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# time complexity : O(n) where n is the number of of elements in the input
# space complexity : O(n) where n in the number of unique elemnts stored in hashmap, anducket list

        



