class Mobile:
   #pass argumets
    def __init__(self , M):
        self.model = M
    def show_model(self,P):
        price = P
        print("model :",self.model,"price :" , price)
realme = Mobile( "Pro12")
realme.show_model(2000)        