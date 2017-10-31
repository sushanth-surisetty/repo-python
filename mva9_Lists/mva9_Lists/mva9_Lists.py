#example1
guests = ['Chirstopher','Susan','Bill','Satya']
scores = [78,85,62,49,98]

#example2
#declare empty lists and add values later
#guests = []
#scores = []

#example3
#print(" " + guests[0])
#print(" " + guests[1])
#print(" " + guests[2])
#print(" " + guests[3])

#print(" %d" % scores[3])

#print("\n printing the list in reverse\n")

#print(" " + guests[-1])
#print(" " + guests[-2])
#print(" " + guests[-3])
#print(" " + guests[-4])

#print("\n")

#print(" " + guests[-5]) >>> list inder out of range

#example4
#guests[0] = "Steve"

#print("1st " + guests[0])
#print("2nd " + guests[1])
#print("3rd " + guests[2])
#print("4th " + guests[3])

#example5
#guests.append("Christopher")
#print("\n appended 'Christopher' \n ")
#print("1st " + guests[0])
#print("2nd " + guests[1])
#print("3rd " + guests[2])
#print("4th " + guests[3])
#print("5th " + guests[4])
#print("\n ")

##example5
#guests.remove("Christopher")
#print("\n removed 'Christopher' \n ")
#print("1st " + guests[0])
#print("2nd " + guests[1])
#print("3rd " + guests[2])
#print("4th " + guests[3])
##print("5th " + guests[4])
#print("\n ")

#example6
#del guests[0]
#print("\n removed 1st value \n ")
#print("1st " + guests[0])

##example7
#print("\n added 2 more values \n ")
#guests.append('Colin')
#guests.append('Trump')
#print("1st " + guests[0])
#print("2nd " + guests[1])
#print("3rd " + guests[2])
#print("4th " + guests[3])
#print("5th " + guests[4])
#print("\n ")

#example8
#print("\n updating the values \n ")
#guests[3] = 'Sachin'
#print("1st " + guests[0])
#print("2nd " + guests[1])
#print("3rd " + guests[2])
#print("4th " + guests[3])
#print("\n ")

#example9
#for steps in range(4) :
#    print(guests[steps])

#example10
#nbrEntries = len(guests)
#for steps in range(nbrEntries) :
#    print(guests[steps])

##alternate-way
for guest in guests :
    print(guest)

guests.sort()
print("\n sorted display \n")
for guest in guests :
    print(guest)

#challenge
print("Please enter the list attendees ")
print(" type EXIT to stop\t: \n")
GuestNames = [] 
Name = " "
while Name != "EXIT" :
    Name = input()
    GuestNames.append(Name)

GuestNames.sort()
for each in GuestNames :
    print(each)


