# Data ={"state":"Lagos","name":"wale"}
# print(Data)
# print(len(Data))
# print(Data.keys())
# print(Data.values())
# print(Data["name"])

# Nigeria={"Lagos":"Ikeja","Edo": "Benini" ,"Kano": "Kano"}
# print(Nigeria)
# print(Nigeria["Lagos"])
# print(Nigeria["Kano"])
# Nigeria["Lagos"] = "vi"
# Nigeria["Edo"]= "Epoma"
# print(Nigeria)
# Nigeria.update({"Oyo":"Ibadan"})
# print(Nigeria)

# US ={"Texas":"Dallas" ,"Oklahoma": "OKC","New_york":"NYC"}
# print(US)
# # print(US.items())
# # del US["Texas"]
# # print(US)

# for x in US:
#     # print(x)
#     # print(US[x])
#     print(x , US.get(x))




# student = {'name': 'John', 'age': 16, 'courses': ['Math', 'CompSci']}
# print(student["name"])
# print(student["courses"])
    
# Data ={"Name":"Wale","Age":30,"Color": "Blue","Sex": "Male"}
# print(Data)
# Data.update({"National":"Ghana"})
# print(Data)

# mydict={"name":"miracle"}
# mydict=dict({"name":"miracle"})
# mylist=list([2,3,4,56,7])
# print(mylist)
# print(mydict)

#nested dict
# smallDict={
#            "item": [2,3,4,5,6],"educated":True,"num ":4,
#            "details":{"sex":"male","age":45,"status":"married"}}
# print(smallDict)
# print(smallDict["details"]["sex"])
# print(smallDict["details"])
# print(smallDict["details"].items())
# print(smallDict["details"])

# print(smallDict["details"].update({"Religion":"Christian"}))
# print(smallDict["details"])

#Tuple

# firstTuple=("apple","banana","cherry","paw paw")
# print(firstTuple)
# print(len(firstTuple))
# print(firstTuple[1:])

# for x in firstTuple:
#     print(x)

# #to convert to list
# ylist = list(firstTuple)
# ylist.append("pineApple")
# secondTuple=tuple(ylist)
# print(secondTuple)

# MyTuple=("Mazda","Toyota,","Honda","Lexus")
# print(MyTuple)
# # # print(MyTuple[2])
# # zlist=list(MyTuple)
# # zlist.append("Volvo")
# # NewTuple=tuple(zlist)
# # print(NewTuple)

# SecondTuple=("Banana","Mango","Orange")
# # CombinedTuple= MyTuple + SecondTuple
# # print(CombinedTuple)
# #or
# MyTuple += SecondTuple
# print(MyTuple)

#To unpackING it

# (Banana,Mango,Orange)=SecondTuple
# print(Banana)
# print(Mango)
# print(Orange)
# print(SecondTuple)

# (*Banana, )=SecondTuple




# Country={"Nigeria":"Abuja","Ghana": "Accra" ,"England": "London"}
# print(Country)
# mylist=[]
# secondlist=[]
# for x in Country:
#     print(x)
#     mylist.append(x)
#     secondlist.append(Country[x])
# # print(mylist)
# # print(secondlist)

# # # #to convert to list
# CountryTuple=tuple(mylist)
# CapitalTURPLE=tuple(secondlist)
# print(CountryTuple)
# print(CapitalTURPLE)

# Country={"Nigeria":"Abuja","Ghana": "Accra" ,"England": "London"}
# # print(Country)
# # for x in Country:
# # #     print(x)

# # CountryTU=tuple(Country)
# # print(CountryTU)

# Country.items()
# mylist =(Country.items())
# print(mylist)
# for(a,b) in mylist:
#     # print (a)
#     print (b)