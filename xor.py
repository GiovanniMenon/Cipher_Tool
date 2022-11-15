

def dec_xor_string(text , key):
    for i in range(len(text)):
        return "".join(chr(ord(text[i])^ord(key[i%len(key)))] for i in range(len(text))) 



print(dec_xor_string("ciao" , "aaaa"))