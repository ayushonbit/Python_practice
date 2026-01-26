#Comprehensions are a concise way to create lists, sets, or dictionaries in Python. They provide a syntactic shortcut for generating these collections from existing iterables.
# Here are examples of list, set, and dictionary comprehensions: single line of code doing many things
# where they are useed in real world: data processing, filtering, transforming data, generating sequences, etc.
# purpose ?? to make code more readable and concise and faster
# Types of comprehensions:
# 1. List Comprehensions
# 2. Set Comprehensions
# 3. Dictionary Comprehensions
# 4. Generator Expressions (not exactly comprehensions but similar in concept) --Annotations in Java is similar to this

#LIST COMPREHENSIONS
menu = ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Lemon Tea", "Black Coffee"]

iced_tea = [tea for tea in menu if "Chai" in tea] #filtering teas with "Chai" in their names.
print("Iced Tea Options:", iced_tea)


#SET COMPREHENSIONS
fav_chai = ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Lemon Tea", "Black Coffee", "Ginger Chai"]
unique_tea_lengths = {tea for tea in fav_chai} #getting unique lengths of tea names
print("Unique Tea Name Lengths:", unique_tea_lengths)

recipes= {
    "Masala Chai": ["Tea Leaves", "Milk", "Sugar", "Spices"],
    "Ginger Chai": ["Tea Leaves", "Milk", "Sugar", "Ginger"],
    "Cardamom Chai": ["Tea Leaves", "Milk", "Sugar", "Cardamom"],
    "Lemon Tea": ["Tea Leaves", "Lemon", "Sugar"],
    "Black Coffee": ["Coffee Beans", "Water", "Sugar"]
}

unique_spices =(spice for ingredients in recipes.values() for spice in ingredients if spice  in ingredients) #getting unique spices used in all chai recipes

print("Unique Spices Used in Chai Recipes:", unique_spices)


#DICTIONARY COMPREHENSIONS
chai_prices = {"Masala Chai": 30, "Ginger Chai": 25, "Cardamom Chai": 35, "Lemon Tea": 20, "Black Coffee": 40}
expensive_chai = {tea: price for tea, price in chai_prices.items() if price > 30} #filtering teas with prices greater than 30
print("Expensive Chai Options:", expensive_chai)

tea_prices_inr = {"Masala Chai": 30, "Ginger Chai": 25, "Cardamom Chai": 35, "Lemon Tea": 20, "Black Coffee": 40}
tea_prices_usd = {tea: price * 0.013 for tea, price in tea_prices_inr.items()} #converting prices from INR to USD
print("Tea Prices in USD:", tea_prices_usd)


#GENERATOR EXPRESSIONS
daily_sales = [150, 200, 250, 300, 350]
total_revenue = sum(sale for sale in daily_sales) #calculating total revenue using generator expression, it is memory effiecient
print("Total Revenue:", total_revenue)






