name=input("Enter your name: ")
year_of_birth=int(input("Enter your year of birth: "))
current_year=2026
age=current_year-year_of_birth
print("\nHello",name)
print("your age is",age)
if age>=60:
    print("You are a senior citizen.")
else:
    print("You are not a senior citizen.")
    