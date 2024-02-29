city = "Warsaw" # Global Variable and is accessible everywhere

def greet(name="Bob", company=None): 
    country = "Poland" # This is not usable outside the fucntion, like below

    if company:
        print(f"Hello {name} from {company}, welcome to python functions in {city}, {country}!")
    else:
        print(f"Hello {name}, welcome to python functions!")

print(country)
print(greet("Valerio", "nocrash.tech"))

