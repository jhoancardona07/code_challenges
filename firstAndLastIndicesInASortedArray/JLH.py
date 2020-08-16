class Solution: 
  def getRange(self, arr, target):
    arr.append(None)
    found=False
    count=0
    result=[]
    for element in arr:
        if (element==target and found==False):
            found=True
            result.append(count)
        if((found==True and element!=target) or (found==True and count==len(arr))):
            found=False
            result.append(count-1)
        count=count+1
    if len(result)==0:
        result.append(-1)
        result.append(-1)
    return result

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))
arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))