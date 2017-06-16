def add_digits(num)
    digits = num.to_s.split('')
    digitsum = digits.inject(0){|sum,x| sum + x.to_i }
    if digitsum / 10 == 0
        return digitsum
    else
        add_digits(digitsum)
    end
end

