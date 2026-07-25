#if else

# a = 13

# if a > 10:
#     print("a is greater then 10")

# else:
#     print("a is less then 10")


# money = int(input("please provide me money :-"))

# if money == 10:
#     print(" i will have the ice-cream")

# elif money == 20:
#     print("i will have the chocolate")

# elif money == 30:
#     print("i will have the cake")
    
# else:
#     print("i will have the water")




# num1 = int(input(" tell me first number"))
# num2 = int(input(" tell me second number"))

# if num1 > num2:
#     print(f"{num1} is greater then {num2}")

# elif num2 > num1:
#     print(f"{num2} is greater then {num1}")

# else:
#     print(" Both the number sare same")




# gen = input("please provide me your gender as character(M or F):-")

# if gen == "M" or gen == "m":
#     print("Good Moring Sir")

# elif gen == "F" or gen == "f":
#     print("Good Moring Ma'am")

# else:
#     print("unknown gender")

# num = int(input("please provide me number:-"))

# if num % 2 == 0:
#     print(" even number")
# else:
#     print(" odd number")    


# num = input("please provide your name :-") 
# age = int(input("now provide your age :-"))

# if age >= 18:
#     print(f"Hello {num} you are a valid voter")
# else:
#     print(f"Hello {num} you are not a valid voter")


#leap year
# year = int(input("tell your year:-"))
# if year % 100 == 0 and year % 400 == 0:
#     print("its a leap year")


# elif year %100 != 0 and year % 4 == 0:
#     print("its a leap year")

# else:
#     print("its a normal year")


#if- elif ladder
temp=int(input("tell me the temperature:- "))

if temp < 0:
    print("freezing weather")

elif temp >= 0 and temp < 10:
    print("very cold weather")


elif temp >= 10 and temp < 20:
    print("cold weather")


elif temp >= 20 and temp < 30:
    print("normal weather")

elif temp >= 30 and temp < 40:
    print("hot weather")

else:
    print("very hot weather")



