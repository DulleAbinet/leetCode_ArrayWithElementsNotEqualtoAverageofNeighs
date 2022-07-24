class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res_arr = []
        left = 0
        right = len(nums)-1
        while len(res_arr) != len(nums):
            res_arr.append(nums[left])
            left += 1
            if left < right :
                res_arr.append(nums[right])
                right -= 1
        return res_arr
