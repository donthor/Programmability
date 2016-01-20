text= 'Am a long line of vowels and consonants'
def anti_vowel(text):
    x = 'aeiouAEIOU'
    for p in x:
       text = text.replace(p, '')
    print text

anti_vowel(text)
