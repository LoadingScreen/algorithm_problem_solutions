# @param {String[]} words
# @return {String[]}    
def find_words(words)
    ltop = ["q","w","e","r","t","y","u","i","o","p"]
    lmid = ["a","s","d","f","g","h","j","k","l"]
    lbott = ["z","x","c","v","b","n","m"]
    ll = [ltop, lmid, lbott]

    output = []
    
    words.each do |word|
        membership = [0,0,0]
        word.each_char do |char|
            3.times do |i|
                membership[i] = 1 if ll[i].include?(char)
        end
        output << word if (membership[0] + membership[1] + membership[2] == 1)
    end
    
    output
end

#time complexity is....O(n)?
#space complexity is O(n)
