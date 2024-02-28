distance = int(input("Enter distance: "))

if distance < 3:
  transportation = "Walk"
elif distance < 15:
  transportation = "Bike"
else:
  transportation = "Car"

print(f"Transportation: {transportation}")