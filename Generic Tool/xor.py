
def xor_str_str(data , key):
    # PRE: data is a string and key is a string
    # POST: Return an array of integer
    xor_str = []

    for i in range(len(data)):
        xor_str.append(ord(data[i])^ord(key[i%len(key)]))
    
    return xor_str


def xor_str_int(data , key):
    # PRE: data is a string and key is a integer
    # POST : Return an array of integer  
    xor_str = []

    for i in range(len(data)):
        xor_str.append(ord(data[i])^key)
    
    return xor_str

    
def xor_int_int(data , key):    
    # PRE: data is an integer and key is an integer
    # POST : Return the xor between key and data 
    return data^key
    

print(xor_str_str("ciao", "menny"))
print(xor_str_int("ciao", 10))
print(xor_int_int(2, 1))
