symbol = input("Введите действие(+,-,*,/):")
numder1 = int(input("Введите первое значение: "))
numder2 = int(input("Введите второе значение: "))
print("Вы получили пример вида", symbol, numder1, numder2 ) 

def exception(symbol):

    if symbol == "+":
        print("Ответ:", numder1 + numder2)
    elif symbol == "-":
        print("Ответ:", numder1 - numder2)
    elif symbol == "*":
        print("Ответ:", numder1 * numder2)
    elif symbol == "/":
        print("Ответ:", numder1 / numder2) 
    else:
        print("some others errors.would be better if you be more careful") 
try:
    exception(symbol)
except (Exception) as e:
    exception("+")
    print(f"ты попал на ошибку {e}")
