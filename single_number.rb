def single_number(nums)
    snums = nums.sort
    i = 0
    while i < snums.size
        return snums[i] if (snums[i] != snums[i+1])
        i += 2
    end
end

#time complexity O(n)
#space complexity O(n)

# other people's solutions used reduce with xor in order to single out the single num. This will be slower than the above solution in all but the worst cases.
