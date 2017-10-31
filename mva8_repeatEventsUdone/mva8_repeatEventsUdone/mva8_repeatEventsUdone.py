#example1
#answer = "0"
#while answer != "4" :
#    answer = input(" What is 2 + 2 \t: ")
#    if answer != "4" :
#        print(">>wrong answer, please try again! .. ")
#print("\n!!!! Yes! 2 + 2 = 4")

#example2
#answer = 0
#while answer != 4 :
#    answer = int(input(" What is 2 + 2 \t: "))
#    if answer != 4 :
#        print(" >>wrong answer, please try again! .. ")
#print("\n !!! Yes! 2 + 2 = 4")

#example3
#import turtle
#counter = 0
#while counter < 4 :
#    turtle.forward(100)
#    turtle.right(90)
#    counter=counter+1

#Challenge
import turtle
Length=int(input(" How long should the line be?\t: "))
userColor=input(" What is your preferred color?\t: ")
angle=int(input(" What should be the angle of the line?\t: "))
while Length !=0 :
    turtle.color(userColor)
    turtle.forward(Length)
    turtle.right(angle)
    




