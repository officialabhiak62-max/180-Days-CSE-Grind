import re
def check_password_strength(password):
    strength = 0
    remarks = ""
    if len(password) >= 8:
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    if strength == 5:
        remarks = "Very Strong "
    elif strength == 4:
        remarks = "Strong "
    elif strength == 3:
        remarks = "Medium "
    elif strength == 2:
        remarks = "Weak "
    else:
        remarks = "Very Weak "

    return remarks
pwd = input("Enter your password: ")
print("Password Strength:", check_password_strength(pwd))

