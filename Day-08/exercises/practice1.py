# 1. Create an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# 2. Create tuples for sisters and brothers
sisters = ("Anna", "Bella")
brothers = ("Chris", "David")

print("Sisters:", sisters)
print("Brothers:", brothers)

# 3. Join siblings tuples
siblings = sisters + brothers
print("All siblings:", siblings)

# 4. Count siblings
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# 5. Add parents (tuples are immutable → convert to list → back to tuple)
family_members = siblings + ("Father", "Mother")
print("Family members:", family_members)