# Sorting based 
Time Complexity : O(nlogn) 
def sortColors(self, nums: List[int]) -> None:
    nums.sort()

# Counting based 
Time Complexity : O(n) - 2 Pass Solution
def sortColors(self, nums: List[int]) -> None:
    zeros=0
    ones=0
    for i in nums:
      if i==0:
        zeros+=1
      if i==1:
        ones+=1
    for i in range(zeros):
      nums[i]=0
    for i in range(zeros,zeros+ones):
      nums[i]=1
    for i in range(zeros+ones,len(nums)):
      nums[i]=2


# Swapping based 
Time Complexity : O(n) - 1 Pass Solution
def sortColors(self, nums: List[int]) -> None:        
      p1 = 0
      p2 = len(nums) - 1
      I = 0
      while I <= p2:

          if nums[I] == 0:
              tmp = nums[p1]
              nums[p1] = nums[I]
              nums[I] = tmp
              p1 += 1
              I += 1

          elif nums[I] == 2:
              tmp = nums[p2]
              nums[p2] = nums[I]
              nums[I] = tmp
              p2 -= 1

          else:
              I +=1
