from socket import EAI_BADFLAGS


CN = int(input("Enter Number of class held :"))
N = int(input("NO of class attend"))
persentage = (CN/N)*100
if persentage > 75:
                   print("you are eligible for exam")
else:
    print("You are not eligible for exam") 