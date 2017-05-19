# https://leetcode.com/problems/array-partition-i/#/description

def array_pair_sum(nums)
    snums = nums.sort
    sum = 0
    snums.each_with_index { |a,i| sum += a if i % 2 == 0 }
    sum
end

# time complexity bounded by .sort
# space complexity O(nums)
