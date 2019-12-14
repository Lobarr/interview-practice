def twoSum(nums, target):
  check = {}
  for index, num in enumerate(nums):
    if num not in check:
      check[num] = [index]
    else:
      check[num].append(index)

  for num in nums:
    complement = target - num
    if complement == num and complement in check:
      if len(check[complement]) >= 2:
        return [check[complement][i] for i in range(2)]
      else:
        continue
    
    if complement in check:
      return [nums.index(num), nums.index(complement)]
    
  return []