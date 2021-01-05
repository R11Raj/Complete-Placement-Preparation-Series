### Approach 1 Naive solution
Time Complexity : O(nlogn)

def findMissingRepeating(self,arr,n):
  arr.sort()
  for i in range(1,n):
    if arr[i]-arr[i-1]==0:
      repeating=arr[i]
    if arr[i]-arr[i-1]==2:
      missing=arr[i-1]+1
  return [repeating,missing]
  
### Approach 2 Average solution
Time Complexity : O(n)
Space Complexity : O(n)

def findMissingRepeating(self,arr,n):
  temp=[0 for i in range(n)]
  for i in arr:
    temp[i-1]+=1
  for i in temp:
    if i==0:
      missing=i
    if i==2:
      repeating=i
  return [repeating,missing]
  
### Approach 2 Optimal solution
Time Complexity : O(n)
Space Complexity : O(1)

def findMissingRepeating(self,arr,n):
  for i in arr:
    if arr[abs(i)-1]>0:
      arr[abs(i)-1]*=-1
    else:
      repeating=abs(i)
  for i in range(n):
    if arr[i]>0:
      missing=i
      break
  return [repeating,missing]
