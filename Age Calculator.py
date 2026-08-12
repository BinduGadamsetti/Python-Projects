from datetime import date, datetime

print("=" * 50)
print("        🎂 AGE & LIFE CALCULATOR")
print("=" * 50)

# Get date of birth
dob_input = input("Enter your date of birth (DD-MM-YYYY): ")

try:
    dob = datetime.strptime(dob_input, "%d-%m-%Y").date()
except ValueError:
    print("❌ Invalid date format!")
    print("Please use DD-MM-YYYY, for example: 15-08-2005")
    exit()

today = date.today()

# Check if date of birth is in the future
if dob > today:
    print("❌ Date of birth cannot be in the future.")
    exit()

# Calculate age
age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

# Approximate life statistics
total_days = (today - dob).days
total_weeks = total_days // 7
total_months = age * 12
total_hours = total_days * 24

# Find next birthday
next_birthday = date(today.year, dob.month, dob.day)

if next_birthday <= today:
    next_birthday = date(today.year + 1, dob.month, dob.day)

days_until_birthday = (next_birthday - today).days

# Milestone checks
if age >= 18:
    adult_status = "You are legally an adult."
else:
    adult_status = f"You have {18 - age} year(s) until adulthood."

if age >= 18:
    license_status = "You may be eligible for a driving licence."
else:
    license_status = "You are not yet 18."

if age >= 18:
    vote_status = "You may be eligible for a voting."
else:
    vote_status = "You are not yet 18."



# Display results
print("\n" + "=" * 50)
print("             📊 YOUR LIFE STATS")
print("=" * 50)

print(f"Date of Birth       : {dob.strftime('%d-%m-%Y')}")
print(f"Current Date        : {today.strftime('%d-%m-%Y')}")
print(f"Age                 : {age} years")
print(f"Approx. Months Lived: {total_months}")
print(f"Approx. Weeks Lived : {total_weeks}")
print(f"Days Lived          : {total_days:,}")
print(f"Approx. Hours Lived : {total_hours:,}")

print("\n🎂 BIRTHDAY")
print("-" * 50)
print(f"Next birthday       : {next_birthday.strftime('%d-%m-%Y')}")
print(f"Days remaining      : {days_until_birthday}")

print("\n📌 STATUS")
print("-" * 50)
print(adult_status)
print(license_status)
print(vote_status)
print("\n" + "=" * 50)
print("       🚀 KEEP MAKING EVERY DAY COUNT!")
print("=" * 50)