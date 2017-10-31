#challenge
def getMessagefromUser() :
    message = input("Please share your opinion on Bahubali movie\t: ")
    return message

def writeMessageToFile(message) :

#method-1
    #file = open('mva12_Func_demo.txt',mode='w')
    #file.write(message)
    #file.close()

#method-2
    with open('mva12_Function_demo.txt',mode='w') as demoFile :
        demoFile.write(message)
        print("following feedback :\n" +
                message + 
                "\n is written to the file Successfully, Please verify...\n")

CustFeedback = getMessagefromUser()
writeMessageToFile(CustFeedback)
print("\n END of process. . . ")