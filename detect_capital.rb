# https://leetcode.com/problems/detect-capital/#/description


def detect_capital_use(word)
    if word == word.upcase
        true
    elsif word == word.downcase
        true
    elsif (word[0] == word[0].upcase) && (word[1..word.length] == word[1..word.length].downcase)
        true
    else
        false
    end
end

# time complexity is O(n^2)
# space complexity is O(n)
# faster than 70% of ruby submissions
