class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        remove_count = 0
        nums_copy = nums[:]
        for index, num in enumerate(nums_copy):
            if num == val:
                k -= 1
                index -= remove_count
                nums = nums[:index] + nums[index + 1:] + [0]
                remove_count += 1

        return k


s = Solution()
print(s.removeElement([3,2,2,3], 3))
