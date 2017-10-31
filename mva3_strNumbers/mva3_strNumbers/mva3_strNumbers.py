#practise-1
age=42
print(" %d" % age)
#no quotes are given here , then its a numeric value
width=20
height=5
area=width*height
#print("\narea:\t")
print(" %d" % area)
#print("area:\t"+area) >>>> doesn't work this way
####
#exponent=5**5
#print("\n exponent=\t" + 5**5) doesn't work this way
#
#() ** */ +- === order of precedence for math operations
print(" width: %d \t" % width )
print(" height: %d \n" % height)
print(" area:\t %d" % area)
print(" ") #just tp beautify the output display
print(" 3d area: \t %6d" % area) #display is prefixed with 6 spaces 
print(" 3d area: \t %06d" % area) #display is prefixed with 6 zeroes 
print(" float area: \t %f" % area) #displays with 6 decimals
print(" float area: \t %.2f" % area) #displays with 2 decimals
#we can also use format method to format numeric values
print(" 6d area: \t {0:6d}".format(area))
print(" 6d area: \t {0:06d}".format(area))
print(" float area: \t {0:f}".format(area))
#example to display multiple numbers
print(" width is {0:d} height is {1:d} and area is {2:d}".format(width, height, area))
#breaking long statements into multiple lines
print(" breaking long statements into multiple lines")
print(""" a 
 b""")
print(" width is" + \
" {0:d} height is {1:d} and area is {2:d}".format(width, height, area))
