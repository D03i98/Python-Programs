from optparse import Option


Balance = 8000
print("""
Select the Options
1.CreateAccount
2. Balance
3. Withdraw
4. Deposit
5. Exit

""")
while True:-

   option =int(input("Please select the Option : "))
   Password = int(input("Enter 4 dgit password"))
   if(option == 1):
    UserName = input("Enter UserName : ")
    Pin = input("Enter 4 Digit Password :")
    print("Create Account Sucessfully")
    Anothertransaction =(input("Do you want to make another transaction yes/ no "))
    if(Anothertransaction == "yes"):
       continue
    else:
        break
   elif(option == 2 ):
      print("your balance is : ", Balance)
      
   elif(option == 3):
       Withdraw = int(input("Enter withdraw amount: "))
       Balance = Balance - Withdraw
       if(Balance > Withdraw):
          print("plesae collect your money")
          print("your current Balance is :" ,Balance)
       else:
          print("Unsufficent Balance")
   elif(option == 4 ):
        Deposit = int(input("Enter deposite amount : "))
        Balance = Balance + Deposit
        print("Sucessfully diposited")
        print("Your current Balance is : " , Balance)
   elif(option == 5):
    print("Thank you")
    exit()
    
   else:
    print("Please select the transaction or enter correct pin")