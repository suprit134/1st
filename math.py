# math.py
try:
  a = float(input("Enter first number:"))
  b = float(input("Enter second number:"))

  print(f"Addition:{a + b}")
  print(f"Subrtraction:{a - b}")
except ValueError:
  print("Plese enter valid number.")
