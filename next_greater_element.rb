# https://leetcode.com/problems/next-greater-element-i/#/description

def next_greater_element(find_nums, nums)
    result = []
    find_nums.each_with_index do |n, i|
        result[i] = -1
        idx = nums.index(n)
        j = idx + 1
        while j <= nums.length - 1
            if nums[j] > n
                result[i] = nums[j]
                break
            end
            p [n,j]
            j += 1
        end
    end
    result
end

# time complexity is O(find_nums, nums)
# space complexity is O(nums)
