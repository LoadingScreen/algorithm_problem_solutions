# https://leetcode.com/problems/reshape-the-matrix/#/description

def matrix_reshape(nums, r, c)
    if nums.size * nums[0].size != r*c
        return nums
    end
    result = Array.new(r) {Array.new(c) {nil} }  #might go wrong here
    fnums = nums.flatten
    i = 0
    k = 0
    while i < r do
        j = 0
        while j < c do
            result[i][j] = fnums[k]
            j += 1
            k += 1
        end
        i += 1
    end
    result
end
