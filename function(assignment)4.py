def ASSIGN():
    marks=int(input("Enter the marks :"))
    if marks>=80:
        Grade=("A")
    elif marks<80 or marks>=65:
        Grade=("B")
    elif marks<65 or marks>=50:
        Grade=("C")
    else:
        Grade=("D")
    print("Grade:",Grade)
    return

ASSIGN()
