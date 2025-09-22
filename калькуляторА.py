print("Привет! Это калькулятор!")
while True:
    print("\n" + "-"*20)
    
    # Ввод чисел
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    
    # Выбор операции
    print("Выберите операцию:")
    print("1) + сложение")
    print("2) - вычитание")
    print("3) * умножение")
    print("4) / деление")
    
    choice = input("Ваш выбор (1-4): ") 
    
    # Вычисление
    if choice == "1":
        result = a + b
        print(f"{a} + {b} = {result}")
    elif choice == "2":
        result = a - b
        print(f"{a} - {b} = {result}")
    elif choice == "3":
        result = a * b
        print(f"{a} * {b} = {result}")
    elif choice == "4":
        if b == 0:
            print("Ошибка! Нельзя делить на ноль!")
        else:
            result = a / b
            print(f"{a} / {b} = {result}")
    else:
        print("Неверный выбор!")
    
    # Продолжить или выйти
    if input("Еще раз? (да/нет): ").lower() != "да":
        print("Пока!")
        break