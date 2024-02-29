def greet(): # defining a function
    print("Hello, welcome to python functions!")

greet() # calling the function so it runs in the terminal

########################

def greet(name): 
    print(f"Hello {name}, welcome to python functions!")

greet("Valerio") # calling the function so it runs in the terminal


###########

def greet(name, company): 
    print(f"Hello {name} from {company}, welcome to python functions!")

greet("Valerio", "nocrash.tech") # calling the function so it runs in the terminal


#######################

# greet() # this fails as nothing is called in it

##############


def greet(company, name="Bob"): 
    print(f"Hello {name} from {company}, welcome to python functions!")


greet("nocrash.tech")

########


def greet(name="Bob", company=None): 
    if company:
        print(f"Hello {name} from {company}, welcome to python functions!")
    else:
        print(f"Hello {name}, welcome to python functions!")

greet()

