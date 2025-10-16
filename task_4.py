# Task 4

a
age = int(input("Enter your age: "))
is_student = input("Are you a student? (True/False): ") == "True"


price = 12

if age <= 12:
    discount = 3   # children discount
elif age >= 65:
    discount = 4   # senior discount
elif is_student:
    discount = 2   # student discount
else:
    discount = 0   # no discount

final_price = price - discount


print(f"\nAge: {age}")
print(f"Is student? {is_student}")
print(f"Your ticket price is ${final_price}.")