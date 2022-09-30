# String are Immutable in Python:

"""
An immutable object is a object whose cotent ca not be changed
In python: strings, numbers ad tuples are immutable
"""

s1 = 'one'
s2 = 'two'

s1 = s2

print(s1)


#Replacing a substring

str = "That is beautiful"
s1 = 'beautiful'              #Logic???????
s2 = 'not beautiful'

str1 = str.replace(s1,s2)
print(str1)



#Split Function
str = "That is beautiful"
str1 = str.split(' ')
print(str1) #here str1 is not a string but list container

for i in str1:
    print(i)

#cahnging case of a string 
str = "That is beautiful"
print(str.upper())
print(str.lower())


# Superscript and Subscript concept in Python
numbers_to_letters = str.maketrans("123", "ABC")
print("Question 1, point 2 and 4".translate(numbers_to_letters))

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
print("C2H5OH".translate(subscript))

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
print("PIr2".translate(superscript))

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
print("PIr2".translate(superscript).replace('PI', 'π'))