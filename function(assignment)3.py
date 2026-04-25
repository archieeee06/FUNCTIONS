def checkgender():
    a=input("Enter the gender:")
    if a=='m' or a=='M':
        message=("male")
    elif a=='f' or a=='F':
        message=("female")
    else:
        message=("transgender")
    print("message:",message)    
    return

checkgender()
