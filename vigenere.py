import string

def dec_vigenere(text, key):
    flag=''
    for i in range(len(text)):
        if text[i] in string.ascii_lowercase:
            flag+=''.join(chr((ord(text[i])-ord(key[i%len(key)]))%26+97))
        elif text[i] in string.ascii_uppercase:
            flag+=''.join(chr((ord(text[i])-ord(key[i%len(key)]))%26+65))
        else:
            flag+=''.join(text[i])
    return flag

#Usage
text="vhixoieemksktorywzvhxzijqni"
key='caesar'
print(dec_vigenere(text,key))