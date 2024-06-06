# try:
#     print(1234)
# except:
#     print("There was an error")
# else:
#     print("Every thing is okay")    
# finally:
#     print("Everything is over")    


# def calc(a,b):
#      try:
#           c=a % b
#      except:
#           print("not working")
#      else:
#           return c     
     
# print(calc("3", "5"))
     

# def calc(a,b):
#      try:
#           c=a % b
#      except:
#           print("not working")
#      else:
#           return c     
# try:
       
#  user = int(input("put a number"))
#  seconduser =int(input("second number"))
# except:
#    print("mistake")
# else:
#     print(calc(user,seconduser))    
    
# mixed_data= [4,5,6,"five","one"]
# def suma(mixed_data):
#  try:
#     Data = sum(mixed_data)
#  except:
#    print("Wrong imput")
    
#  else:
#     print(Data)

# print(suma(mixed_data))   

# mixed_data = [4,5,6,"five","one"]
# def suma(mixed_data):
#  try:
#     Data = sum(mixed_data)
#  except:
#    print("Wrong imput")
#  else:
#     print(Data)
# print(suma(mixed_data))


# def sum_numeric_elements(mixed_list):
#     total_sum = 0  # Initialize the sum to 0
#     for element in mixed_list:
#         try:
#             # Attempt to add the element to the total_sum
#             total_sum += element
#         except TypeError:
#             # If a TypeError is raised (non-numeric type), skip this element
#             print(f"Skipping non-numeric type: {element}")
#     return total_sum

# # Example usage
# mixed_data = [1, 2.5, 'text', 3, 'another string', 4.5]
# result = sum_numeric_elements(mixed_data)
# print(f"Sum of numeric elements: {result}")

   

# try:
#     f = open("nine24.py")
#     f.write("This should throw an error")
# except:
#     print("The write method is not supported")    
# else:
#     f.close()   


# x=0   
# while (x < 5):
#     print("you are good")
#     x += 1
# else:
#     raise Exception("Not good enough")    
   
mylist = [1,2,3,4,5,6,7,8,8,10]
try:
    for y in mylist:
        if y == 5:
         raise Exception("Try again") 
        else:
           print(y)  
except:
    print("Not good")
 

         
    