import base64

def base64_to_text(text):
    return base64.b64decode(text).decode('UTF-8', errors="ingore")

#Usage
text="Vmxkd1NrNVhVbk5qUlZKU1ltdGFjRlJYZEhOaWJFNVhWR3RPV0dKVmJEWldiR1JyV1ZkS1ZXRXphRnBpVkVaVFYycEtVMU5IUmtobFJYQlRUVmhDTmxZeFdtdGhhelZ5WWtWYWFWSlViRmRVVlZaYVRURmFjbFpyT1ZaV2JXUTJWa1pvYTFkck1YVlVhbHBoVWxack1GUlZaRXRqVmxaMVZHMTRXRkpVUlRCWFdIQkdUbGRHY2s1VmFFOVdNWEJoV1Zkek1XSldaSFJPVm1SclZsZDRXbFJWVm5wUVVUMDk="
#we are looking for a "FLAG" "INSA" OR "CTF"


for i in range(10):
    text = base64_to_text(text)
    if "INSA" in text:
        print(f"Round {i} : ",text)
        break

#print(base64_to_text(text))