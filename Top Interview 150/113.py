class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
      """
      出題者賢すぎ問題その2

      これは二つのケースが考えられる
      1、maxSum が array　の一部であるとき
      2、maxSum　が array　の後部　＋ array の前部の時

      Case1ではDPで解ける O(N)
      Case2では maxSumが連続ではないため、直接解くことはできない。しかし、maxSumが連続ではない時はminSumは連続である。
      この時の maxSum = sum(nums) - minSumである。
      """
      INF = 10**16
      n = len(nums)
      dp_max = [-INF]*(n+1)
      dp_min = [INF]*(n+1)

      for i in range(n):
        num = nums[i]
        dp_max[i+1] = max(dp_max[i]+ num, num)
        dp_min[i+1] = min(dp_min[i] + num, num)
      
      maxSum = max(dp_max)
      minSum = min(dp_min)

      if maxSum < 0: return maxSum
      return max(maxSum, sum(nums)-minSum)