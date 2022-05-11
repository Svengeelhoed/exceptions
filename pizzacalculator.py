def PizzaCalc(AmountofMoney):
    try:
        PizzaSize = input("Wil je een small(5.00,-), medium(7.50,-) of large pizza?(10.00),-")
        AmountofPizzas = input("Hoeveel " + PizzaSize + " pizzas wil je?")
        for i in range(int(AmountofPizzas)):
            if PizzaSize == "small":
                AmountofMoney = AmountofMoney + 5.00
            if PizzaSize == "medium":
                AmountofMoney = AmountofMoney + 7.50
            if PizzaSize == "large":
                AmountofMoney = AmountofMoney + 10.00
        Bonnetje(AmountofMoney)
    except NameError:
        print("get your code right you silly billy, thats a name error")
    else:
        print("nothing went wrong")
    finally:
        print("finish")

def Bonnetje(AmountofMoney):
    Nogmeer = input("wil je nog meer pizzas bestellen? ja/nee: ")
    if Nogmeer == "ja":
        PizzaCalc(AmountofMoney)
    else:
        print("Dat wordt dan " + str(AmountofMoney) + " euro!")

PizzaCalc(0)

