
name = input("Введите ваше имя:")
age = input("Введите ваш возраст:")
city = input("Введите ваш город:")

str1 = "Вас зовут %s, вам %s и вы живете в городе %s." % (name, age, city)
str2 = "Вас зовут {}, вам {} и вы живете в городе {}.".format(name, age, city)

print (str1)
print (str2)
print (f"Вас зовут {name}, вам {age} и вы живете в городе {city}.")


