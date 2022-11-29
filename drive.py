from coffee_class import Coffee
from black_coffee import BlackCoffee


while True:
    print("""
    <------------------Enter your choose------------------>
    press 1(One) ---->>Regular Coffee(Hot & Could)
    press 2(Two) ---->>Black Coffee
    press 3(Three) ---->>Off Machine
    
""")
    choose=int(input("Enter your Choose: "))
    if(choose==1):
        suger=str(input("Do you want to add suger (yes/no)?: "))
        milk=float(input("Enter amount of milk(50gm/75gm/100gm): "))
        Coffee=Coffee(suger,milk)
        Coffee.coffee_details()

    elif(choose==2):
        blackCoffee=BlackCoffee()
        blackCoffee.coffee_details()
    else:
        exit()
