# Challenge Problem

weight = float(input("Enter the total weight (lbs): "))
destination = input("Enter destination (domestic/international): ").lower()
membership = input("Enter membership type (standard/premium): ").lower()

base_cost = 10
extra_cost = 0
details = f"Base ${base_cost}"

if weight > 20:
    extra_cost += 5
    details += " + Overweight $5"

total_cost = base_cost + extra_cost

if membership == "premium":
    
    total_cost = total_cost * 0.8  
    details += ", Premium 20% discount applied, International fee waived."
else:
 
    if destination == "international":
        total_cost *= 2  
        details += ", International fee applied."


print(f"\nWeight (lbs): {weight}")
print(f"Destination (domestic/international): {destination}")
print(f"Membership (standard/premium): {membership}")
print(f"Final Shipping Cost: ${total_cost:.2f}")
print(f"(Details: {details})")