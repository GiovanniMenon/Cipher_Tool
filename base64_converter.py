import base64

def base64_to_text(text):
    return base64.b64decode(text).decode('UTF-8', errors="ingore")

#Usage
text="Y2lhbw=="         #ciao in base64
print(base64_to_text(text))