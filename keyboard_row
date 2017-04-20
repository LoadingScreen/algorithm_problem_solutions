# @param {String[]} words
# @return {String[]}    
def find_words(words)
    ltop = ["q","w","e","r","t","y","u","i","o","p"]
    lmid = ["a","s","d","f","g","h","j","k","l"]
    lbott = ["z","x","c","v","b","n","m"]
    
    output = []
    
    words.each do |word|
        membership = [0,0,0] #first thing that came to mind, don't laugh
        word.each_char do |char|
            membership[0] = 1 if (ltop.include?(char))
            membership[1] = 1 if (lmid.include?(char)) #not dry so sorry
            membership[2] = 1 if (lbott.include?(char))
        end
        output << word if (membership[0] + membership[1] + membership[2] == 1)
    end
    
    output
end

#time complexity is....O(n)?
#space complexity is O(n)
