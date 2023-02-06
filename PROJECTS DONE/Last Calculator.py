def operation(zn, opn):
    if (opn == "+"):
        print(sum(zn))
    elif (opn == "-"):
        print(sub(zn))
    elif (opn == "*"):
        print(mul(zn))
    elif (opn == "/"):
        print(div(zn))
    else:
        print("Invalid input , Thank you")
    ifneedmore()

###################################


def sum(zs):
    result = float(0.0)
    for i in range(len(zs)):
        result = zs[i]+result
    return result


def sub(zb):
    result = float(0.0)
    for i in range(len(zb)):
        result = zb[i]-result
    return result


def mul(zm):
    result = float(1.0)
    for i in range(len(zm)):
        result = zm[i]*result
    return result


def div(zd):
    result = float(1.0)
    for i in range(len(zd)):
        result = zd[i]/result
    return result


def ifneedmore():
    new = input("Do you need another calcualtions (yes / no):").lower()
    if (new == "no"):
        print("Thank You for using our calculator 💕💕")
    elif (new == "yes"):
        newoperation()
    else:
        ifneedmore()


def newoperation():
    numofele = int(input("Enter the number of elements :"))
    z = []

    for i in range(0, numofele):
        ele = float(input("Enter the element : "))
        z.append(ele)

    op = input("What is the operation + , - , * , / : ")


######################
print(" Hello in Metcha Calculator")
numofele = int(input("Enter the number of elements :"))
z = []

for i in range(0, numofele):
    ele = float(input("Enter the element : "))
    z.append(ele)
op = input("What is the operation + , - , * , / : ")

operation(z, op)
