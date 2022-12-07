

def funcPrint(userStrint):
  print (userStrint)

#funcPrint("Hello")

def funcSum(a,b):
  c=a+b
  print(c)

#funcSum(13,12)
  
def funcMath(example,answer):
  print (f"Решите пример: {example}")
  b=int(input("Ответ:"))
  if b == answer:
    print (f"Правильно, ответ: {b} Правильный ответ: {answer}")
  else:
    print (f"Неправильно, ответ: {b} Правильный ответ: {answer}")

#funcMath("2+2*3",8)

def funcInfo(name,age,city):
  print (f"Вас зовут {name}, вам {age} и вы живете в городе {city}.")

#funcInfo("Вася Пупкин","18","Москва")

def funcNumber(number):
  if number > 0:
    print("1")
  else:
    print ("-1")

#funcNumber(-2)

def funcString(userString):
  if userString != '':
    print("OK")

#funcString("My string")

def funcNumber2(number):
  if number > 0:
    print("1")
  elif number == 0:
    print ("0")
  else:
    print ("-1")

#funcNumber2(-123)

def funcYear(year):
  if year % 400 == 0:
    print("True")
  elif year % 4 == 0 and year % 100 != 0:
    print ("True")
  else:
    print ("False")

#funcYear (1236)

def funcLen(userString):
  if len(userString) == 4:
    print ("True")
  else:
    print ("False")

#funcLen("1234")


def funcNumString(userString,count):
  var = 0
  while var < count:
    var+=1
    print (f"{var} {userString}")

#funcNumString("yeah",10)

def funcRowSum(row):
  i=1
  s=0
  while i<=row:
    s=i+s
    i=i+1
  print (s)

#funcRowSum(3)

def funcEvenNumbers(a,b):
  for i in range(a, b + 1, 1):
    if i % 2 == 0:
      print(i)

#funcEvenNumbers(1,144)


def funcMultiplesNumber(a,b,c):
  for i in range(a, b, 1):
    if i % c == 0:
      print(i)

#funcMultiplesNumber(123,333,3)
