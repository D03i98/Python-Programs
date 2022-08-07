from distutils.file_util import write_file
from math import remainder


num = int(input("Enter a Number"))
rev = 0
while num > 0:
    rem = num%10
    rev = (rev*10)+rem
    num = num % 10
    print("/n reverse of entred no is = %d" %rev)
