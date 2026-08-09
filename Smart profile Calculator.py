print("===================================")
print("     SMART PERSONAL PROFILE")
print("===================================")

name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
college = input("Enter your college: ").strip()
branch = input("Enter your branch: ").strip()
skill = input("Enter your main programming skill: ").strip()
projects = int(input("How many projects have you completed? "))

# Calculate approximate birth year
birth_year = 2026 - age

# Determine experience level
if projects == 0:
    level = "Beginner"
elif projects <= 3:
    level = "Learner"
elif projects <= 7:
    level = "Intermediate"
else:
    level = "Project Builder"

print("\n===================================")
print("        YOUR PROFILE")
print("===================================")

print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"College    : {college}")
print(f"Branch     : {branch}")
print(f"Main Skill : {skill}")
print(f"Projects   : {projects}")
print(f"Level      : {level}")
print(f"Born Around: {birth_year}")

print("\n-----------------------------------")

if projects >= 5:
    print(f"{name}, you're building strong project experience! 🚀")
else:
    print(f"{name}, keep building more projects! 💻")

print("===================================")