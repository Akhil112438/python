#for loop
# a= range(1, 15, 1)

# for i in a:
#     print(i)

# for i in range(2, 16, 2):
#     print(i)

#forword loop
# for i in range(15):
#     print(i)

# for i in range(15,46):
#     print(i)

# backword loop
# for i in range(15,0,-1):
#     print(i)

#forword loop in negative
# for i in range(-3,-16,-1):
#     print(i)


#Lets print the table of 10 using for loop
# n = int(input("which table you want: "))
# for i in range(n, (n * 10) + 1, n):
#     print(i)


#Loop for string
# a = "MISBAH"
# for i in range(7):
#     print(a[i])


#lenth of string
# a = "MISBAH IS A BME ENGINEER"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])

# a = "MISBAH IS A BME ENGINEER"
# for i in a:
#     print(i) 


#Break statement

# for i in range(1, 21):
#     if i == 15:
#         break
#     else:
#         print(i)

# for i in range(1, 21):
#     if i == 25:
#         print("Break statement is executed")
#         break
#     print(i)
# else:
#     print("break statement is not executed")


#continue statement

# for i in range(1, 21):
#     if i == 15:
#         print("Continue statement is executed")       
#         continue
#     print(i)



#for loop questions
# n = int(input("enter the number:"))

# for i in range(n):
#     print(" Misbah is a Biomedical Engineer")

#natural numbers to n
# n = int(input("enter the number:"))
# for i in range (1,n+1):
#     print(i)

#reverse natural numbers to n
# n = int(input("enter the number:"))
# for i in range(n,0,-1):
#     print(i)


# n = int(input("which table you want: "))

# for i in range(1, 11):
#     print(f"{n}*{i} = {n*i}")


# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
#     print(f"your sum is {sum}")


# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
#     print(f"your factorial is {fact}")


# n = int(input("Tell your number: ")) 
# even = 0 
# odd = 0 

# for i in range(1, n+1): 
#     if i % 2 == 0: 
#         even = even + i
#     else: 
#         odd = odd + i

# print(f"Your even and odd count are {even}, {odd}")


# n = int(input("which number factors you want:"))

# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)



n = int(input("chake your number is perfect or not:- "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("your number  is perfect ")
else:
    print("your number is not perfect ")