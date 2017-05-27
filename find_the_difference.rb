def find_the_difference(s, t)
    ss = s.split('').sort
    st = t.split('').sort
    (ss.length).times do |i|
        a, b = ss.shift, st.shift
        return b if a != b
    end
    st
end

#time complexity bounded by sort
#space complexity O(s)
