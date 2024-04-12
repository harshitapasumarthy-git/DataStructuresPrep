nums = [2,7,11,15]
target = 9

def twoSum( nums, target):
    for i in range (len(nums)):
        res = target - nums[i]
        if res in nums:
            idx = nums.index(res)
            if(i == idx):
                continue
            break
    print( i,idx)
twoSum(nums,target)
        
       

