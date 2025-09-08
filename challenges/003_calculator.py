#variables
num1 = 10
num2 = 0
oper = "/"

#header
def hashtag():
    print("####################################")

hashtag()
print("Calculadora mais boçal de todas")
hashtag()

#switch
if oper == "+":
    print(num1 + num2)

elif oper == "-":
    print(num1 - num2)

elif oper == "*":
    print(num1 * num2)

elif oper == "/":
    if num2 == 0:
        print("pode n, man...")
    else:
        print(num1 / num2)

else:
    print("Oq caralhos tu digitou?!")