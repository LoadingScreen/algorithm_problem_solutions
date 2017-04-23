# @param {Integer[]} nums
# @return {Integer[]}
def next_greater_elements(nums)
    result = Array.new(nums.size, -1)
    
    nums.each_with_index do |n1, i|
        # p result
        new_nums = nums.rotate(i)
        new_nums.each do |n2|
            if n2 > n1
                result[i] = n2
                break
            end
        end
    end
    result
end

# time complexity is O(n*n)
# space complexity is O(n)

# not yet efficient enough to pass all test cases on LeetCode
