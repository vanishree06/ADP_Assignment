#Design and Implement python code for Phone Number and Email Address Extractor using Regular Expression

import re
s1="Phone number is 5648213488,9876543210"
x=re.search("[6-9]\d{9}",s1)
print(x.group())
e='^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,6}$'
def check(email):
    if(re.search(e,email)):
        print("Valid")
    else:
        print("Invalid")
#check("ankit32.com")
check("sanmT8@gmail.com")
