import string

def string_to__bit(text):
    return "".join(f'{ord(char):08b}' for char in text )
 
def bit_to_string(bit):
    return "".join(chr(int(bit[8*i:8*i+8] , 2)) for i in range(len(bit)//8))

def int_to_bit(intT):
    return f'{intT:08b}'

def bit_to_int(bit):
    return int(bit , 2)

#Usage
text = string_to__bit("Hello World")
print(text)
bit = bit_to_string(text)
print(bit)

bitIntero = int_to_bit(23)
print(bitIntero)
Intero = bit_to_int(bitIntero)
print(Intero)

