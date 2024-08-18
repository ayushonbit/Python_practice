#QUESTIONS ON CONDITIONALS

#1 AGE GROUP CATEGORIZATION

# userage = int( input("Enter your age : ")) #typecasting

if userage <13 :
    print("You are a child")

elif userage >= 13 and userage <= 19:
    print("You are a teenager.")

elif userage >= 20 and userage <= 59:
    print("You are an Adult.")

elif userage >= 60 :
    print("You are a Senior citizen.")


#2 MOVIE TICKET PRICING 

age = int(input("Age btado sir: "))
day = str(input("Kis din dekhni hai movie? "))

price =12 if age>=18 else 8

if day=="Wednesday" or "wednesday":
    price = price-2

print("Your total is " + str(price))


#3 GRADE CALCULATOR

#4 FRUIT RIPENESS CHECKER 
#5 WEAHTHER ACTIVITY SUGGESTION
#6 TRANSPORTATION MODE SELECTION
#7 COFFEE CUSTOMIZATION
#8 PASSWORD STRENGTH CHECKER 
#9 LEAP YEAR CHECKER
#10 PET FOOD RECOMENDATION



