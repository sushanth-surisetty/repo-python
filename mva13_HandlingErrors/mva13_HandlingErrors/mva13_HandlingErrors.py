#example1
import sys
first=input("Enter the first Number\t: ")
second=input("Enter the second number\t: ")
firstNumber=float(first)
secondNumber=float(second)
errorFlag=False
try:
    result = firstNumber / secondNumber
    print(first + "/" + second + "=" + str(result))
#### method-1
#except :
#    error = sys.exc_info()[0]
#    print("I am sorry something went wrong . . .\n")
#    print(error)
#    print("\n")
#
#### method-2
except ZeroDivisionError :
    print("The answer is Infinity")
    #sys.exit() #to break the flow and exit the process
#### method-3
    errorFlag = True
except :
    error = sys.exc_info()[0]
    print("I am sorry something went wrong . . .\n")
    print(error)
    print("\n")
if not errorFlag :
    print("Default message to indicate END of process. . . ")
else :
    print("there was an error \n END of process .. .. .. \n")