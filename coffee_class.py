
class Coffee:

    def __init__(self,suger='No',milk=50.00):
        self.coffeeType=self.coffee_type()
        self.coffeeSize=self.coffee_size()
        self.coffeePrice=self.coffee_price(self.coffee_type,self.coffee_size)
        self.suger=suger
        self.milk=self.add_milk(milk)

    def coffee_type(self):
        print("""
            <--------------Slect Coffee Type--------------->
            press 1----->>Hot Coffee
            press 2----->>Cold Coffee
        """)
        choose=int(input("Slect your Coffee Type: "))

        if(choose==1):
            return "Hot Coffee"
        elif(choose==2):
            return "Cold Coffee"
        else:
            print("Worng Slection Try againg")
            choose=int(input("Slect your coffee type: "))
    
    def coffee_size(self):
        print("""
            <--------------Slect Coffee Size --------------->
            press 1----->>Small
            press 2----->>Regular
            press 3----->>Big
        """)
        choose=int(input("Slect your coffee type: "))
        if(choose==1):
            return "Small"
        elif(choose==2):
            return "Regular"
        elif(choose==3):
            return "Big"
        else:
            print("Worng Slection Try againg")
            choose=int(input("Slect your coffee type: "))
    
    def add_milk(self,milk):
        if (milk>100):
            return "100 gm"
        else:
            return f"{milk} gm"

    def coffee_price(self,coff_type,coff_size):
        
        if(coff_type=="Hot Coffee"):
            if coff_size=="Small":
                return 100
            elif coff_size=='Regualr':
                return 120
            else:
                return 150
        else:
            if coff_size=="Small":
                return 60
            elif coff_size=='Regualr':
                return 70
            else:
                return 100
    
    def coffee_details(self):
        print("")
        print("Coffee Type: ",self.coffeeType)
        print("Coffe Size: ",self.coffeeSize)
        print("Coffee Price: ",self.coffeePrice)
        print("Suger: ",self.suger)
        print("Amount of Milk: ",self.milk)
    
    def __str__(self):
        return "Regular Coffee Class"



