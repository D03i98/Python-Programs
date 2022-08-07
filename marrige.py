Gender = input("Enter the Gender ")
Age = int(input("Entrer the age "))
if Gender == 'Male' and Age > 21:
    print("cogratulation ! yo are eligible for marrrige")
elif Gender == 'Female' and Age > 18:
    print("cobgratulation you are eligible for marrige")
else:
    print("You are child")