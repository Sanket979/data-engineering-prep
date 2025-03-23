#Question Description: Given an integer array nums and an integer k, return the k most frequent elements within the array.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = [[] for i in range(len(nums)+1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)

        #count = {1:1, 2:2, 3:3}

        for n , cnt in count.items():
            freq[cnt].append(n) #this will append the no at its right position.
        
        #freq =  [[], [1], [2], [3], [], [], []]

        res = []
        for i in range(len(freq)-1, 0, -1): #it will stop before 0th idx
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# time complexity : O(n) where n is the number of of elements in the input
# space complexity : O(n) where n in the number of unique elemnts stored in hashmap, anducket list

        



