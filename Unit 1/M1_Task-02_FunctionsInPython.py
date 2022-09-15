def my_function():
    print("Hello from a function")
print("Out of the function")

my_function()


# Function with parameter
def function(fname):
    print(str(fname)+" Reference ")

function("Email")
function("Password")
function(123)
function(1)
function(1.2)


# Arbitary Arguments, *args
def fn(*kids):  # '*' is used to make tuple[-4]
    print(kids[1])

fn("Ravi", "Sumit", "Amit")
fn("Ravi", "Sumit", "Amit","Ankush")
fn("Ravi", "Sumit" )
fn("Ravi", 123)


# Keyword Arguments
def fn2(child3,child2,child1):
    print("The youngest child is "+child3)

fn2(child1 = "Emi",child2 = "Amit ",child3 = "Ravi")


# Default value of a function parameter
def f3(country ="Norway"):
    print("I am from "+country)
f3("Sweden")
f3("India")
f3()
f3("Brazil")


#Passing a list as an argument
def fn(food):
    for i in food:
        print(i)

fruits=['Apple',"Bananan","Cherry",123, 123.4]
fn(fruits)


#return valus
def f5(x):
    return 5*x

print(f5(3))
print(f5(4))
print(f5(5))

def f6():
    pass

f6()