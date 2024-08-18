# Objects/Datatypes

- [] => Square Brackets, () => Parentheses, {} => Braces or Curly Braces

- Number : 1234, 01b234, 3+4j, 0b111, Decimal(), Fraction()

-  String : 'Spam', "Bob's", b'a\x01c'

- List : [1,2,[4,5,'Six'], 7,8,9]

- Tuple - (1,'Spam',2,4,''U) Tuple('Spam') namedtuple

- Dictionary: {'Food':'Spam', 'Taste':Yum,}, Dict(hours:10) // Key value Pair

- Set: Set(abc), Set(a,b,c) // it basically stores your unique value

- File : open('eggs.txt'), open('path to file')

- Boolean: True or False

- None: None (No response)

- Functions, Modules, Classes, Instances

- Advance: Decorators, Generators, Iterators, Metaprogrammg

## INTERNAL WORKING OF PYTHON.

- Numbers and Strings are treated a bit differently in python. Ref_count is always there but abstracted.

- Garbage collection of numbers and strings are quite late, anyway forceful collection is still a option.

- The data type of a variable is always assigned in mememory rather than that specific variable.

- In python before calculation all the value of refences are collected then it goes for computed calculation.

- After calculation new object is created in the memory and the resulant value of the calculated sum is assigned.

-- COMING TO LIST --

. MyListOne = [1,2,3]
. MyListTwo = MyListOne

- When we assign same item twice on two different list it will be assigned as different references. mtlb ki alag alag bn jaega ref 2 baar assign krne pe.

- Lekin aga hum L1= L2 de toh same ko point krega aur agar hum L1 ko change kre toh L2 k values mai relfect krega woh change and this is not same with above case.

- Usually in Production it is Written as :

- h1 =[1,2,3]
- h2 = h1[:] // by this colon (:) we mean tha slice the h1 list from start to end anyway we can mention the index if we need to. 

- One thing to notice is that we could have directly assigned the value but we are not doing that here because by this way we have created a COPY  of that list.

- Apart from this we also have a copy module to copy and Deep copy stuff.

- >> import copy
- >> h2 = copy.copy(h1) or copy.deepcopy(h1) // list k andar lsit.

- One Important thing is that agar hume values check karni hai just value toh hum Value1 == value2 kar skte hai.

- Lekin humein yeh check krna hai ki memory k andar bhi same reference hai ki nhi toh hum krengay, "value1 is value2".

## NUMBERS IN DEPTH IN PYHTON

-  Numbers is a strong game in python. Number is not a single object but a group of objects.

- ** -> Power
- % -> Modulo remainder
- // -> floor dividion mtlb quotient dega.
- READ AVOUT REPL STR AND PRINT.
- Booleans are treated as Numbers 0 & 1s.
- 1==2<3 can also be written as 1==2 and 2<3 which returns false.
- import math (library for numbers).
- Math.floor(3.5) => 3 (gives closest number below value) bottom value.
- Math.trunc() => takes towards zero.
- Complex numbers or iota numbers are also dealt 2+ij.
- We do have square root methods and power methods.
- import random
- random.random(), random.randint(1,100), random.choice([1,2,3,4])

- To play around **decimal values**:
   >> from decimal import Decimal;
   >> Decimal(0.1) + Decimal(0.1) + Decimal(0.1) gives Decimal(0.3) without decimal this gives error.
-  **Decimal context manager** 

- To play with **fractions**
  >> from fraction import Fraction
  >> myFra = Fractions(2,7)
  >> myFra

**SETS**
- & is used for intersection.
- Setone = {1,2,3,4}
- Settwo = {1,3}
- setone & settwo gives {1,3}

- | is used for union.
- Setone = {1,2,3,4}
- Settwo = {1,3}
- setone & settwo gives {1,2,3,4}
- setone - {1,2,3,4} gives set() which is empty set not {} cus these braces are for dict.
- True is 1. (returns false with a error)

### STRINGS IN PYTHON.

- chai = "Masala Chai"
- Suppose we have to take MASALA out, then we will just slice out from 0 till n+1;
- Syntax would be : Slice_Chai = chai[0:6];
-as seen above we have 2 para meters inside the bounds but we also have a 3rd parameter called hop parameter.

**String Methods**
1. chai.lower()
2. chai.upper()
3. chai.strip() //to remove extra spaces
4. chai.replace("Kisko", "kiss say") //it takes 2 parameters i.e kisko and kiss say.
5. chai.split() // yeh string ko list mai convert krega based on a parameter that is given like  ", "
6. "".join(chai_list) //"".join method to convert a list to a String aur " " isme jo hoga woh hoga beech m har char k.
7. chai.find() // yeh position batega jaha par woh word ya character present hai aur nhi mila toh -1.
8. chai.count() // kisi word k count ko dega string say.
9. chai.format() // isme hum ek sentence mai dynamic value aur type dalwa skte hai jaise for example: I ordered {} cups of {} chai. yha par value assign ho jaegi using this aur, isko {} placeholder bolte hai.
10. chai .len // to find the length of string.
11. Raw String => r"andar jo bhi likhna ho" //iss say yeh hoga ki compiler ko confusion nhi hoga aur as it is stirng print krdega.
12. containing questions we can ask in string.
13. chai.append("oolong")// to add at the end

## LIST IN PYTHON 
- tea_Varieties= ["Green","Black","Oolong","White"]

- tea_varieties[0:2]=["Elaichi","Adrak"] // Array k form mai pass krengay warna woh "L", "E","M", "O", "N" hi jaega 

- tea_varieties[1:1] return karega [] lekin agar hum

- tea_varieties[1:1]= ["test", "test"] kare toh 0 index k baad insert hoga.

- tea_varieties.append("oolong") // to add at the end of the list.

-  tea_varieties.pop() //last ka element return krdega list say aur list mutable hai toh remove bhi hojaega

- tea_varieties.remove("") // keyword str remove krdega

- tea_varities.insert(index, "string") //inserts at the specific index

- tea_varieties.copy() // it is used to create a copy with different reference in memory.

Function // Description

1. append()

Adds an element to the end of the list

2. extend()

Adds more than one element to the end of the list

3. insert()

Adds an element in between the list

4. remove()

Removes an elements from the list

5. pop()

Removes the last elements from the list

6. slice()

Prints a section of the list

7. reverse()

Reverses the order of the elements in a list

8. len()

Gives the length of a list

9. min()

Gives the minimum element (by value) of a list

10. max()

Gives the maximum element (by value) of a list

11. count()

Counts the number of copies in a list

12. Concatenate

Combines two list

13. Multiply

Multiplies the occurrence of elements in a list

14. index()

Gives index number of an element in the list

15. sort()

Sorts the list in ascending order

16. clear()

Clears every element in a list

**List Comprehension**

- Squared_num = [x**2 for x in range(10)] // that means sqaure krdo 1 say 10 tak k numbers ka






    























