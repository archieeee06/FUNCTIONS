def CALCFARE():
    cartype = (input("Enter the cartype :"))
    if cartype =="small":
        fare = 1000
    elif cartype == "van":
        fare = 800
    elif cartype == "suv":
        fare = 2500
    
    print("fare:",fare)
    return

CALCFARE()
