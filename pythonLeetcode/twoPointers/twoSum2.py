
def twoSum2(nums, target):

  l=0
  r=len(nums)-1

  while l<=r:

    if nums[l]+nums[r] == target:
      return [l+1, r+1]
    elif nums[l]+nums[r] > target:
      r=r-1
    else:
      l=l1+1
      
