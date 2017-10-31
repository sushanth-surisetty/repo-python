import datetime
CD=CY=datetime.date.today()
userInput=input('Please enter your birthday (MM/DD/YYYY): \t')
birthday=datetime.datetime.strptime(userInput, '%m%d%Y')
print(birthday)
B_DT=datetime.datetime.strptime(userInput, '%m%d%Y').date()
days=B_DT - CD
print(days)
print(days.days)