1. What are Python’s core data types?
int, float, str, list, tuple, dict, set, bool, NoneType.

chai_types = {"Masala":"spicy", "Ginger":"Zesty", "Green":"Mild"}
print(chai_types)

print(chai_types["Masala"]) #0,1,2 keys will throw error as we have mentioned our own keys here.

chai_types["Green"]= "Healthy" ##here we changed the value from mild to Healthy
print(chai_types)

print(chai_types.items()) #returns the itmes of dict.

print(chai_types.keys()) #returns the keys like masala ginger and green

# print(chai_types.pop("Masala")) ##pops out the mentiond value of the key and removes that from dict

print(chai_types)

#print(chai_types.popitem())

##for chai in chai_types:
 ##  print(chai,chai_types[chai], end=",")

# Other way to access
for key,value in chai_types.items():
    print(key, value, end=", ")

if "Masala" in chai_types:
    print("Haa bhai masala chai hai!!")

chai_types["Earl Grey "] = "Citrus" #Ek naya item add hogya

print(chai_types)

del chai_types["Green"] ## to delete a specific key
print(chai_types)

squar_num= {x:x**2 for x in range(10)}
print(squar_num)
squar_num.clear()
print(squar_num)

##Default Value

keys = ["name", "age", "city"]
default_value = "Unknown"
my_dict = {key: default_value for key in keys}
print(my_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
