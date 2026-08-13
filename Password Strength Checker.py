import string

print("=" * 50)
print("        🔐 PASSWORD STRENGTH CHECKER")
print("=" * 50)

password = input("Enter your password: ")

score = 0
feedback = []

# 1. Check length
if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters.")

# 2. Uppercase
if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

# 3. Lowercase
if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

# 4. Digit
if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add at least one number.")

# 5. Special character
if any(char in string.punctuation for char in password):
    score += 1
else:
    feedback.append("Add at least one special character.")

# 6. Check common passwords
common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "password123"
]

if password.lower() in common_passwords:
    score = 0
    feedback.append("This is a commonly used password.")

# 7. Check repeated characters
if len(set(password)) < len(password) / 2:
    feedback.append("Avoid using too many repeated characters.")
    score -= 1

# Keep score between 0 and 6
score = max(0, min(score, 6))

# Determine strength
if score <= 2:
    strength = "🔴 Weak"
elif score <= 4:
    strength = "🟡 Moderate"
else:
    strength = "🟢 Strong"

# Display result
print("\n" + "=" * 50)
print("             📊 RESULT")
print("=" * 50)

print(f"Password Length : {len(password)}")
print(f"Security Score  : {score}/6")
print(f"Strength        : {strength}")

if feedback:
    print("\n💡 Suggestions:")
    for item in feedback:
        print(f"• {item}")
else:
    print("\n✅ Excellent! Your password satisfies all checks.")

print("=" * 50)