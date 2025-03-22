
def twoSum(nums, target):

  hashmap = {}
  for i, v in enumerate(nums):
    diff = target - v
    if diff in hashmap:
      return [hashmap[diff], i]
    hashmap[v] = i
  return


#time complexity
# space cmplexity: 
