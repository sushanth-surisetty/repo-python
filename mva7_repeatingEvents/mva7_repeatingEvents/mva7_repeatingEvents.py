
#example1
#import turtle
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)

#example2
#import turtle
#turtle.color('green')
#turtle.forward(100)
#turtle.right(45)
#turtle.color('blue')
#turtle.forward(50)
#turtle.right(45)
#turtle.color('pink')
#turtle.forward(100)
#turtle.right(90)
#turtle.color('red')
#turtle.forward(100)

#example3
#use a for loop to avoid repeating code
#import turtle
#for steps in range(4) :
#    turtle.forward(10)
#    turtle.right(90)
##turtle.color('red')
##turtle.forward(40)
#    turtle.color('red')
#    turtle.forward(40)

#example4
import turtle
#for steps in range(4) :
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#        turtle.forward(50)
#        turtle.right(90)

#example5
#for steps in range(6) :
#    turtle.forward(100)
#    turtle.right(360/6)
#    for moresteps in range(6):
#        turtle.forward(50)
#        turtle.right(360/6)

#example6
#nbr = 6
#for steps in range(nbr) :
#    turtle.forward(100)
#    turtle.right(360/nbr)
#    for moresteps in range(nbr):
#        turtle.forward(50)
#        turtle.right(360/nbr)

#example7
#nbr=6
#for steps in range(nbr) :
#    print(steps)

#example8
#for steps in range(1,4) :
#    print(steps)
#for steps in range(1,10,2) :
#    print(steps)
#for steps in [1,2,3,4,5] :
#    print(steps)

#example9
#nbr = 4
#for steps in ['red','blue','green','black'] :
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(360/nbr)

#Challenge
nbr = 8
for steps in range(nbr) :
    turtle.forward(100)
    turtle.right(360/nbr)
    for moresteps in range(nbr):
        turtle.forward(50)
        turtle.right(360/nbr)









