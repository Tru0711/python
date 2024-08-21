print("********* DICT METHODS ********")
person = {"name": "Alice", "age": 25} 
print(person)
print(" Accessing value of Name : " , person["name"])
  # Accessing value by key
print(" Accessing value of Age : " , person["age"])
person.clear()
print("clear() : \n", person)
print("-------------------------------------------------------------")
dict1 = {
             "college":"DYPCET",
             "class":"TY",
             "div":"C" 
       }
print("Given Dict : \n",dict1)
print("copy() : \n", dict1.copy())
print("-------------------------------------------------------------")
x = ("key1","key2","key3","key4")
y = (1)
Dict = dict.fromkeys(x,y)
print("fromkeys() : \n", Dict)
print("-------------------------------------------------------------")
print(dict1)
X = dict1.get("class")
print("get() : \n", X)
print("-------------------------------------------------------------")
print(dict1)
Y = dict1.items()
print("items() : \n", Y)
print("-------------------------------------------------------------")
Z = dict1.keys()
print("keys() : \n", Z)
print("-------------------------------------------------------------")
dict1.pop("college")
print("pop() : \n", dict1)
print("-------------------------------------------------------------")
print(dict1)
dict1.popitem()
print("popitem() : \n", dict1)

print("-------------------------------------------------------------")
N = {    "book":"Rare",
         "prize":200,
         "color":"pink"
    }
n = N.setdefault("color","white")
N.setdefault("pages",400)
print("setdefault() : \n", n)
print(N)
print("-------------------------------------------------------------")
print(N)
N.update({"color":"white"})
N.update({"pages":550})
print("update() : \n", N)
print("-------------------------------------------------------------")
print(N)
print("values() : \n", N.values())
print("**********----------------**********-------------------********")








