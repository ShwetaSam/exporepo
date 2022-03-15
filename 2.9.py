totalpercentage=int(input("Enter total percentage obtained"))
if(totalpercentage>=90&totalpercentage<100):
    print("Grade: S")
elif(totalpercentage>=85&totalpercentage<90):
    print("Grade: A+")
    elif(totalpercentage>=80&totalpercentage<85):
        print("Grade: A")
    elif(totalpercentage>=75&totalpercentage<80):
        print("Grade: B+")
    elif(totalpercentage>=70&totalpercentage<75):
        print("Grade: B")
    elif(totalpercentage>=65&totalpercentage<70):
        print("Grad: C")
    elif(totalpercentage>=60&totalpercentage<65):
        print("Grade: C+")
    elif(totalpercentage>=55&totalpercentage<60):
        print("Grade: D")
else:
    print("Grade: F")
