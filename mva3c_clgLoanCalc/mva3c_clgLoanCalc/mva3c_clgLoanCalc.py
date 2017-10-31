LoanAmt=input("Please enter your Loan Amount: \t")
IntRate=input("Please enter your Loan Interest Rate: \t")
NoOfPayments=input("How many payments would you like to schedule: \t")
##
L=float(LoanAmt)
i=float(IntRate)
n=int(NoOfPayments)
M=L*(i*(1+i)*n)/((1+i)*n-1)
print("\nYour Scheduled Monthly EMI would be "+\
    "{0:.2f}".format(float(M)))