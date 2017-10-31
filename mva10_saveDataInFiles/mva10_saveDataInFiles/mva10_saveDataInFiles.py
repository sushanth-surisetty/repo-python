#example1
#Syntax >>> myFile = open(Filename,Accessmode)
#FileName like data.txt, data.csv
#path for the file is same folder as program
#
#Accesmodes: r=read;w=write;a=append;b=open-binary-file

fileName = "demo.txt"
#accessMode = 'w'
#WRITE='w'
#READ='r'
APPEND = 'a'

#myFile = open(fileName,accessMode)
#file = open(fileName, accessMode)
#file = open(fileName, mode='w')
#file = open(fileName, module=accessMode)
#file = open(fileName, mode=WRITE)
file = open(fileName, mode=APPEND)

file.write("~Hi there!")
file.write("~How are you doing?")
#output written is >>> "test data~Hi there!~How are you doing?"
file.write("\n Very Well, enjoy your day, it's nice weather out there today~\n Take Care!")
#output after executing these 3 write statements is as below...
#
#test data~Hi there!~How are you doing?~Hi there!~How are you doing?
# Very Well, enjoy your day, it's nice weather out there today~
# Take Care!
#
#make sure to always close the file 
file.close()
print("File written Successfully...")

#test data~Hi there!~How are you doing?~Hi there!~How are you doing?
# Very Well, enjoy your day, it's nice weather out there today~
# Take Care!~Hi there!~How are you doing?
# Very Well, enjoy your day, it's nice weather out there today~
# Take Care!

file = open(fileName,mode=APPEND)
file.write("\n testing re-execution")
file.close()
print("File written Successfully... 3rd attempt")

#executed twice, it falied before 3rd attempt , 

#test data~Hi there!~How are you doing?~Hi there!~How are you doing?
# Very Well, enjoy your day, it's nice weather out there today~
# Take Care!~Hi there!~How are you doing?
# Very Well, enjoy your day, it's nice weather out there today~
# Take Care!~Hi there!~How are you doing?
# Very Well, enjoy your day, it's nice weather out there today~
# Take Care!~Hi there!~How are you doing?
# Very Well, enjoy your day, it's nice weather out there today~
# Take Care!
# testing re-execution