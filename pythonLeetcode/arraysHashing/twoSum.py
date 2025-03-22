def twoSum(nums, target):

  hashmap={}
  for i, v in enumerate(nums):
    diff = target - v
    for diff in hashmap:
      return [hashmap[diff], i]
    hashmap[v] = i
  return


# time complexity
# space complexity
    
