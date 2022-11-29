from coffee_class import Coffee

class BlackCoffee(Coffee):

    def __init__(self, suger='No', milk=50):
        super().__init__(suger, milk)
    

    def coffee_type(self):
        print("""
            <--------------Slect Coffee Type--------------->
            press 1----->>Black Coffee(Light)
            press 2----->>Black Coffee(Regular)
            press 3----->>Black Coffee(Strong)
        """)
        choose=int(input("Slect your Coffee Type: "))

        if(choose==1):
            return "Black Coffee(Light)"
        elif(choose==2):
            return "Black Coffee(Regular)"
        elif(choose==3):
            return "Black Coffee(Strong)"
        else:
            print("Worng Slection Try againg")
            choose=int(input("Slect your coffee type: "))
    
    def add_milk(self,milk):
        return "Milk is not applicable for Black Coffee"
    
    def __str__(self):
        return "Black Coffee "