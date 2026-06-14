# List- It is used to store certain set of data
# We can also store different datatypes here
# List is mutable
# marks=[100,45,89,47,84]
# print(marks[0])
# print(type(marks))
# print(len(marks))

# # Assigning new value to the list
# marks[1]=55
# print(marks)

# List Methods- List methods does not return anything

list1=[67,90,100]
# Append method is used to add an element at the end of the list
# list1.append(4)
# print(list1) 

# # Arrange the data into increasing order
# list1.sort()
# print(list1)

# # If we need to arrange the data in descending order
# list1.sort(reverse=True)
# print(list1)

# # Reverse- just reverses the list
# list1.reverse()
# print(list1)

# # Insert- used to insert new element in a list
# list1.insert(2,"mahi")
# print(list1)

# Remove- used to remove an element from the list(only the first occurrence)
# Used to remove element by its value not by index
# list1.remove(100)
# print(list1)

# Pop-used to remove element by its index from the list
# list1.pop(1)
# print(list1)

# Poll question
name="Programming"
print(len(name))

num1= int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3= int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest number is:", num2)
else:
    print("Greatest number is:", num3)
