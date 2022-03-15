rate=0.20
sd=10000.0
dd=3000.0
grossincome=float(input("enter gross income"))
dependents=int(input("enter no. of dependents"))
taxincome=grossincome-sd-dd*dependents
print("taxincome=",taxincome)
tax=taxincome*rate
print("tax="+str(tax))
                         
