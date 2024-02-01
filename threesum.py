class Solution:  
    def tresSuma(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        for i in range (len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    ret.add((nums [i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif target > 0>
                    r -= 1
                else:
                    l += 1
        return list(ret)
            