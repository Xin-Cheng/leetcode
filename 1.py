# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def __init__(self, array):
        self.data = array
    def twoSum(self, target):
        for i in self.data:
            if target - i in self.data:
                return [self.data.index(i), self.data.index(target - i)]

def main():
    array = [2, 7, 11, 15]
    sol = Solution(array)
    result = sol.twoSum(18)
    print(result)

if __name__ == "__main__":
    main()