password = input("Enter password: ")
password_length = len(password)

if password_length < 6:
  print("Weak password")
elif password_length < 10:
  print("Medium password")
else:
  print("Strong password")