import string

def count_char(text):
    Chars = {}
    count = 0;
    for char in text:
        if char in string.ascii_letters:
            if char not in Chars:
                Chars[char] = 1
            else:
                Chars[char] += 1
            count += 1

    for n in Chars:
        Chars[n] = str(round(Chars[n] / count, 2)*100) + " %"
    
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

def count_word_noascii(text, lenght = None):
    Words = {}

    for letter in text:
        if letter not in string.ascii_letters:
            text = text.replace(letter, " ")

    if lenght is None:
        Words = text.split()
        wfreq=[Words.count(w) for w in Words]
        return dict(sorted(dict(zip(Words, wfreq)).items() , key=lambda item:item[1], reverse=True))
    else:
        for word in text.split():
            if word in Words:
                Words[word] += 1
            elif len(word) == lenght:
                Words[word] = 1

    Words = dict(sorted(Words.items(), key=lambda item: item[1], reverse=True))
    
    return Words 

#Usage:

print(count_word("Hello World!!!!!"))
print(count_word("I , i'm , don't" , 3))
print(count_word_noascii("Hello World, Hello World!!!!!"))
print(count_word_noascii("I , i'm , don't" , 3))
print(count_char("Hello World!!!!!"))