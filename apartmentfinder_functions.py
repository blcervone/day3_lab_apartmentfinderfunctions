def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        pets = "that allows pets"
    else:
        pets = ""
    print(
        f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments {pets}, all within a budget of ${max_rent} per month...")


apt_search1("Detroit", 2000, 3, True)
print()

def apt_search2(city, max_rent, min_beds = 2, pets_allowed = False):
    if pets_allowed:
        pets = "that allows pets"
    else:
        pets = ""
    print(
        f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments {pets}, all within a budget of ${max_rent} per month...")

apt_search2("Chicago", 1500)
print()
apt_search2("Atlanta", 2300, 3)
print()
apt_search2(city = "New York", max_rent = 2500, pets_allowed = True)

plus_one_hundred = lambda x : x + 100
square_num = lambda x : x ** 2
concatenate = lambda x : "- " + x
divide_by_three = lambda x : x / 3

print()

print(plus_one_hundred(100))
print(square_num(4))
print(concatenate('hello'))
print(divide_by_three(9))