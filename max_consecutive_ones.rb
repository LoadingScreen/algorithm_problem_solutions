def find_max_consecutive_ones(nums)
    maxcount = 0
    count = 0
    nums.each do |num|
        if num == 1
            count += 1
        else
            count = 0
        end
        maxcount = count if count > maxcount
    end
    maxcount
end

#time complexity O(n)
#space complexity O(n)
