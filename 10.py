#if else statements

a=(int(input("enter your age?\n")))
print("Your age is ",a)

if(a>18):
    print("you can open bank account")
elif(a<18 and a>10):
    print("you can open joint account")
    if(a==17):
        print("you are just one year less than 18")
    elif(a<16):
        print("you are still a teenage")
    else:
        print("you are 16 years old")
else:
    print("you cannot open bank account")