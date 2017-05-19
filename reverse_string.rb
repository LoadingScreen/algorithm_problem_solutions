# @param {String} s
# @return {String}
def reverse_string(s)
    result = []
    s.each_char do |ch|
        result.unshift(ch)
    end
    result.join
    # s.reverse!
end

# time complexity O(n)
# space complexity O(n)
