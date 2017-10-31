#to practise workng with dates and time
import datetime
#today is a function that returns todays date
currentDate=datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)
#python doesnot know it has day, month, year values until code is executed
CY=datetime.date.today().year
print(CY)
CD=CY=datetime.date.today()
#formatting date into MM/DD/YYY
print(CD.strftime('%d %b %Y'))
print(CD.strftime('%b %d %Y'))
print(CD.strftime('%B %d %Y'))
print(CD.strftime('%B %d %Y %a'))
print(CD.strftime('%B %d %Y %A'))
print(CD.strftime('month: %B  day: %d  Year: %Y weekday: %A'))
###
