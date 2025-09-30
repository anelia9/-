print("Привет! Это калькулятор!")
print("\n" + "-"*20)
    
a = float(input("Первое число: "))
b = float(input("Второе число: "))

choice = input("Введите знак операции: ")
    
if choice == "+":
    result = a + b
    print(a,"+",b,"=",result)
elif choice == "-":
    result = a - b
    print(a,"-",b,"=",result)
elif choice == "*":
    result = a * b 
    print(a,"*",b,"=",result)
elif choice == "//" and b!=0:
     result = a // b
     print(a,"//",b,"=",)
elif choice == "%" and b!=0:
    result = a % b
    print(a,"%",b,"=",result)
elif choice == "**":
    result = a ** b
    print(a,"**",b,"=",result) 
elif choice == "/" and b!=0 :
    result = a / b
    print(a,"/",b,"=",result)
else:
    print("Неверный выбор!")

    if choice == "==":
        result = a == b
        print(a,"==",b,"=",result)
    elif choice == "!=":
        result = a != b
        print(a,"!=",b,"=",result)
    elif choice == ">":
        result = a > b 
        print(a,">",b,"=",result)
    elif choice == "<":
        result = a < b
        print(a,"<",b,"=",result)
    elif choice == ">=":
        result = a >= b
        print(a,">=",b,"=",result)
    elif choice == "<=":
        result = a <= b
        print(a,"<=",b,"=",result)