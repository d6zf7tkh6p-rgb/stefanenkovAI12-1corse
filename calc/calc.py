while True:
    print("калькулятор путешественника")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (**)")
    print("6. Остаток от деления (%)")
    print("7. Целочисленное деление (//)")
    print("0. Выход")
    choice = input("Выберите действие: ")
    if choice == "0":
        print("Программа завершена")
        break
    if choice in ["1", "2", "3", "4", "5", "6", "7"]:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if choice == "1":
            result = a + b
        elif choice == "2":
            result = a - b
        elif choice == "3":
            result = a * b

        elif choice == "4":
            if b != 0:
                result = a / b
            else:
                print("На ноль делить нельзя!")
                continue
        elif choice == "5":
            result = a ** b
        elif choice == "6":
            if b != 0:
                result = a % b
            else:
                print("На ноль делить нельзя!")
                continue
        elif choice == "7":
            if b != 0:
                result = a // b
            else:
                print("На ноль делить нельзя!")
                continue
        print("Результат:", result)
        if result > 10000:
            print("Проверь бюджет поездки")
    else:
        print("Неверный выбор!")