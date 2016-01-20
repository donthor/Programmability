def reverse(text):
    word = []
    num = len(text) - 1
    for count in text:
        while num >= 0:
            word.append(text[num])
            num -= 1
    s = ''.join(word)
    return s

print reverse('Hello')
