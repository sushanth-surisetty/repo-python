salary=input('What is your salary: \t')
bonus=input('what is your bonus: \t')
PayCheckAmount=salary+bonus
print(""" notice here the numbers are concatenated as strings
 input function returns strings, hence they are used as strings
 inorder to convert them into numbers, we have to use number 
 functions such as int(), float() etc.
 """)
print("Total Salary: " + PayCheckAmount)
numericSalary=int(salary)
numericbonus=int(bonus)
PayCheckAmount=numericSalary+numericbonus
print(""" result after using the number functions""")
print("Total Salary: {0:06d}".format(PayCheckAmount))
