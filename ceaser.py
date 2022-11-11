import string


def dec_ceaser(data,key):
    decData = ""
    for char in data:
        if char in string.ascii_lowercase:
            decData += chr((ord(char)-97 - key)%26 + 97)
        elif char in string.ascii_uppercase:
            decData += chr((ord(char)-65 - key)%26 + 65)
        else: 
            decData += char      
    return decData

def enc_ceaser(data,key):
    encData = ""
    for char in data:
        if char in string.ascii_lowercase:
            encData += chr((ord(char)-97 + key)%26 + 97)
        elif char in string.ascii_uppercase:
            encData += chr((ord(char)-65 + key)%26 + 65)
        else: 
            encData += char      
    return encData

def dec_ceaser_ascii_character_includes(data,key):
    decData = ""
    for char in data:
            decData += chr(ord(char) - key)
    return decData

def enc_ceaser_ascii_character_includes(data,key):
    encData = ""
    for char in data:
            encData += chr(ord(char) + key)
    return encData

# USAGE:
text = enc_ceaser("Hello World, UPPER_CASE , lower_case?!" , -24)

for key in range(-30 , 30): #Unknown key, key brute force 
   print(f"turno {key}: " + dec_ceaser(text,key))

print(dec_ceaser(text,-24)) #known key
