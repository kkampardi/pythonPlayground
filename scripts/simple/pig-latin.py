# get sentence fron user
original = input("Enter a sentence:").strip().lower()


#split sentece into words

words = original.split()

"""
loop through words and convert to pig latin
Rouls
if it starts with a vowel just add "yay"
otherwise move the first consonant cluser to end, and add "ay"
"""
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_words.append( word + "yey")
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)


# stick words back together
output = " ".join (new_words)

#output the final string

print( output)

