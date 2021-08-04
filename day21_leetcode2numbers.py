# LEETCODE https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target. You may assume that each input would have
# exactly one solution, and you may not use the same element twice. You can return the
# answer in any order.

from itertools import combinations
nums = [2, 7, 11, 15]
target = 9
for item in (combinations(nums, 2)):
    if sum(item) == target:
        print([nums.index(item[0]), nums.index(item[-1])])
