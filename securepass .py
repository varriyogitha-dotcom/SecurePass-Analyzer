# Import regular expressions module
import re

# Display program title
print("=" * 50)
print("         SecurePass Analyzer")
print("=" * 50)
print("Check how strong your password is.")
print()

# Get password from user
password = input("Enter your password: ")

# Initialize score and suggestions
score = 0
suggestions = []

# Check password length
if len(password) >= 8:
    score += 2
else:
    suggestions.append("Use at least 8 characters.")

# Check for uppercase letter
if re.search(r"[A-Z]", password):
    score += 2
else:
    suggestions.append("Add at least one uppercase letter.")

# Check for lowercase letter
if re.search(r"[a-z]", password):
    score += 2
else:
    suggestions.append("Add at least one lowercase letter.")

# Check for numbers
if re.search(r"[0-9]", password):
    score += 2
else:
    suggestions.append("Add at least one number.")

# Check for special characters
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 2
else:
    suggestions.append("Add at least one special character.")

# Decide password strength
if score <= 4:
    strength = "Weak"
    meter = "###-------"
elif score <= 7:
    strength = "Medium"
    meter = "######----"
else:
    strength = "Strong"
    meter = "##########"

# Display results
print()
print("=" * 50)
print("           PASSWORD ANALYSIS REPORT")
print("=" * 50)

print(f"Password Strength : {strength}")
print(f"Security Score    : {score}/10")
print(f"Strength Meter    : {meter}")

print("\nPassword Checks")
print("-" * 50)

print("Length (8+)              :", "Pass" if len(password) >= 8 else "Fail")
print("Uppercase Letter         :", "Pass" if re.search(r"[A-Z]", password) else "Fail")
print("Lowercase Letter         :", "Pass" if re.search(r"[a-z]", password) else "Fail")
print("Number                  :", "Pass" if re.search(r"[0-9]", password) else "Fail")
print("Special Character       :", "Pass" if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else "Fail")

print("\nSuggestions")
print("-" * 50)

if suggestions:
    for item in suggestions:
        print("- " + item)
else:
    print("Excellent! Your password is very strong.")

print("\nThank you for using SecurePass Analyzer.")
print("=" * 50)