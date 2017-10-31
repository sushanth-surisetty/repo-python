fileName='UserInfo.txt'
WRITE='w'

data=input("Please enter some information about you...\t:")
file=open(fileName, mode=WRITE)
file.write(data)
file.write("\nfile Closed ... ")
file.close
print("\nThanks for your patience, our Associate will get back to you shortly.")
