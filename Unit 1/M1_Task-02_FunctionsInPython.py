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
def fn(*kids):
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
