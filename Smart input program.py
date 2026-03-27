# Smart Input Program

# Your details
name = "Aishwarya"
age = 22
hobby = "Badminton"

# Categorizing age
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

# Printing personalized message
print("\nHello", name + "!")
print("You are a", category + ".")
print("You enjoy", hobby + ". Keep it up!")