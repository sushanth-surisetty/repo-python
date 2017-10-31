#challenge
errorFlag=False
FN=input("Please enter the file name you want to access\t: ")
try :
    #myfile = open(FN,mode='r')
    with open(FN,mode='r') as myfile :
        data = myfile.read()
        for row in data :
            for value in row :
                print(value)

            #print(';'.join(row))
except FileNotFoundError :
    print("Sorry we could not find the file you're looking for : " + FN)
    errorFlag = True
if not errorFlag :
    print("File found and read successfully, Congratulations!! \n")
else :
    print("Are you sure you've the correct file name you need? \n")