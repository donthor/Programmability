print ("Type a word: ")
pig = raw_input ().lower()
if len(pig) > 0 and pig.isalpha():
    def piglatin():
        if pig[0] not in ['a', 'e', 'i', 'o', 'u']:
            newname = pig[1:len(pig)] + pig[0] + 'ay'
            print newname
        else:
            print (pig + "yay")
    piglatin()
else:
    print "Try again"