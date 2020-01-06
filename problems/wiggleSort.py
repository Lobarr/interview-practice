def wiggleSort(nums):
    for i in range(1, len(nums)):
      isEven = i % 2 == 0
      prevIndex = i - 1
      if (isEven and nums[prevIndex] <= nums[i]) or (not isEven and nums[prevIndex] >= nums[i]):
          nums[prevIndex], nums[i] = nums[i], nums[prevIndex]