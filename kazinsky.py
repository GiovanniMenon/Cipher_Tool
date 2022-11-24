def shift(text, key_length):
    return text[key_length:] + text[:key_length]

#we compare the original sentence with its shifted version
#we count the amount of same charcters in the same position
def freq_counter(s1, s2):
    freq = sum([1 for (x, y) in zip(s1, s2) if x == y])
    return freq

secret=''           #insert the crypted text

for kl in range(5, 16):
    print(f"Lenght:\t{kl}\tFreq:\t{freq_counter(secret, shift(secret, kl))}")