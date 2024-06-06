def count_words(text):
  words = text.split()
  lenth=(len(words))
  Joined ="".join(words)
  Upper= Joined.upper()
  return lenth,Joined,Upper
 

# print(count_words("i am on my way home "))
     
     

# a= "I am a good man".split()
# print(a)
# print("".join(a).upper())
