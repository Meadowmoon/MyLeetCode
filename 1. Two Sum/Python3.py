class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in dic.values():
                key = [key for key, value in dic.items() if value == other]
                return key+[i]
            dic[i] = nums[i]

if __name__ == '__main__':
    a = Solution()
    result = a.twoSum([3,3], 6)
    print(result)
