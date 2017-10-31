#example1
#answer = input(' Would you like express shipping? (Yes/No) - ')
#if answer == "Yes" :
#    print(" That will be an extra  $10")
#print(" Have a nice day! \n")

#example2
#favTeam = input(" what is your fav hocky team? \t")
#if favTeam == "Senators" :
#    print(" Yes Go Sens Go")
#    print(" 2nd line")
#print(" It's okay if you prefer football/soccer")

#example3
#favTeam = input(" your fav Team name?\t")
#if favTeam.upper() == "Senators" :
#    print(" Yes Go Sens Go")
#    print(" 2nd line")
#print(" It's okay if you prefer football/soccer")

#example4
#favTeam = input(" your fav Team name?\t")
#if favTeam.upper() == "SENATORS" :
#    print(" Yes Go Sens Go")
#    print(" 2nd line")
#print(" It's okay if you prefer football/soccer")

#example5
#bestTeam = 'SENATORS'
#favTeam = input(" your fav Team name?\t")
#if favTeam.upper() == bestTeam :
#    print(" Yes Go Sens Go")
#    print(" 2nd line")
#print(" It's okay if you prefer football/soccer")

#example6
#bestTeam = 'senators'
#favTeam = input(" your fav Team name?\t: ")
#if favTeam.upper() == bestTeam.upper() :
#    print(" Yes Go Sens Go")
#    print(" 2nd line")
#print(" It's okay if you prefer football/soccer")

#example7
#answer = input("answer? (Yes, No)\t: ")
#if answer == "Yes" :
#    print("Good")
#if not answer == "Yes" :
#    print("Not Good")
#vaccinated = input("vaccination done? (Yes, No)\t: ")
#if not vaccinated == "Yes" :
#    print("Vaccination is mandatory")

#example8
#deposit = input("how much is your deposit? \t: ")
#if int(deposit) > 100 :
#    print(" enjoy your toaster")
#print(" Have a nice day!")

#example9
#deposit = int(input("how much is your deposit? \t: "))
#if deposit > 100 :
#    print(" enjoy your toaster")
#print(" Have a nice day!")

#example10
#deposit = int(input(" how much is your deposit? \t: "))
#if deposit > 100 :
#    print(" you get a free toaster")
#else:
#    print(" Enjoy your mug")
#print(" Have a nice day!")

#example11
#freeToaster = False
#freeMug = False
#deposit = int(input(" how much is your deposit? \t: "))
#if deposit > 100 :
#    freeToaster = True
#else:
#    freeMug = True
#
#if freeToaster :
#    print(" you get a free toaster")
#else :
#    if freeMug :
#        print(" Enjoy your mug")
#print(" Have a nice day!")

#Challenge
totalCost = 0.00
shippingCost = 10.00
totalPurchase = float(input("how is your total purchase?\t: "))
if totalPurchase < 50.00 :
    totalCost = totalPurchase + shippingCost
    print(" your Shipping cost is about ${0:.2f}".format(shippingCost))
    print(" Your total amount due is ${0:.2f}".format(totalCost))
else :
    totalCost = totalPurchase
    shippingCost = 0.00
    print(" your Shipping cost is about ${0:.2f}".format(shippingCost))
    print(" Your total amount due is ${0:.2f}".format(totalCost))








