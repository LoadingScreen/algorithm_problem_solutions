# https://leetcode.com/problems/fizz-buzz/#/description

# Write a program that outputs the string representation of numbers from 1 to n.

#But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For #numbers which are multiples of both three and five output “FizzBuzz”.

# @param {Integer} n
# @return {String[]}
def fizz_buzz(n)
    arr = Array (1..n)
    arr.map! do |i|
        if i % 15 == 0
            "FizzBuzz"
            elsif i % 5 == 0
            "Buzz"
            elsif i % 3 == 0
            "Fizz"
        else
            i.to_s
        end
    end
end

#time complexity O(n)
#space complexity O(n)
