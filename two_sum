# https://leetcode.com/problems/two-sum/#/description
def two_sum(nums, target)
    i = 0
    while i < nums.size
        j = i + 1
        while j < nums.size
            if nums[i] + nums[j] == target && i != j
                return [i, j]
            end
            j += 1
        end
        i += 1
    end
end

#time complexity O(n^2)
#space complexity O(n)
