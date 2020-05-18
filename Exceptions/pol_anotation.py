symbol = input("Введите польскую нотацию ")

def exception(symbol):
    i = symbol.split(' ')
    sym = i[0]
    assert sym in ['+', '-', '/' , '*'], "Ошибка ввода"
    try:
      n1 = int(i[1])
      n2 = int(i[2])
    except Exception as e:   
      print("Ошибка", e) 
      return (symbol) 
    if sym == "/":
      try:
        print (n1/n2)
      except ZeroDivisionError as e:   
        print("Ошибка", e)
    if sym == "*":
      print (n1*n2)
    elif sym == "-":
      print (n1-n2)
    elif sym == "+":
      print (n1+n2)      
    
exception(symbol)