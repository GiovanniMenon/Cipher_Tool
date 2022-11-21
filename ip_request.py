import requests
import hashlib #Maybe for MD5 hash


#IP 

ip = "127.0.0.1"
port = "8080"

#Request
for i in range(100):
    cookies = {'name': 'value'}
    r = requests.post(f"http://{ip}:{port}", cookies)
    r.cookies  # Where "FLAG" is another cookies's name and this return the cookies FLAG value


#HashLib


tester_Md5 = hashlib.md5(str.encode("ciao")).hexdigest()
#Arg of hashlib.md5 must be econde string and the return must be in hex form


print(tester_Md5)
