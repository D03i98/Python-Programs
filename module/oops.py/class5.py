class Moblie:
    def __init__(self , M):
        self.model = M
    def show_model(self,p):
        price = p
        print("Model: " , self.model ,"price : " , price)

#create diffrent object of single class
realme = Moblie("Realme X")
realme.show_model(2000)
print(id(realme)) # to show memory adress
print()

Redmi =Moblie("Redmo Note 10")
Redmi.show_model(3000)
print(id(Redmi))
print()

Vivo =Moblie("Vivo Y5")
Vivo.show_model(5000)
print(id(Vivo))
print()