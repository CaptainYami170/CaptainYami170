num = int(input("ENTER THE VALUE: "))
if(num < 0):
    print("NUMBER IS NEGATIVE !")
elif(num > 0):

    if (num <= 10):
        print("NUMBER IS IN BETWEEN 1 TO 10")
    elif(num > 10 and num <= 20):
        print("NUMBER IS IN BETWEEN 10 AND 20")
    elif(num > 20 and num <= 50):
            print("NUMBER IS IN BETWEEN 20  ND 50")
    elif(num >50 and num <=100):
            print("NUMBER IS IN BETWEEN 5O TO 100")
    else:
            print("NUMBER IS GREATER THAN 100")

else:
    print("NUMBER IS ZERO !")

input("") 






