"""
198. 打家劫舍
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        pre, cur = 0, 0
        for i, num in enumerate(nums):
            cur, pre = max(pre + num, cur), cur
        return cur