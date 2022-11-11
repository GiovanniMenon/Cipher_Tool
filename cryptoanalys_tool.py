import string

def count_char(text):
    Chars = {}
    for char in text:
        if char in string.ascii_letters:
            if char not in Chars:
                Chars[char] = 1
            else:
                Chars[char] += 1
    return dict(sorted(Chars.items() , key= lambda item:item[1], reverse= True))

def count_word(text, lenght = None):
    if lenght is None:
        Words = text.split()
        wfreq=[Words.count(w) for w in Words]
        return dict(sorted(dict(zip(Words, wfreq)).items() , key=lambda item:item[1], reverse=True))
    else:
        Words = {}
        for word in text.split():
            if len(word) == lenght:
                if word not in Words:
                    Words[word] = 1
                else:
                    Words[word] += 1
        return dict(sorted(Words.items() , key= lambda item:item[1], reverse= True)) 

#Usage:

print(count_word("Hello World!!!!!"))
print(count_char("Hello World!!, Hello World"))