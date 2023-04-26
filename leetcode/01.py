#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [3,2,4]
target = 6
prethodni_broj=0
zbroj=0
for i in range(len(nums)):
    if(prethodni_broj+nums[i]==target):
        print(f"[{i-1},{i}]")
        print(f"[{nums[i-1]},{nums[i]}]")
    prethodni_broj=nums[i]
 
    
    

    
    











