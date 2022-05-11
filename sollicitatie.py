print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Welkom bij de sollicitatie van de baan Circusdirecteur voor Circus HotelDeBotel!")
print("Ik ga jou een paar vragen stellen om te zien of jij geschikt bent!")
print("Hier komt 'ie!")

def man():
    dierendressuur = input("Hoeveel jaar heb je ervaring met dieren-dressuur? ")
    jongleren = input("Hoeveel jaar ervaring heb je met jongleren? ")
    acrobatiek = input("Hoeveel jaar ervaring heb je met acrobatiek? ")
    MBO = input("Wat voor MBO diploma heeft u? ")
    rijbewijs = input("Hoeveel jaar heeft u al een vrachtwagen rijbewijs?" )
    hoed = input("Hoeveel hoge hoedden heeft u?" )
    snor = input("Heeft u een snor?")
    lengtesnor = input("Hoe lang is uw snor?")
    lengte = input("Hoeveel cm bent u? ")
    gewicht = input("Hoeveel kilo zwaar bent u? ")
    diploma = input("Wat voor diploma heb je? ")
    if int(dierendressuur) > 5 and int(jongleren) > 4 and int(acrobatiek) > 3 and int(MBO) == 4 and int(rijbewijs) > 1 and int(hoed) > 1 and snor == "ja" and int(lengtesnor) > 10 and int(lengte) > 150 and int(gewicht) > 90 and diploma == "Overleven met gevaarlijk personeel":
        print("Gefeliciteerd, je bent gekwalificeerd voor de baan!")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    else: print("helaas, je bent niet ervaren genoeg")

def vrouw():
    try:
        dierendressuur = input("Hoeveel jaar heb je ervaring met dieren-dressuur? ")
        jongleren = input("Hoeveel jaar ervaring heb je met jongleren? ")
        acrobatiek = input("Hoeveel jaar ervaring heb je met acrobatiek? ")
        MBO = input("Wat voor MBO diploma heeft u? ")
        rijbewijs = input("Hoeveel jaar heeft u al een vrachtwagen rijbewijs?" )
        hoed = input("Hoeveel hoge hoedden heeft u?" )
        haarlengte = input("Hoelang is uw haar?")
        lengte = input("Hoeveel cm bent u? ")
        gewicht = input("Hoeveel kilo zwaar bent u? ")
        diploma = input("Wat voor diploma heb je? ")
        if dierendressuur > 5 and jongleren > 4 and acrobatiek > 3 and MBO == 4 and rijbewijs > 1 and hoed > 1 and haarlengte > 20 and lengte > 150 and gewicht > 90 and diploma == "Overleven met gevaarlijk personeel":
            print("Gefeliciteerd, je bent gekwalificeerd voor de baan!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        else: print("helaas, je bent niet ervaren genoeg")
    except NameError: 
        if hoed == "geen":
            print("dat is niet mogelijk!")
    

geslacht = input("welk geslacht bent u?")
if geslacht == "vrouw":
    vrouw()
elif geslacht == "man":
    man()