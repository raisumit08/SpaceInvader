x = int (input("Enter an integer: "))

#If else statemeny
if x < 0:
    print("Less than zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")


# For statements [The range() Function]
for i in range(0,5,2):
    print(i)

# While loop statement [Values in reverse order]
while(x>=1):
    print(x)
    x-=1

#break and continue Sattements, and else clauses on loops

n = 7
count = 0
for x in range(2,n):
    if n % x == 0:
        print("Not a prime")
        count+=1
        break
    else:
        continue
if count == 0:
    print("It is a prime number")

#The pass statement
from subprocess import check_output


def initlog():
    pass

initlog()

# while True:
#     pass


#match Statements
cpuModel = str.lower(input("Please enter your CPU model: "))

#The match statement evaluates the variable's value
match cpuModel:
    case "celeron":
        print("Forget about it and play minesweeper instead")
    case "core i3":
        print("Good luck with that")
    case "core i5":
        print("Yeah, you should be fine.")
    case "core i7":
        print("Have fun!")
    case "core i9":
        print("Our team designed nice loading screens")
    case _:
        print("Is that even a thing?")

# Short circuit (lazy evaluation) {minimal evaluation}
"""
When evaluating an expression that involves the or operator  result 
Python can sometimees determine the result without evaluating all the operands
This is called short-circuit evaluation or lazy evaluation
"""

is_admin =  False
is_editor = True
can_edit = is_admin or is_editor

print(can_edit)