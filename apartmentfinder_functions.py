# Define apt_search1 function with required parameters
def apt_search1(city, max_rent, min_beds, pets_allowed):
    # Check if pets are allowed and assign correct string value to pets variable
    if pets_allowed:
        pets = " that allows pets"
    else:
        pets = ""
    # Print f-string output to pass parameter and function variable values to the string
    print(
        f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments{pets}, all within a budget of ${max_rent} per month...")

# Instantiate apt_search1 correctly (ie with parameter values)
apt_search1("Detroit", 2000, 3, True)
print()

# Define apt_search2 function with required parameters, min_beds and pets_allowed have default values assigned
def apt_search2(city, max_rent, min_beds = 2, pets_allowed = False):
    # Check if pets are allowed and assign correct string value to pets variable
    if pets_allowed:
        pets = " that allows pets"
    else:
        pets = ""
    # Print f-string output to pass parameter and function variable values to the string
    print(
        f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments{pets}, all within a budget of ${max_rent} per month...")

# Instantiate apt_search2 function as instructed in assignment
apt_search2("Chicago", 1500)
print()
apt_search2("Atlanta", 2300, 3)
print()
apt_search2(city = "New York", max_rent = 2500, pets_allowed = True)


# Define lambda functions as instructed
plus_one_hundred = lambda x : x + 100
square_num = lambda x : x ** 2
concatenate = lambda x : "- " + x
divide_by_three = lambda x : x / 3

print()

# Print instantiated lambda functions
print(plus_one_hundred(100))
print()
print(square_num(4))
print()
print(concatenate('hello'))
print()
print(divide_by_three(9))