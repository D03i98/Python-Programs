Number = int(input("Enter a number"))
a = Number//10
b = Number%10
c = a//10
d = a%10
sum = (c*c*c)+(b*b*b)+(d*d*d)
if Number==sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")


