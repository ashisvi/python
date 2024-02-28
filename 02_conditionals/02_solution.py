from datetime import datetime

age = int(input("Enter your age: "))
day = datetime.now().date().strftime('%A')

price = 12 if age >= 18 else 8

if day == "wednesday":
  price -= 2

print(f"Ticket price: ${price}")