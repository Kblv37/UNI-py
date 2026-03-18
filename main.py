from funk320QJK import funk320QJK

if __name__== "__main__":
    choice  = input("1 - получение второго значения,")

    if choice == "1":

        #Кобилов

        user_input = input("Введите числа через пробел: ")

        nums = [int(x) for x in user_input.split()]

        result = funk320QJK(nums)

        if result is None:
            print("Второго по величине элемента нет")
        else:
            print("Второй по величине элемент:", result)