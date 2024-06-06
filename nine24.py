# def name_generator(name):
#       print("provide a name")
#       return(name)

# name_generator("wale")

# def my_function(first_name,second_name,third_name):
#     print(first_name,second_name,third_name)


# my_function("Olawale" ,"Omoyeni","Oluwaseun")   

# def my_function(first_name,second_name,third_name):
#     print(first_name,second_name,third_name)

# my_function(third_name="Olawale" ,second_name="Omoyeni",first_name="Oluwaseun") 


# def my_function(first_name,second_name,third_name="None"):
#     print(first_name,second_name,third_name)

# my_function(third_name="Olawale" ,second_name="Omoyeni",first_name="Oluwaseun") 


# Fruit =["Pineapple","Apple","Paw Paw","Citrus","Orange","Guava"]
# for y in Fruit:
#     print(y)

 #Function that take a list

# Fruits =["Pineapple","Apple","Paw Paw","Citrus","Orange","Guava"]
# def function_for_fruits(list):
#     for x in list:
#         print(x)
#         return list

#  #function_for_fruits(Fruits)        
    
# # cars =["Pineapple","Apple","Paw Paw","Citrus","Orange","Guava"]
# # function_for_fruits(cars)
        
# cars =["Pineapple","Apple","Paw Paw","Citrus","Orange","Guava"]
# print(function_for_fruits(cars))


# def triangle(base, height):
#     area = base * height / 2
#     return area

# print(triangle(base=4, height=10))

#gettting a maximum and minimum value
# def my_function(list):
#     max= list [0]
#     min= list [0]
#     for x in list:
#         if x > max:
#             max = x
#         elif x < min: 
#             min = x
#     return max , min          
    
# list_of_num=[1,2,3,4,5,6,7,8,9,10]  
# second_list_of_num=(15,16,17,18,19,20)  
# print(my_function(list_of_num)) 
# print(my_function(second_list_of_num))

#AVERAGE NUMBER
# def my_function(list):
#     total = sum(list)
#     add = 0
#     for x in list:
#         add += x
#     print(add,total)
#     avg =total / len(list)
#     return avg

# print(my_function(list_of_num)) 

#cal Cylinder_volume


# def Cylinder_volume(radius, height):
#     pi=3.214
#     volume = pi * radius*radius * height
#     return volume

# print(Cylinder_volume(radius=10, height=8))


##Create a function check_password(password) that takes a password as input and checks its strength based on criteria (e.g., minimum length, presence of uppercase, lowercase, and numbers).
#Use len() to check length, string methods like isupper(), islower(), and isdigit() for character types, and if-elif-else statements for logic.
#Give appropriate feedback about the password's strength (e.g., "Weak", "Moderate", "Strong").
 

# def check_password(password):
#     length = len(password)
#     no_of_upper_case_characters = 0
#     no_of_lower_case_characters = 0
#     no_of_digits = 0
#     for x in password:
#         if x.isupper():
#             no_of_upper_case_characters += 1
#         elif x.islower():
#             no_of_lower_case_characters += 1
#         elif x.isdigit():
#             no_of_digits += 1
#     print("The length of your password is: ", length)
#     print("The Number of lowercase characters in your password is: ", no_of_lower_case_characters)
#     print("The Number of uppercase characters in your password is: ", no_of_upper_case_characters)
#     print("The Number of digits in your password is: ", no_of_digits)
#     return password



# password = input("Put in your Password: ")
# check_password(password)   
#method 2     

# def check_password(password):
#     length = len(password)
#     no_of_upper_case_characters = 0
#     no_of_lower_case_characters = 0
#     no_of_digits = 0
#     for x in password:
#         if x.isdigit():
#             no_of_digits += 1
#         else:
#           if x.islower():
#             no_of_lower_case_characters += 1
#           elif x.isupper():
#             no_of_upper_case_characters += 1
#     print("The length of your password is: ", length)
#     print("The Number of lowercase characters in your password is: ", no_of_lower_case_characters)
#     print("The Number of uppercase characters in your password is: ", no_of_upper_case_characters)
#     print("The Number of digits in your password is: ", no_of_digits)
#     return password



# password = input("Put in your Password: ")
# check_password(password)

#String formating

# def check_password(password):
#     length = len(password)
#     no_of_upper_case_characters = 0
#     no_of_lower_case_characters = 0
#     no_of_digits = 0
#     for x in password:
#         if x.isdigit():
#             no_of_digits += 1
#         else:
#           if x.islower():
#             no_of_lower_case_characters += 1
#           elif x.isupper():
#             no_of_upper_case_characters += 1
#     print(f"The length of your password is: {length}" )
#     print(f"The Number of lowercase characters in your password is: {no_of_lower_case_characters}")
#     print(f"The Number of uppercase characters in your password is: {no_of_upper_case_characters}" )
#     print(f"The Number of digits in your password is: {no_of_digits}")
#     return password



# password = input("Put in your Password: ")
# check_password(password)

#setuation where 1 parameter is handling all argument

# def my_function(name):
#     print(name)

# my_function("wale")  

# def my_function_second():
#     print("1 am good")

# name = "Miracle"    

# def my_function(first_name ,last_name,):
#     print(first_name+last_name)

    
# my_function(first_name="Olawale", last_name="Omoyeni")



def addition(a,b):
    result = a + b
    return result

def subtraction(a,b):
    if a > b:
     result = a - b
    else:
     result = b - a
    return result

def division(a,b):
    if a > b:
     result = a / b
    else:
     result = b / a
    return result

def multiplication(a, b):
    result = a * b
    return result