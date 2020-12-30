### Approach 1 
Time Complexity : O(nlogn)
Space Complexity : O(1) because of python sort() else it would be O(n)

def findDuplicate(self , nums):
  nums.sort()
  for i in range(1,len(nums):
    if nums[i]==nums[i-1]:
      return nums[i]
    
### Approach 2
Time Complexity : O(n)
Space Complexity : O(n)

def findDuplicate(self , nums):
  unique = dict()
  for i in nums:
    if unique.get(i,0)==0:
      unique[i]=1
    else:
      return i
      
### Approach 3
Time Complexity : O(n)
Space Complexity : O(1)

def findDuplicate(self , nums):
  n=len(nums)
  big=n+1
  for i in range(n):
    I=nums[i]%big
    nums[I]+= big
    
  for i in range(n):
    if nums[i]>=(2*big):
      return nums[i]
