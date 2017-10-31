#example1
#country = input("Where are you from?\t: ")
#if country == "CANADA" :
#    print("Hello")
#elif country == "GERMANY" :
#    print("Hi ...")
#elif country == ("FRANCE") :
#    print("Bonjour")
#
#challenge
GST = 0.00
HST = 0.00
PST = 0.00
totalCost = 0.00
totalCharge = float(input(" Total order of your online order?\t: "))
country = input(" Where are you from?\t: ")
if country == "CANADA" :
    province = input(" in CANADA, province of shopping location is?\t: ")
    if province.upper() == "ALBERTA" :
        GST = 0.05
    elif province.upper() == "ONTARIO" or \
        province.upper() == "NEW BURNSWICK" or \
        province.upper() == "NOVA SCOTIA" :
            HST = 0.13
    else :
        PST = 0.06
        GST = 0.05
else :
    GST = 0.00
    HST = 0.00
    PST = 0.00
    province = "Non-CANADA location"

GSTtax = (GST*totalCharge)/100
HSTtax = (HST*totalCharge)/100
PSTtax = (PST*totalCharge)/100
totalCost = totalCharge + GSTtax + HSTtax + PSTtax
print(" Based on your province :" + province)
print(" GST tax is \t: %.2f" % GSTtax)
print(" HST tax is \t: %.2f" % HSTtax)
print(" PST tax is \t: %.2f" % PSTtax) 
print(" Your Purchase total is \t: %.2f" % totalCost)
