#Design and Implement python code for Phone Number and Email Address Extractor using Regular Expression

import re
s1="Phone number is 5648213488,9876543210,email ID of Jazz is Jazz5@gmail.com,typrgmail.com,hh.in,faiZan88@gmail.com"
x=re.search("[6-9]\d{9}",s1)
print(x.group())
emails = re.findall(r"[A-Za-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]{2,6}", s1)
print (emails)
