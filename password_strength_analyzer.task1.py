import re
import secrets
import string

def analyze_password(password):
    score = 0
    suggestions = []

    # Length
    if len(password) >= 16:
        score += 40
    elif len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 12 characters.")

    # Complexity
    checks = [
        (r"[a-z]", "Add lowercase letters."),
        (r"[A-Z]", "Add uppercase letters."),
        (r"\d", "Add numbers."),
        (r"[^A-Za-z0-9]", "Add special characters.")
    ]

    for pattern, suggestion in checks:
        if re.search(pattern, password):
            score += 15
        else:
            suggestions.append(suggestion)

    # Common passwords
    common = {"password", "123456", "qwerty", "admin", "letmein"}
    if password.lower() in common:
        score = 0
        suggestions.append("Avoid common passwords.")

    if score >= 80:
        strength = "Very Strong"
    elif score >= 60:
        strength = "Strong"
    elif score >= 40:
        strength = "Fair"
    else:
        strength = "Weak"

    return strength, score, suggestions


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


password = input("Enter password: ")
strength, score, suggestions = analyze_password(password)

print(f"\nStrength: {strength}")
print(f"Score: {score}/100")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Excellent password!")

print("\nSuggested password:", generate_password())