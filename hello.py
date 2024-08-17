print("hello")

def tea(n):
    print(n)

tea(4)



# STRINGS IN PYTHON 
chai = "Masala chai"
slice_chai = chai[0:6]
print(slice_chai)

#to have last value
last_digit =chai[-1]
print(last_digit)

#with hop para =meter
list= "123456789"
hop_para= list[0:10:2]
print(hop_para)

#string methods
lower= chai.lower()
print(lower)

#to remove extra spaces
strip_club =  "     Looks Cool        "
test_Strip = strip_club.strip()
print(test_Strip)

#to replace a word
sexy_chai = "lemon chai"
replaced_chai= sexy_chai.replace("lemon","Elaichi")
print(replaced_chai)

# split method String ko list mai convert krega based on a parameter
split_chai = "Ginger chai, lemon chai, elaichi chai, cinnamon chai"
list_chai = split_chai.split(", ")
print(list_chai)

#find methof jo position dega agar hua toh
print(sexy_chai.find("lemon")) #yeh dega 0 th position
print(sexy_chai.find("ginger")) # yeh error dega -1

#kisi word k count k liye
count_chai = "masala chai chai chai chai"
print(count_chai.count("chai")) # should return 4.

#format method jha placeholder  ki value daalni ho.
order_type = "Masala"
quantity= 2
sentence= "I ordered {} cups of {} chai."
print(sentence.format(quantity,order_type)) # working cool :)

# "".join method to convert a list to a String.
list_fchai= ["masala", "ginger", "elaichi"]
print("-".join(list_fchai))